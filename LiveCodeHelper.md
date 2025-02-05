## test
Add assemble a fleet call (`hexa_assemble_a_fleet`)

## Add interface contract
* create package `api` in domain [fleet](domain/src/rebel_rescue/fleet)
* Add `assemble_a_fleet.py` in  package [api](domain/src/rebel_rescue/fleet/api)  
  *  create interface `AssembleAFleet` with contract in [test_assemble_a_fleet](domain/tests/test_assemble_a_fleet.py)

## Add AssembleAFleet api implementation
Add implementation `FleetAssembler` in [fleet](domain/src/rebel_rescue/fleet/) package
  - Add `fleet_assembler.py` of AssembleAFleet 
  - with a `StarshipInventory` attribute.
  - add StarshipInventory.starships() -> list[Starship] in domain

## Add StarshipInventory in spi
* create folder `spi` in [fleet](domain/src/rebel_rescue/fleet/)
* add starship_inventory.py in [spi](domain/src/rebel_rescue/fleet/spi)
- Add `StarshipInventory` interface with method `starships()`

## domain
- Add business logic (commands : `hexa_business_logic`)
- Add implementation detail commands : `hexa_select_starships`

## Test
- Add Stub (commands: `hexa_starship_stub`)
- run test
- Applause

## Commands:
### hexa_assemble_a_fleet 
```python
assemble_a_fleet.for_passengers(number_of_passenger)
```

### hexa_business_logic
```python
starships: list[Starship] = self.get_starships_having_passenger_capacity()
rescue_starships: list[Starship] = self.select_starships(
  number_of_passengers, starships
)

return Fleet(starships=rescue_starships)
```

### hexa_select_starships
```python
def select_starships(self, number_of_passengers, starships):
  rescue_starships = []
  while number_of_passengers > 0:
    starship = starships.pop()
    number_of_passengers -= starship.passengensCapacity
    rescue_starships.append(starship)
  return rescue_starships


def get_starships_having_passenger_capacity(self):
  starships = filter(
    lambda s: s.passengensCapacity > 0, self.starships_inventory.starships()
  )
  return sorted(starships, key=lambda s: s.passengensCapacity, reverse=True)
```
