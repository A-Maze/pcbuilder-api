import logging
from pyramid.view import view_config
from api.lib.factories.hardware import HardwareFactory
from api.lib.encode import JSONEncoder
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
    hardware = get_all_hardware()
    hardware_dict = [obj.to_mongo() for obj in hardware]
    return {"hardware": hardware_dict}
