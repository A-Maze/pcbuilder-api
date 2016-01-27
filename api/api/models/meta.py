from api.lib.decorators import singleton
import redis


@singleton
class RedisSession(object):
    def __init__(self, host, port, db):
        self.session = redis.StrictRedis(host=host, port=port, db=db)
