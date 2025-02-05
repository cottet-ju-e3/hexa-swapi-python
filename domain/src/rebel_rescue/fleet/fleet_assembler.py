from typing import override

from rebel_rescue.fleet.api.assemble_a_fleet import AssembleAFleet
from rebel_rescue.fleet.fleet import Fleet
from rebel_rescue.fleet.spi.starship_inventory import StarshipInventory
from rebel_rescue.fleet.starship import Starship


class FleetAssembler(AssembleAFleet):
    def __init__(self, starship_inventory: StarshipInventory):
        self.starships_inventory: StarshipInventory = starship_inventory

    @override
    def for_passengers(self, number_of_passengers: int) -> Fleet:
        starships: list[Starship] = self.get_starships_having_passenger_capacity()
        rescue_starships: list[Starship] = self.select_starships(
            number_of_passengers, starships
        )

        return Fleet(starships=rescue_starships)

    def get_starships_having_passenger_capacity(self):
        starships = filter(
            lambda s: s.passengensCapacity > 0, self.starships_inventory.starships()
        )
        return sorted(starships, key=lambda s: s.passengensCapacity, reverse=True)

    def select_starships(self, number_of_passengers, starships):
        rescue_starships = []
        while number_of_passengers > 0:
            starship = starships.pop()
            number_of_passengers -= starship.passengensCapacity
            rescue_starships.append(starship)
        return rescue_starships
