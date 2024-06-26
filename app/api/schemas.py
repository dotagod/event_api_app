from typing import List, Optional

from pydantic import BaseModel

class EventFilterParams(BaseModel):
    start_date: str
    end_date: str


class EventResponse(BaseModel):
    events: List[dict]
