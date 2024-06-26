from fastapi import APIRouter, Depends, Query
from datetime import datetime

from app.services.event_service import EventService, get_event_service
from app.api.schemas import EventResponse

router = APIRouter()


@router.get("/events", response_model=EventResponse)
def get_events(
    starts_at: str = Query("2021-07-30T21:00:01", description="Start date in ISO format"),
    ends_at: str = Query("2021-08-30T21:00:00", description="Start date in ISO format"),
    event_service: EventService = Depends(get_event_service)
) -> EventResponse:
    """
    Retrieve events within a specified date range.

    Fetches events using the provided EventService instance, filtering them based on
    the given start and end dates. The filtered events are returned in an EventResponse object.

    Args:
        starts_at (str): The start date of the date range (inclusive).
        ends_at (str): The end date of the date range (inclusive).
        event_service (EventService, optional): Instance of EventService retrieved via dependency injection.
            Defaults to using the get_event_service function for initialization.

    Returns:
        EventResponse: An EventResponse object containing a list of events filtered by the specified date range.
    """
    events = event_service.get_events_by_date_range(starts_at, ends_at)
    return EventResponse(events=events)
