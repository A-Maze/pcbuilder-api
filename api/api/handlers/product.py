import logging
import json
from functools import partial
from bson.json_util import dumps
from bson.objectid import ObjectId

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
    products = request.context
    products_dict = [json.loads(dumps(obj.to_mongo())) for obj in products]
    return {"products": products_dict}


@product_view(request_method="GET")
def return_product(request):
    product_id = request.subpath[0]
    product = request.context.get_product(product_id)
    product_json = json.loads(dumps(product.to_mongo()))
    return {'product': product_json}


@product_view(request_method="POST")
def save_product(request):
    data = json.dumps(request.json_body)
    if request.subpath:
        product = request.context.get_product(request.subpath[0])
    else:
        product = Hardware()  # this should select model based on category
        product.category = request.context
        product.id = ObjectId()
    product.from_json(data)
    product.save(force_insert=True)
    request.context.products.append(product)
    request.context.save()
    return {"message": "product saved"}
