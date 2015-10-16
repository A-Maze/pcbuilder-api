from api.lib.factories import BaseFactory


class HardwareFactory(BaseFactory):
    def __getitem__(self, key):
        raise KeyError
