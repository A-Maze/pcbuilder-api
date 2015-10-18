import logging
from bson.json_util import dumps
from pyramid.view import view_config
from api.lib.factories.hardware import HardwareFactory
# from api.lib.encode import JSONEncoder
from api.models.hardware import Hardware, get_all_hardware, get_hardware
from functools import partial
from auping_api.lib.response import not_found


log = logging.getLogger(__name__)

hardware_factory_view = partial(
    view_config,
    context=HardwareFactory,
    permission='public')   # This can probably remain public


@hardware_factory_view(request_method="GET", renderer='json')
def default_hardware_view(request):
    """ Returns all hardware models """
    hardware = get_all_hardware()
    hardware_dict = [dumps(obj.to_mongo()) for obj in hardware]
    return {"hardware": hardware_dict}


@hardware_factory_view(request_method='POST', rendered='json')
def add_hardware(request):
    """ Add new hardware to the database """
    if 'hardware_id' in request.matchdict:
        hardware_id = request.matchdict['hardware_id'] or None

    category = request.matchdict['category'] or None
    if not category:
        return not_found(message="Category {} not found".format(category))

    # check if its an update
    if hardware_id:
        hardware = get_hardware(id_=hardware_id, category=category)
        if not hardware:
            return not_found(message="Hardware {} not found"
                             .format(hardware_id))
    else:
        hardware = Hardware()
