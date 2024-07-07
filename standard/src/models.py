from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class Healthy:
    message: str = "Service is healthy."


@dataclass(frozen=True)
class Fibonacci:
    number: int


@dataclass(frozen=True)
class AddOne:
    number: int
