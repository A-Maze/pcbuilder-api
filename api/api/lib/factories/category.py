import logging
from api.lib.factories import BaseFactory
from api.models.category import get_category_by_id

log = logging.getLogger(__name__)


class CategoryFactory(BaseFactory):
    def __init__(self, *args, **kwargs):
        super(CategoryFactory, self).__init__(*args, **kwargs)

    def __getitem__(self, key):
        try:
            return get_category_by_id(key)
        except:
            raise KeyError
