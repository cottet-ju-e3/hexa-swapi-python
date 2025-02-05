from rebel_rescue.fleet.fleet import Fleet
from rebel_rescue.fleet.starship import Starship

# starship_stub

def test__assemble_a_fleet_for_1050_passsengers() -> None:
    # Given
    number_of_passenger: int = 1050

    # When
    fleet: Fleet = None

    #Then
    assert enough_capacity_for_starships(fleet.starships, number_of_passenger)


def enough_capacity_for_starships(_starships: list[Starship], capacity: int) -> bool:
    return sum(s.passengensCapacity for s in _starships) >= capacity
