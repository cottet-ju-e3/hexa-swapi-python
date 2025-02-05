from pydantic import BaseModel


class SwapiStarship(BaseModel):
    name: str
    passengers: str
    cargo_capacity: str
