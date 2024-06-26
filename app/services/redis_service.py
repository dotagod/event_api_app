import redis
from fastapi import Depends


class RedisService:
    """
    A service for interacting with a Redis data store.
    
    This service provides basic methods to set, get, and delete keys in a Redis store.
    """

    def __init__(self, host='localhost', port=6379):
        """
        Initialize the RedisService with the given host and port.
        
        Args:
            host (str): The Redis server host. Defaults to 'localhost'.
            port (int): The Redis server port. Defaults to 6379.
        """
        self.client = redis.Redis(host=host, port=port, decode_responses=True)

    def set(self, key: str, value: str, expire=None):
        """
        Set a key-value pair in Redis with an optional expiration time.
        
        Args:
            key (str): The key to set in Redis.
            value (str): The value to set for the given key.
            expire (int, optional): The expiration time for the key in seconds. Defaults to None.
        """
        self.client.set(key, value, ex=expire)

    def get(self, key: str):
        """
        Get the value of a key from Redis.
        
        Args:
            key (str): The key to retrieve from Redis.
        
        Returns:
            str: The value of the given key, or None if the key does not exist.
        """
        return self.client.get(key)

    def delete(self, key: str):
        """
        Delete a key from Redis.
        
        Args:
            key (str): The key to delete from Redis.
        """
        self.client.delete(key)


def get_redis_service() -> RedisService:
    """
    This function creates and returns a RedisService instance, which can be used by other parts of the application.
    
    Returns:
        RedisService: An instance of RedisService.
    """
    return RedisService()
