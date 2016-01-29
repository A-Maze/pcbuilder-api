from paste.deploy.loadwsgi import appconfig
import os
import urllib2
import logging
import json
from nose.tools import assert_equal
from nose.tools import assert_not_equal
here = os.path.dirname(__file__)
settings = appconfig('config:' + os.path.join(here, '../../', 'test.ini'))
log = logging.getLogger(__name__)


class TestApi(object):
    def __init__(self):
        self.base_url = 'http://{}:{}/category/'.format(
            settings['mongodb.host'], '6543')

    def test_category_name(self):
        response = urllib2.urlopen('{}{}'.format(self.base_url,
                                   'optical_drive')).read()
        response_ = json.loads(response)
        assert_equal(response_['name'], 'optical_drive')
        assert_not_equal(response_['name'], 'cpu')

    def test_category_products(self):
        response = urllib2.urlopen('{}{}'.format(self.base_url,
                                   'optical_drive')).read()
        response_ = json.loads(response)
        assert_equal(isinstance(response_['products'], list), True)
        assert_not_equal(isinstance(response_['products'], int), True)

    def test_product_call(self):
        response = urllib2.urlopen('{}{}'.format(self.base_url,
                                   'optical_drive/product/a')).read()
        response_ = json.loads(response)
        assert_equal(response_['message'], 'product not found')

    def test_product_post(self):
        product = {}
        product['name'] = 'test_product'
        url = '{}{}'.format(self.base_url, 'optical_drive/product/')
        response = urllib2.Request(url, product)
        response.add_header('Content-Type', 'application/json')
        resp = urllib2.urlopen(response)
        assert_equal(resp['message'], 'product saved')
