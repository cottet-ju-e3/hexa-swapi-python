from abc import ABC, abstractmethod

from rebel_rescue.fleet.fleet import Fleet


class AssembleAFleet(ABC):
    @abstractmethod
    def for_passengers(self, number_of_passengers: int) -> Fleet: ...
