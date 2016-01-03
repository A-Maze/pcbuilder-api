from pyramid.config import Configurator

from api.lib.factories.root import RootFactory
from mongoengine import connect
import sys


def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    config = Configurator(settings=settings, root_factory=RootFactory)
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')
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
    config.add_route('home', '/')
    config.scan('api.handlers')
    return config.make_wsgi_app()
