import logging

from rebel_rescue.fleet.spi.starship_inventory import StarshipInventory
from rebel_rescue.fleet.starship import Starship

logger = logging.getLogger(__name__)

class SwapiClient(StarshipInventory):
    def starships(self) -> list[Starship]:
        pass
