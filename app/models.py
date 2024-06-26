from pydantic import BaseModel
from typing import List


class Event(BaseModel):
    id: str
    title: str
    start_date: str
    end_date: str
    sale_mode: str


class EventList(BaseModel):
    events: List[Event]
