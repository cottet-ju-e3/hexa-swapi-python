from fastapi import FastAPI
from fastapi_injector import attach_injector
from hexa_swapi_infra.test_utils.is_test_context import is_pytest
from injector import Injector, inject

from hexa_swapi_infra.controllers.rescue_fleet_controller import rescue_fleet_router
from hexa_swapi_infra.swapi.swapi_client import SwapiClient
from rebel_rescue.fleet.api.assemble_a_fleet import AssembleAFleet
from rebel_rescue.fleet.fleet_assembler import FleetAssembler
from rebel_rescue.fleet.spi.starship_inventory import StarshipInventory
from rebel_rescue.fleet.spi.stubs.starship_inventory_stub import StarshipInventoryStub


def make_app() -> FastAPI:
    api = FastAPI(
        title="Consumption audit API",
        description="Consumption audit REST API",
        root_path="/",
        docs_url="/docs",
    )

    api.include_router(rescue_fleet_router)
    inj = Injector()

    inject(FleetAssembler)
    inj.binder.bind(AssembleAFleet, to=FleetAssembler)
    if is_pytest():
        inj.binder.bind(StarshipInventory, to=StarshipInventoryStub)
    else:
        inj.binder.bind(StarshipInventory, to=SwapiClient)
    attach_injector(api, inj)

    return api
