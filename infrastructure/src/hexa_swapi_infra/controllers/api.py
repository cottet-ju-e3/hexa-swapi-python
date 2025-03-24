from fastapi import FastAPI
from fastapi_injector import attach_injector
from injector import Injector

from hexa_swapi_infra.controllers.rescue_fleet_controller import rescue_fleet_router


def make_app() -> FastAPI:
    api = FastAPI(
        title="Rescue Fleets API",
        description="Hexa architecture implementation with Star wars RescueFleet example ",
        root_path="/",
        docs_url="/docs",
    )

    api.include_router(rescue_fleet_router)
    inj = Injector()

    # TODO: 2  inject assemble a fleet with repository in API
    #  hexa_inject_in_api

    attach_injector(api, inj)

    return api
