from frozentime.lib.factories import BaseFactory


class AdminFactory(BaseFactory):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
