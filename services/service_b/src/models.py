from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class Healthy:
    message: str = 'Service "b" is healthy.'
