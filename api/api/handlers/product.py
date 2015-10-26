import logging
import json
from bson.json_util import dumps
from pyramid.view import view_config
from api.models.category import Category
from functools import partial

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
