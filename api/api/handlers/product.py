import logging
import json
from functools import partial

from bson.json_util import dumps
from bson.objectid import ObjectId
from bson.errors import InvalidId

from mongoengine.queryset import DoesNotExist

from pyramid.view import view_config

from api.models.category import Category
from api.models.hardware import Hardware


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
    name='product'
    )


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
        product_id = request.subpath[0]
    except IndexError:
        return {"message": "Please specify a product id"}

    try:
        product = request.context.get_product(product_id)
    except InvalidId:
        return {"message": "Invalid id given"}
    except DoesNotExist:
        return {"message": "product not found"}

    product_json = json.loads(dumps(product.to_mongo()))
    return {'product': product_json}


@product_view(request_method="POST")
def save_product(request):
    """ handles both update and create requests """
    data = json.dumps(request.json_body)
    if request.subpath:
        try:
            product = request.context.get_product(request.subpath[0])
        except:
            return{"message": "product not found"}
    else:
        product = Hardware()
        product.category = request.context
        product._id = ObjectId()
    product.from_json(data)
    request.context.products.append(product)
    request.context.save()
    return {"message": "product saved"}
