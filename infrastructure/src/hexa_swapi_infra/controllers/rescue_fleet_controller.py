from __future__ import annotations

from dataclasses import dataclass

from fastapi import FastAPI, APIRouter
from fastapi_injector import Injected
from rebel_rescue.fleet.api.assemble_a_fleet import AssembleAFleet
from rebel_rescue.fleet.fleet import Fleet

app = FastAPI()


rescue_fleet_router = APIRouter()


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
