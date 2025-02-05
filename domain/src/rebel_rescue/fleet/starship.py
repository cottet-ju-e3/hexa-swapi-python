from dataclasses import dataclass


@dataclass
class Starship:
    name: str
    passengensCapacity: int
    cargoCapacity: int = 0
