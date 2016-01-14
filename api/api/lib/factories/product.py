import logging
from api.lib.factories import BaseFactory

log = logging.getLogger(__name__)


class ProductFactory(BaseFactory):
    def __init__(self, *args, **kwargs):
        super(ProductFactory, self).__init__(*args, **kwargs)
        self['filters'] = FilterFactory(self, 'filter')


class FilterFactory(BaseFactory):
    def __init__(self, *args, **kwargs):
        super(FilterFactory, self).__init__(*args, **kwargs)
