from abc import ABC, abstractmethod

from rebel_rescue.fleet.starship import Starship


class StarshipInventory(ABC):
    @abstractmethod
    def starships(self) -> list[Starship]:
        pass
