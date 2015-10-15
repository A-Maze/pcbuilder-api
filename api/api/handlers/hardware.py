from pyramid.view import view_config
from api.lib.factories.hardware import HardwareFactory
from functools import partial

hardware_factory_view = partial(
    view_config,
    context=HardwareFactory,
    permission='public')   # This can probably remain public


@hardware_factory_view(request_method="GET", renderer='json')
def default_hardware_view(request):
    """ Returns all hardware models """
    return {"message": "Good job you've made a GET request for the hardware"}
