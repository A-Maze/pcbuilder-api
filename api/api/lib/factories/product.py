import logging
from api.models.category import get_all_categories
from api.lib.factories import BaseFactory

log = logging.getLogger(__name__)


class ProductFactory(BaseFactory):
    def __init__(self, *args, **kwargs):
        super(ProductFactory, self).__init__(*args, **kwargs)
        self['filters'] = FilterFactory(self, 'filter')

    def list_products(self):
        product_lists = [category.products for category in
                         get_all_categories()]
        return [product.to_mongo() for product_list in product_lists for
                product in product_list]


class FilterFactory(BaseFactory):
    def __init__(self, *args, **kwargs):
        super(FilterFactory, self).__init__(*args, **kwargs)
