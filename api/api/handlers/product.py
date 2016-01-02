import logging
import json
from functools import partial

from bson.json_util import dumps
from bson.objectid import ObjectId
from bson.errors import InvalidId

from mongoengine.queryset import DoesNotExist
from jsonschema.exceptions import ValidationError

from pyramid.view import view_config

from api.models.category import Category
from api.models.hardware import Hardware
from jsonschema import validate

log = logging.getLogger(__name__)

products_view = partial(
    view_config,
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
        new_field = field.replace(".", "")
        print new_field
        print new_field.encode('utf8')
        setattr(product, new_field, data[field])
    request.context.products.append(product)
    request.context.products.save()
    return {"message": "product saved"}
