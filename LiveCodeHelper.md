# Lets add swapi implementation

## Create a SWAPI client that implements Starship inventory

### Implementation
#### Create empty implementation `infrastructure/swapi`   
* [hexa_swapi_infra](infrastructure/src/hexa_swapi_infra/swapi)
* add `swapi_client.py`
* that return empty list[starships]
#### Add ACL in `swapi/models` folder
* [hexa_swapi_infra](infrastructure/src/hexa_swapi_infra/swapi)
* Add swapi_starship.py (`swapi_starship`)
  * name (str)
  * passengers (str)
  * cargo_capacity (str)
* Add swapi_response.py (`swapi_response`)
  * count: int
  * next: Optional[str]
  * previous: Optional[str]
  * results: list[DataT] 
* Finish client implementation with real call to swapi url  (`swapi_client`)
  * BASE_URL = "https://swapi.dev/api"
  * STARSHIPS = "starships"
#### Add test context for test controller for not use real call to swapi
* Add `is_pytest()` to inject
 * InventoryStub in test
 * SwapiClient in prod

## Run test
```shell
uv run pytest
```

## Run main
```shell
uv run main
```

## Commands:
### swapi_starship
```python
from pydantic import BaseModel


class SwapiStarship(BaseModel):
  name: str
  passengers: str
  cargo_capacity: str
```

### swapi_response
```python
from typing import TypeVar, Generic, Optional

from pydantic import BaseModel

DataT = TypeVar('DataT')


class SwapiResponse(BaseModel, Generic[DataT]):
  count: int
  next: Optional[str]
  previous: Optional[str]
  results: list[DataT]
```

### swapi_client
```python
import logging

from hexa_swapi_infra.swapi.models.swapi_response import SwapiResponse
from hexa_swapi_infra.swapi.models.swapi_starship import SwapiStarship
import httpx
from rebel_rescue.fleet.spi.starship_inventory import StarshipInventory
from rebel_rescue.fleet.starship import Starship

BASE_URL = "https://swapi.dev/api"
STARSHIPS = "starships"

logger = logging.getLogger(__name__)


class SwapiClient(StarshipInventory):
  def starships(self) -> list[Starship]:
    next_url = f"{BASE_URL}/{STARSHIPS}"
    starships: list[Starship] = []
    while next_url:
      logger.error(f"Calling {next_url}")
      response = httpx.get(next_url)
      response.raise_for_status()
      swapi_response = SwapiResponse[SwapiStarship].model_validate(response.json())
      next_url = swapi_response.next
      starships.extend(_to_domain(swapi_response.results))
    return starships


def _to_domain(swapi_starships: list[SwapiStarship]) -> list[Starship]:
  return [
    Starship(name=swsh.name, passengensCapacity=int(swsh.passengers))
    for swsh in swapi_starships
    if _is_valid(swsh)
  ]


def _is_valid(swapi_starship: SwapiStarship) -> bool:
  try:
    int(swapi_starship.passengers)
    int(swapi_starship.cargo_capacity)
    return True
  except ValueError:
    return False
```
