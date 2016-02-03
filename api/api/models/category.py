import logging
import json
from mongoengine import (Document, DictField,
                         StringField, EmbeddedDocumentListField)
from mongoengine.queryset import DoesNotExist
from api.models.hardware import Hardware  # noqa
from api.models.meta import RedisSession

log = logging.getLogger(__name__)


class Category(Document):
    name = StringField(max_length=120)
    products = EmbeddedDocumentListField('Hardware')
    product_schema = StringField()
    locale = DictField()

    def get_product(self, key):
        try:
            for product in self.products:
                if str(product['_id']['$oid']) == key:
                    return product
                elif product.get('ean', None) and (key in product['ean']):
                    return product
                elif product.get('sku', None) and (key in product['sku']):
                    return product
        except (AttributeError, TypeError):
            # value is not yet cached and has to be handled differently
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

    def get_fields(self, fields=('name',)):
        return dict((k, getattr(self, k, None)) for k in fields)

    def invalidate(self):
        return RedisSession().session.delete('category_{}'.format(self.name))


def get_all_categories(searchterm='', for_sale=None, limit=None, offset=0):
    """Returns all categories in a list

    Optionally filters the products of these categories
    based on a searchterm and if the product is for sale.
    """

    categories = RedisSession().session.get('categories')

    # Defining the range of products to be fetched
    start = int(offset)
    end = int(limit) + start if limit else limit

    # if categores could not be retrieved from cache fetch it from the DB and
    # write it to cache. Otherwise let the values retrieved from the cache
    # represent itself as Category objects
    if not categories:
        categories = Category.objects.all()
        RedisSession().session.set('categories', categories.to_json())
    else:
        json_categories = json.loads(categories.decode('utf-8'))
        categories = []
        for json_category in json_categories:
            category = Category()
            json_category['products'] = json_category['products'][start:end]
            category.set_fields(json_category)
            categories.append(category)

    if any((searchterm, for_sale)):
        for category in categories:
                category.products = filter_category_products(
                    category.products[start:end],
                    searchterm, for_sale)
    else:
        for category in categories:
            category.products = category.products[start:end]
    return categories


def get_category_by_name(name, limit=None, offset=0, **kwargs):
    """Returns a category by name

    Optionally the products of this category by the filters specified in
    **kwargs.
    """

    category = RedisSession().session.get('category_{}'.format(name))

    # Defining the range of products to be fetched
    start = int(offset)
    end = int(limit) + start if limit else limit

    # If the category could not be received by name from the cache fetch it
    # from the DB instead and write it to the cache. Otherwise let the value
    # retrieved from the caches represent itself as a Category object
    if not category:
        category = Category.objects(name=name).first()
        RedisSession().session.set('category_{}'.format(name),
                                   category.to_json())
    else:
        json_category = json.loads(category.decode('utf-8'))
        json_category['products'] = json_category['products'][start:end]
        category = Category()
        category.set_fields(json_category)

    # return only the range that was requested
    category.products = filter_category_products(
        category.products[start:end], **kwargs)

    return category


def filter_category_products(products, searchterm='', for_sale=None, **kwargs):
    """Filters a list of products based on the given arguments"""

    searchterm = searchterm.lower()
    filtered_products = []
    for product in products:
        if searchterm not in product['name'].lower():
            continue
        if for_sale and not product['records']:
            continue
        filtered_products.append(product)
    return filtered_products


def get_categories_info():
    """Returns only basic info about the category excluding products"""

    categories_info = RedisSession().session.get('categories_info')

    if not categories_info:
        categories_info = Category.objects().only('name', 'locale')
        RedisSession().session.set('category_info', categories_info.to_json())
    return categories_info
