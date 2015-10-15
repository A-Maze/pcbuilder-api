from api.lib.factories.admin import AdminFactory
from api.lib.factories.albums import HardwareFactory


class RootFactory(dict):
    def __init__(self, request):
        self.requires_oauth = False
        self.request = request
        self.__name__ = None
        self.__parent__ = None

        self['hardware'] = HardwareFactory(self, 'hardware')
        self['admin'] = AdminFactory(self, 'admin')
