import redis

redis_session = redis.StrictRedis(host='localhost', port=6379, db=0)
