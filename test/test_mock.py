import unittest
from unittest import mock
import check_systemd
from helper import Capturing, mock_main

# POpen class
# Line 334 p = subprocess.Popen(['systemctl', 'list-units', '--all'],
# SystemctlListUnitsResource

# Line 460 p = subprocess.Popen(['systemd-analyze'],
# SystemdAnalyseResource

# Line 576 p = subprocess.Popen(['systemctl', 'list-timers', '--all'],
# SystemctlListTimersResource

# Line 656 p = subprocess.Popen(['systemctl', 'is-active', self.unit],
# SystemctlIsActiveResource


class TestMock(unittest.TestCase):

    def test_ok(self):
        result = mock_main(popen_stdout_files=[
                           'systemctl-list-units-ok.txt',
                           'systemd-analyze-34-min.txt'])
        result['sys_exit'].assert_called_with(0)

    def test_help(self):
        with mock.patch('sys.exit'), \
                mock.patch('sys.argv', ['check_systemd.py', '--help']):
            with Capturing() as output:
                check_systemd.main()

        self.assertIn('usage: check_systemd', output.tostring())
        # sys_exit.assert_called_with(0)

    def test_single_unit(self):
        with mock.patch('sys.exit') as sys_exit, \
                mock.patch('check_systemd.subprocess.run') as run, \
                mock.patch('check_systemd.subprocess.Popen') as Popen, \
                mock.patch('sys.argv', ['check_systemd.py', '-u',
                                        'nginx.service']):
            run.return_value.returncode = 0
            process = Popen.return_value
            process.communicate.return_value = (b'active', None)
            with Capturing():
                check_systemd.main()
            # self.assertIn('SYSTEMD OK - nginx.service: active', output)

            sys_exit.assert_called_with(0)

    def test_multiple_units(self):
        result = mock_main(popen_stdout_files=[
                           'systemctl-list-units-ok.txt',
                           'systemd-analyze-34-min.txt'])
        result['sys_exit'].assert_called_with(0)


if __name__ == '__main__':
    unittest.main()
