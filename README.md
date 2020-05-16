[![pypi.org](http://img.shields.io/pypi/v/check_systemd.svg)](https://pypi.python.org/pypi/check_systemd)
[![Build Status](https://travis-ci.org/Josef-Friedrich/check_systemd.svg?branch=master)](https://travis-ci.org/Josef-Friedrich/check_systemd)

# check_systemd

`check_systemd` is a
[Nagios](https://www.nagios.org) / [Icinga](https://icinga.com)
monitoring plugin to check [systemd](https://systemd.io) for failed
units.

This Python script will report a degraded system to your monitoring solution.
It requires only the
[nagiosplugin](https://nagiosplugin.readthedocs.io/en/stable) library.

You can also test a single service with the `-u, --unit` parameter.

Released under GNU GPLv2 License.

## Installation

```
pip3 install check_systemd
```

## Command line interface

```
usage: check_systemd [-h] [-c SECONDS] [-e UNIT | -u UNIT] [-t]
                     [-W DEAD_TIMERS_WARNING] [-C DEAD_TIMERS_CRITICAL] [-v]
                     [-V] [-w SECONDS]

Copyright (c) 2014-18 Andrea Briganti a.k.a 'Kbyte' <kbytesys@gmail.com>
Copyright (c) 2019-20 Josef Friedrich <josef@friedrich.rocks>

Nagios / Icinga monitoring plugin to check systemd for failed units.

optional arguments:
  -h, --help            show this help message and exit
  -c SECONDS, --critical SECONDS
                        Startup time in seconds to result in critical status.
  -e UNIT, --exclude UNIT
                        Exclude a systemd unit from the checks. This option can
                        be applied multiple times, for example: -e mnt-
                        data.mount -e task.service. Regular expressions can be
                        used to exclude multiple units at once, for example: -e
                        'user@\d+\.service'. For more informations see the
                        Python documentation about regular expressions
                        (https://docs.python.org/3/library/re.html).
  -u UNIT, --unit UNIT  Name of the systemd unit that is being tested.
  -t, --dead-timers     Check for dead / inactive timers.
  -W DEAD_TIMERS_WARNING, --dead-timers-warning DEAD_TIMERS_WARNING
                        Time ago in seconds for dead / inactive timers to
                        trigger a warning state (by default 6 days).
  -C DEAD_TIMERS_CRITICAL, --dead-timers-critical DEAD_TIMERS_CRITICAL
                        Time ago in seconds for dead / inactive timers to
                        trigger a critical state (by default 7 days).
  -v, --verbose         Increase output verbosity (use up to 3 times).
  -V, --version         show program's version number and exit
  -w SECONDS, --warning SECONDS
                        Startup time in seconds to result in warning status.

Performance data:
  - count_units
  - startup_time
  - units_activating
  - units_active
  - units_failed
  - units_inactive

```

## Project pages

* https://github.com/Josef-Friedrich/check_systemd
* https://exchange.icinga.com/joseffriedrich/check_systemd
* https://exchange.nagios.org/directory/Plugins/System-Metrics/Processes/check_systemd/details

## Testing

```
pyenv install 3.7.6
pyenv install 3.8.1
pyenv local 3.7.6 3.8.1
pip3 install tox
tox
```

## Deploying

Edit version number in check_systemd.py (without `v`)

```
git tag v2.0.11
git push --tags
```
