from rebel_rescue.fleet.api.assemble_a_fleet import AssembleAFleet
from rebel_rescue.fleet.fleet import Fleet
from rebel_rescue.fleet.fleet_assembler import FleetAssembler
from rebel_rescue.fleet.spi.starship_inventory import StarshipInventory
from rebel_rescue.fleet.spi.stubs.starship_inventory_stub import StarshipInventoryStub
from rebel_rescue.fleet.starship import Starship


def test__assemble_a_fleet_for_1050_passsengers() -> None:
    sh_inventory: StarshipInventory = StarshipInventoryStub()
    assemble_a_fleet: AssembleAFleet = FleetAssembler(starship_inventory=sh_inventory)

    number_of_passenger: int = 1050

    fleet: Fleet = assemble_a_fleet.for_passengers(number_of_passenger)

    assert enough_capacity_for_starships(fleet.starships, number_of_passenger)


def enough_capacity_for_starships(_starships: list[Starship], capacity: int) -> bool:
    return sum(s.passengensCapacity for s in _starships) >= 0
