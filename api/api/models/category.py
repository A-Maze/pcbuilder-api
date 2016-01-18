import logging
import json
from mongoengine import (Document,
                         StringField, EmbeddedDocumentListField)
from mongoengine.queryset import DoesNotExist
from api.models.hardware import Hardware  # noqa
from api.models.meta import redis_session as redis

log = logging.getLogger(__name__)


class Category(Document):
    name = StringField(max_length=120)
    products = EmbeddedDocumentListField('Hardware')
    product_schema = StringField()

    def get_product(self, key):
        for product in self.products:
            if (str(product._id) == key or
               product.ean == key or
               product.sku == key):
                    return product
            raise DoesNotExist


def get_all_categories():
    categories = json.loads(redis.get('categories').decode('utf-8'))
    if not categories:
        categories = Category.objects.all().to_json()
        redis.set('categories', categories)
    return categories


def get_category_by_name(name):
    return Category.objects(name=name).first()
