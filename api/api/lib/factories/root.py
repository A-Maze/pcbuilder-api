from api.lib.factories.admin import AdminFactory
from api.lib.factories.category import CategoryFactory
from api.lib.factories.product import ProductFactory


class RootFactory(dict):
    def __init__(self, request):
        self.requires_oauth = False
        self.request = request
        self.__name__ = None
        self.__parent__ = None

        self['admin'] = AdminFactory(self, 'admin')
        self['category'] = CategoryFactory(self, 'category')
        self['product'] = ProductFactory(self, 'product')
