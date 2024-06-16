from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class Healthy:
    message: str = 'Service "a" is healthy.'
