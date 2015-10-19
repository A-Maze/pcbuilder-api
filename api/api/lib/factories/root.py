from api.lib.factories.admin import AdminFactory
from api.lib.factories.category import CategoryFactory


class RootFactory(dict):
    def __init__(self, request):
        self.requires_oauth = False
        self.request = request
        self.__name__ = None
        self.__parent__ = None

        self['category'] = CategoryFactory(self, 'category')
        self['admin'] = AdminFactory(self, 'admin')
