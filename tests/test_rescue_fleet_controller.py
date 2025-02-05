from typing import TYPE_CHECKING
from fastapi import status

if TYPE_CHECKING:
    from starlette.testclient import TestClient


def test_system_check_should_respond_ok(fake_test_api: "TestClient") -> None:
    response = fake_test_api.post("/rescueFleets", json={"number_of_passenger": 12})

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["uid"] is not None
    assert len(response.json()["starships"]) == 2
    assert response.json()["starships"][0]["name"] == "Millenium Falcon"
    assert response.json()["starships"][0]["passengensCapacity"] == 6
