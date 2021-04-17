import json
import os
import redis

# Read the Redis credentials from the REDIS_URL environment variable.
REDIS_URL = os.environ.get('REDIS_URL')
REDIS_PORT = os.environ.get('REDIS_PORT')

# Initialize the cache
pool = redis.ConnectionPool(host=REDIS_URL, port=REDIS_PORT, decode_responses=True)
r = redis.Redis(connection_pool=pool)

def set(key, value):
    r.set(key, value)