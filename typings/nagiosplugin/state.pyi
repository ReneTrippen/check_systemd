from dataclasses import dataclass
from typing import Literal

def worst(states: list[ServiceState]) -> ServiceState: ...
@dataclass
class ServiceState:
    code: Literal[0, 1, 2, 3]
    text: Literal["ok", "warning", "critical", "unknown"]

    def __str__(self) -> str: ...
    def __int__(self) -> Literal[0, 1, 2, 3]: ...

Ok: ServiceState = ...

Warn: ServiceState = ...

Critical: ServiceState = ...

Unknown: ServiceState = ...
