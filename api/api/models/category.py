import logging
import json
from mongoengine import (Document,
                         StringField, EmbeddedDocumentListField)
from mongoengine.queryset import DoesNotExist
from api.models.hardware import Hardware  # noqa
from api.models.meta import RedisSession

log = logging.getLogger(__name__)


class Category(Document):
    name = StringField(max_length=120)
    products = EmbeddedDocumentListField('Hardware')
    product_schema = StringField()

    def get_product(self, key):
        for product in self.products:
            if str(product._id) == key:
                return product
            elif product.ean and (key in product.ean):
                return product
            elif product.sku and (key in product.sku):
                return product
        raise DoesNotExist


def get_all_categories():
    categories = RedisSession().session.get('categories')
    if not categories:
        categories = Category.objects.all().to_json()
        RedisSession().session.set('categories', categories)
        categories = json.loads(categories)
    else:
        categories = json.loads(categories.decode('utf-8'))
    return categories


def get_category_by_name(name):
    category = RedisSession().session.get('category_{}'.format(name))
    if not category:
        category = Category.objects(name=name).first().to_json()
        RedisSession().session.set('category_{}'.format(name), category)
    else:
        category = json.loads(category.decode('utf-8'))
    return category
