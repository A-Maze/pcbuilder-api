from pyramid.config import Configurator

from api.lib.factories.root import RootFactory


def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    config = Configurator(settings=settings, root_factory=RootFactory)
    config.include("pyramid_mongoengine")
    config.add_connection_database()
    config.add_route('home', '/')
    config.scan('api.handlers')
    return config.make_wsgi_app()
