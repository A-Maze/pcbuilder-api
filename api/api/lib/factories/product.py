import logging
from api.models.category import get_all_categories
from api.lib.factories import BaseFactory

log = logging.getLogger(__name__)


class ProductFactory(BaseFactory):
    def __init__(self, *args, **kwargs):
        super(ProductFactory, self).__init__(*args, **kwargs)
        self['filters'] = FilterFactory(self, 'filter')

    def list_products(self):
        products = []
        for category in get_all_categories():
            products += category.products

class FilterFactory(BaseFactory):
    def __init__(self, *args, **kwargs):
        super(FilterFactory, self).__init__(*args, **kwargs)
