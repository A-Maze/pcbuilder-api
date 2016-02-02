from paste.deploy.loadwsgi import appconfig
import os
import logging
from api.models.hardware import Hardware
from api.models.category import Category
from api.models.record import Record
import requests
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
here = os.path.dirname(__file__)
settings = appconfig('config:' + os.path.join(here, '../../', 'test.ini'))
log = logging.getLogger(__name__)


class TestApi(object):
    def __init__(self):
        self.base_url = 'http://{}:{}/'.format(
            settings['mongodb.host'], '6543')

    def test_category_name(self):
        response = requests.get('{}{}'.format(self.base_url,
                                'category/optical_drive')).json()
        assert_equal(response['name'], 'optical_drive')
        assert_not_equal(response['name'], 'cpu')

    def test_category_products(self):
        response = requests.get('{}{}'.format(self.base_url,
                                'category/optical_drive')).json()
        assert_equal(isinstance(response['products'], list), True)
        assert_not_equal(isinstance(response['products'], int), True)

    def test_product_call(self):
        response = requests.get('{}{}'.format(self.base_url,
                                'category/optical_drive/product/a')).json()
        assert_equal(response['message'], 'product not found')

    def test_filter_call(self):
        response = requests.get('{}{}'.format(self.base_url,
                                '/product/filters')).json()
        assert_not_equal(len(response), 0)

    def test_all_products_call(self):
        response = requests.get('{}{}'.format(self.base_url,
                                '/product')).json()
        assert_equal(isinstance(response, list), True)
        assert_not_equal(isinstance(response, int), True)

    def test_hardware_model(self):

        def create_hardware():
            hardware = Hardware()
            hardware.name = 1
        assert_raises(TypeError, create_hardware())

    def test_record_model(self):

        def create_record():
            record = Record()
            record.price = "12"
        assert_raises(TypeError, create_record())

    def test_category_model(self):

        def create_category():
            category = Category()
            category.name = 12
        assert_raises(TypeError, create_category())
