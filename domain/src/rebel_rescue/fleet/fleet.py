from dataclasses import field
import uuid
from rebel_rescue.fleet.starship import Starship
from pydantic import BaseModel


class Fleet(BaseModel):
    uid: uuid.UUID = field(default_factory=uuid.uuid4)
    starships: list[Starship] = field(default_factory=list)
