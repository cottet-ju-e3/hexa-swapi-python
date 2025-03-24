from __future__ import annotations


from fastapi import FastAPI, APIRouter

app = FastAPI()


rescue_fleet_router = APIRouter()

# TODO: 0 Add POST controller(/"rescueFleets") that "assemble_a_fleet" with:
#  Body with number_of_passengers
#  Call to AssembleAFleet
#  return a Fleet
#  helper: hexa_add_endpoint
