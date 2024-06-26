from typing import List
import requests
import xmltodict
import logging
from fastapi import Depends, APIRouter

from app.services.redis_service import RedisService, get_redis_service
from app.models import Event
from app.utils.date_utils import is_date_within_range


class EventService:
    """
    Service for handling event-related operations, including fetching events from an API
    and retrieving events by date range, utilizing a Redis cache.
    """

    def __init__(self, redis_service: RedisService):
        """
        Initialize the EventService with a Redis service for caching.

        Args:
            redis_service (RedisService): The Redis service to use for caching event data.
        """
        self.redis = redis_service
        self.base_url = "https://provider.code-challenge.feverup.com/api/events"
    
    def fetch_events(self) -> List[Event]:
        """
        Fetch the event list from the API endpoint.

        This method makes an HTTP GET request to the API endpoint and parses the XML response
        to extract event details. Only events with a "sell_mode" of "online" are included.

        Returns:
            List[dict]: A list of dictionaries containing event details.
        """
        response = requests.get(self.base_url)
        if response.status_code == 200:
            data = xmltodict.parse(response.content)
            events = [
                {
                    "base_event_id": event["@base_event_id"],
                    "title": event["@title"],
                    "event_id": event["event"]["@event_id"],
                    "event_start_date": event["event"]["@event_start_date"],
                    "event_end_date": event["event"]["@event_end_date"],
                    "zones": event["event"]["zone"]
                }
                for event in data["eventList"]["output"]["base_event"]
                if event["@sell_mode"] == "online"
            ]
            return events
        return []

    def get_events_by_date_range(self, start_date: str, end_date: str) -> List[dict]:
        """
        Retrieve the event list for a specified date range from the cache or the API.

        This method first checks the Redis cache for events within the specified date range.
        If the events are not found in the cache, it fetches them from the API and filters them
        by the given date range. Events are then stored in the cache for future requests.

        Args:
            start_date (str): The start date of the date range (inclusive).
            end_date (str): The end date of the date range (inclusive).

        Returns:
            List[dict]: A list of dictionaries containing event details within the specified date range.
        """
        cache_key = f"{start_date}_{end_date}"
        cached_events = self.redis.get(cache_key)
        if cached_events:
            return cached_events

        all_events = self.fetch_events()
        filtered_events = [
            event for event in all_events
            if is_date_within_range(event["event_start_date"], start_date, end_date)
        ]
        return filtered_events


def get_event_service(redis_service: RedisService = Depends(get_redis_service)) -> EventService:
    """
    Dependency injection function to provide an instance of EventService.

    This function creates and returns an EventService instance, using the provided
    RedisService instance for caching.

    Args:
        redis_service (RedisService): The RedisService instance to be used by EventService.
            It is injected by FastAPI's Depends function, which resolves the dependency.

    Returns:
        EventService: An instance of EventService initialized with the provided RedisService.
    """
    return EventService(redis_service)
