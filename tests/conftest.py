from typing import TYPE_CHECKING

import pytest
from starlette.testclient import TestClient

from hexa_swapi_infra.controllers.api import make_app

if TYPE_CHECKING:
    from fastapi import FastAPI


@pytest.fixture(scope="session")
def fake_app() -> "FastAPI":
    return make_app()


@pytest.fixture(scope="session")
def fake_test_api(fake_app: "FastAPI") -> TestClient:
    return TestClient(fake_app)
