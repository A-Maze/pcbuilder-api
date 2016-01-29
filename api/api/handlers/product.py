import logging
import json

from jsonschema import validate
from functools import partial
from bson.json_util import dumps
from bson.objectid import ObjectId
from bson.errors import InvalidId

from mongoengine.queryset import DoesNotExist
from jsonschema.exceptions import ValidationError

from pyramid.view import view_config
from api.models.category import Category
from api.models.record import Record
from api.lib.factories.product import ProductFactory, FilterFactory
from api.lib.factories.category import CategoryFactory
from api.models.category import get_all_categories
from api.models.hardware import Hardware

log = logging.getLogger(__name__)

record_view = partial(
    view_config,
    permission='public',
    renderer='json',
    context=Category,
    name='record')

product_factory_view = partial(
    view_config,
    context=ProductFactory,
    permission='public',
    renderer='json')

filter_factory_view = partial(
    view_config,
    context=FilterFactory,
    permission='public',
    renderer='json')

products_view = partial(
    view_config,
    containment=CategoryFactory,
    permission='public',
    renderer='json')

product_view = partial(
    view_config,
    permission='public',
    renderer='json',
    context=Category,
    name='product')


@products_view(request_method="GET")
def return_products(request):
    """ returns all products in a category """
    products = request.context
    products_dict = [json.loads(dumps(obj.to_mongo())) for obj in products]
    return {"products": products_dict}


@product_view(request_method="GET")
def return_product(request):
    """ returns a specific product in a category based on the id """
    try:
        key = request.subpath[0]
    except IndexError:
        return {"message": "Please specify a product id"}

    try:
        product = request.context.get_product(key)
    except InvalidId:
        return {"message": "Invalid id given"}
    except DoesNotExist:
        return {"message": "product not found"}

    product_json = json.loads(dumps(product.to_mongo()))
    return {'product': product_json}


@product_view(request_method="POST")
def save_product(request):
    """ handles both update and create requests """
    data = request.json_body
    try:
        validate(data, json.loads(request.context.product_schema))
    except ValidationError:
        return {"message": "invalid data"}
    if request.subpath:
        try:
            product = request.context.get_product(request.subpath[0])
        except DoesNotExist:
            return {"message": "product not found"}
    else:
        product = Hardware()
        product._id = ObjectId()
        product.category = request.context.name

    for field in data:
        # there can not be a . in a field name so we remove that.
        new_field = field.replace(".", "")
        setattr(product, new_field, data[field])

    request.context.products.append(product)
    request.context.products.save()
    return {"message": "product saved"}


@record_view(request_method="POST")
def save_records(request):
    """ handles the records requests """
    data = request.json_body
    for item in data['items']:
        item_ = json.loads(item)
        ean_numbers = item_['ean'].split()
        products = request.context
        product = None
        for number in ean_numbers:
            try:
                if number is not None:
                    product = products.get_product(key=str(number))
                    continue
            except DoesNotExist:
                log.critical('product not found')

        if not product:
            try:
                if item_['sku']:
                    product = products.get_product(key=str(item_['sku']))
            except DoesNotExist:
                return {"message": "product not found"}
        else:
            record = Record(price=item_['price'].replace(',', '.'),
                            webshop=item_['webshop'])

            product.records.append(record)
    request.context.save()

    return {
        "message": "records saved"
    }


@product_factory_view(request_method="GET")
def list_products(request):
    return _get_products_list()


def _get_products_list():
    products_list = []
    for category in get_all_categories():
        products_list.append({
            'products': category['products'],
            'product_schema': category['product_schema'],
            'category_name': category['name']
        })

    return products_list


@filter_factory_view(request_method="GET")
def list_filters(request):
    return _process_product_filters(_get_products_list())


def _process_product_filters(products_list):
    filter_list = []
    for products_dict in products_list:
        # List the column that this category can be filtered on
        category_filters = {"filters": {},
                            "category": products_dict['category_name']}

        filter_fields = json.loads(products_dict['product_schema'])['required']
        filter_fields.remove("name")  # We don't need to name in filters

        for product in products_dict['products']:
            # Check the possible filter values per product
            for key in filter_fields:
                try:
                    category_filters["filters"].setdefault(
                        key, set()).add(product[key])
                except KeyError:
                    log.info("key {} not found for category {}".format(
                        key, products_dict['category_name']
                    ))

        filter_list.append(category_filters)

    return filter_list
