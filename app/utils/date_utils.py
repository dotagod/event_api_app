from datetime import datetime


def is_date_within_range(event_date: str, start_date: str, end_date: str) -> bool:
    """
    Check if an event date falls within a specified date range.

    Args:
        event_date (str): The date of the event in ISO 8601 format ('YYYY-MM-DDTHH:MM:SS').
        start_date (str): The start date of the date range (inclusive) in ISO 8601 format.
        end_date (str): The end date of the date range (inclusive) in ISO 8601 format.

    Returns:
        bool: True if the event date is within the specified date range; False otherwise.
    """
    event_datetime = datetime.strptime(event_date, '%Y-%m-%dT%H:%M:%S')
    start_datetime = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S')
    end_datetime = datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S')

    return start_datetime <= event_datetime <= end_datetime
