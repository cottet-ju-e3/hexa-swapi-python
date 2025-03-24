# Lets add rest implementation

## Show API test
* [test_rescue_fleet_controller.py](tests/test_rescue_fleet_controller.py)
* [conftest.py](tests/conftest.py)

## Implement
* 0 
  * Add POST controller(/"rescueFleets") that "assemble_a_fleet"
  * [rescue_fleet_controller.py](infrastructure/src/hexa_swapi_infra/controllers/rescue_fleet_controller.py)
* 1
  * Move test stub in spi
  * [test_rescue_fleet_controller.py](tests/test_rescue_fleet_controller.py)
* 2
  * Inject assemble a fleet with repository in API
  * [api.py](infrastructure/src/hexa_swapi_infra/controllers/api.py)

## Run test
```shell
uv run pytest
```

## Commands:
### hexa_add_endpoint
```python
@dataclass
class AssembleAFleetRequestBody:
  number_of_passenger: int


@rescue_fleet_router.post("/rescueFleets")
def assemble_a_fleet(
        assemble_a_fleet_request_body: AssembleAFleetRequestBody,
        fleet_assembler: AssembleAFleet = Injected(AssembleAFleet),
) -> Fleet | None:
  fleet = fleet_assembler.for_passengers(
    assemble_a_fleet_request_body.number_of_passenger
  )
  return fleet
```

### hexa_inject_in_api
```python
inject(FleetAssembler)
inj.binder.bind(AssembleAFleet, to=FleetAssembler)
inj.binder.bind(StarshipInventory, to=StarshipInventoryStub)
```
