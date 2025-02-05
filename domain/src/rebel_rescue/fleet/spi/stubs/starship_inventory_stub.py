from typing import override

from rebel_rescue.fleet.spi.starship_inventory import StarshipInventory
from rebel_rescue.fleet.starship import Starship

starships: list[Starship] = [
    Starship("X-Wing", 0),
    Starship("Millenium Falcon", 6),
    Starship("Rebel transport", 90),
    Starship("Mon Calamari Star Cruisers", 1200),
    Starship("CR90 corvette", 600),
]


class StarshipInventoryStub(StarshipInventory):
    @override
    def starships(self) -> list[Starship]:
        return starships
