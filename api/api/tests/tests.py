from paste.deploy.loadwsgi import appconfig
import os
import urllib
import logging
here = os.path.dirname(__file__)
settings = appconfig('config:' + os.path.join(here, '../../', 'test.ini'))
log = logging.getLogger(__name__)


class TestA(object):
    def __init__(self):
        self.base_url = 'http://{}:{}/category/'.format(
            settings['mongodb.host'], settings['mongodb.port'])

    def test_init(self):
        response = urllib.request(self.base_url).read()
