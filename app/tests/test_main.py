import pytest
import redis
from fastapi.testclient import TestClient

from app.main import app

@pytest.fixture
def client():
    """Create a FastAPI TestClient fixture."""
    return TestClient(app)


def test_read_main(client):
    """Test the root endpoint."""
    response = client.get(
        "/events?starts_at=2021-06-30T21:00:01&ends_at=2021-08-30T21:00:00"
        )
    assert response.status_code == 200


# Test connection to Redis server
def test_redis_connection():
    redis_service = redis.Redis(host='localhost', port=6379)
    assert redis_service.ping()  # Check if the Redis server is available


# Test set, get, and delete operations in Redis
def test_redis_operations():
    redis_service = redis.Redis(host='localhost', port=6379)
    key = "test_key"
    value = "test_value"

    # Set key-value pair
    redis_service.set(key, value)

    assert redis_service.get(key).decode('utf-8') == value  # Check if the key-value pair is correctly set

    # Delete key
    redis_service.delete(key)
    assert redis_service.get(key) is None  # Check if the key is deleted