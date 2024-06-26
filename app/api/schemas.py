from pydantic import BaseModel
from typing import List, Optional

class EventFilterParams(BaseModel):
    start_date: str
    end_date: str

class EventResponse(BaseModel):
    events: List[dict]
