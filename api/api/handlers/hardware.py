import logging
from pyramid.view import view_config
from api.lib.factories.hardware import HardwareFactory
from api.models.hardware import Hardware, get_all_hardware
from functools import partial

log = logging.getLogger(__name__)

hardware_factory_view = partial(
    view_config,
    context=HardwareFactory,
    permission='public')   # This can probably remain public


@hardware_factory_view(request_method="GET", renderer='json')
def default_hardware_view(request):
    """ Returns all hardware models """
    hardware_dict = {}
    hardware = get_all_hardware()
    for category in hardware:
        hardware_dict[str(category.id)] = category.to_mongo()
    return {"hardware": hardware_dict}
