from api.lib.factories import BaseFactory


class AdminFactory(BaseFactory):
    def __getitem__(self, key):
            raise KeyError
