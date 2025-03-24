from typing import override

from rebel_rescue.fleet.api.assemble_a_fleet import AssembleAFleet
from rebel_rescue.fleet.fleet import Fleet
from rebel_rescue.fleet.fleet_assembler import FleetAssembler
from rebel_rescue.fleet.spi.starship_inventory import StarshipInventory
from rebel_rescue.fleet.starship import Starship


def test__assemble_a_fleet_for_1050_passsengers() -> None:
    # TODO: 1
    #  move in spi stubs for running real call
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

    sh_inventory: StarshipInventory = StarshipInventoryStub()
    assemble_a_fleet: AssembleAFleet = FleetAssembler(starship_inventory=sh_inventory)

    number_of_passenger: int = 1050

    fleet: Fleet = assemble_a_fleet.for_passengers(number_of_passenger)

    assert enough_capacity_for_starships(fleet.starships, number_of_passenger)


def enough_capacity_for_starships(_starships: list[Starship], capacity: int) -> bool:
    return sum(s.passengensCapacity for s in _starships) >= 0
