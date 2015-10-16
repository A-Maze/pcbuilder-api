from pyramid.view import view_config
from api.lib.factories.admin import AdminFactory
from functools import partial

admin_factory_view = partial(
    view_config,
    context=AdminFactory,
    permission='public')   # This needs to be changed to the proper permission


@admin_factory_view(request_method="GET", renderer='json')
def default_admin_view(request):
    """ Default admin GET request """
    return {"Message": "Good job you've made an admin GET request"}
