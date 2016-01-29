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

    def set_fields(self, values):
        for key, value in values.items():
            setattr(self, key, value)


def get_all_categories():
    categories = RedisSession().session.get('categories')
    if not categories:
        categories = Category.objects.all()
        RedisSession().session.set('categories', categories.to_json())
    else:
        json_categories = json.loads(categories.decode('utf-8'))
        categories = []
        for json_category in json_categories:
            category = Category()
            category.set_fields(json_category)
            categories.append(category)
    return categories


def get_category_by_name(name):
    category = RedisSession().session.get('category_{}'.format(name))
    if not category:
        category = Category.objects(name=name).first()
        RedisSession().session.set('category_{}'.format(name),
                                   category.to_json())
    else:
        json_category = json.loads(category.decode('utf-8'))
        category = Category()
        category.set_fields(json_category)
    return category
