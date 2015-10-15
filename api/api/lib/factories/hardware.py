from frozentime.lib.factories import BaseFactory


class HardwareFactory(BaseFactory):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
