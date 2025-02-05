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
        starships : list[Starship] = []
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
    try :
        int(swapi_starship.passengers)
        int(swapi_starship.cargo_capacity)
        return True
    except ValueError:
        return False
