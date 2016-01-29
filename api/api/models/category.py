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
            if str(product['_id']['$oid']) == key:
                return product
            elif product.get('ean', None) and (key in product['ean']):
                return product
            elif product.get('sku', None) and (key in product['sku']):
                return product
        raise DoesNotExist

    def set_fields(self, values):
        for key, value in values.items():
            setattr(self, key, value)


def get_all_categories(searchterm='', for_sale=None):
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

    if any((searchterm, for_sale)):
        searchterm.lower()

        for category in categories:
                filtered_products = []
                for product in category.products:
                    if searchterm not in product['name'].lower():
                        continue
                    if for_sale and not product['records']:
                        continue
                    filtered_products.append(product)
                category.products = filtered_products
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
