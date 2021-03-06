import datetime
from bson.objectid import ObjectId
from pyramid.config import Configurator
from pyramid.renderers import JSON

from api.models.meta import RedisSession
from api.models.record import Record
from api.models.hardware import Hardware
from api.lib.factories.root import RootFactory
from api.lib.renderer import (object_id_adapter, datetime_adapter,
                              set_adapter, mongo_adapter)
from mongoengine import connect


def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    config = Configurator(settings=settings, root_factory=RootFactory)
    # MongoDB
    db_name = settings['mongodb.db_name']
    db_host = settings['mongodb.host']
    db_port = int(settings['mongodb.port'])
    db_user = settings['mongodb.user']
    db_password = settings['mongodb.password']
    if db_user == '':
        db_user = None
        db_password = None
    connect(db_name, username=db_user, password=db_password, host=db_host,
            port=db_port)
    RedisSession(settings['redis.host'], settings['redis.port'],
                 settings['redis.db'])
    config.add_route('home', '/')
    config.scan('api.handlers')

    renderers = {'json': JSON()}
    for name, renderer in renderers.items():
        renderer.add_adapter(ObjectId, object_id_adapter)
        renderer.add_adapter(datetime.datetime, datetime_adapter)
        renderer.add_adapter(set, set_adapter)
        renderer.add_adapter(Record, mongo_adapter)
        renderer.add_adapter(Hardware, mongo_adapter)
        config.add_renderer(name, renderer)
    return config.make_wsgi_app()
