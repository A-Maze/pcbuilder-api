import logging
import json
from bson.json_util import dumps
from pyramid.view import view_config
from functools import partial

log = logging.getLogger(__name__)

product_view = partial(
    view_config,
    permission='public',
    renderer='json')


@product_view(request_method="GET")
def return_product(request):
    products = request.context
    products_dict = [json.loads(dumps(obj.to_mongo())) for obj in products]
    return {"products": products_dict}
