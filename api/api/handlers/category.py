import logging
import json
from bson.json_util import dumps
from pyramid.view import view_config
from api.lib.factories.category import CategoryFactory
from api.models.category import Category, get_categories_info
from functools import partial

log = logging.getLogger(__name__)

category_factory_view = partial(
    view_config,
    context=CategoryFactory,
    permission='public',
    renderer='json')   # This can probably remain public

category_view = partial(
    view_config,
    context=Category,
    permission='public',
    renderer='json')


@category_factory_view(request_method="GET")
def default_category_view(request):
    """ Returns all categories """
    categories = get_categories_info()
    categories_dict = [obj.get_fields(('name', 'locale')) for
                       obj in categories]
    return {"categories": categories_dict}


@category_view(request_method="GET")
def get_category(request):
    """ Returns a category based on it's id """
    category = request.context
    category_json = json.loads(dumps(category.to_mongo()))
    return category_json
