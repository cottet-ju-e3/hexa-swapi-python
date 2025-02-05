from typing import TypeVar, Generic, Optional

from pydantic import BaseModel

DataT = TypeVar('DataT')

class SwapiResponse(BaseModel, Generic[DataT]):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: list[DataT]
