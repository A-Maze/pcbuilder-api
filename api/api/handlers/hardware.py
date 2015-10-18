import logging
import json
from bson.json_util import dumps
from pyramid.view import view_config
from api.lib.factories.hardware import HardwareFactory
# from api.lib.encode import JSONEncoder

from api.models.hardware import get_all_hardware, get_hardware
from functools import partial
from api.lib.response import not_found, bad_request
from api.lib.validation import MotherboardSchema, populate
from api.models.motherboard import Motherboard
from api.models.record import Record
log = logging.getLogger(__name__)

hardware_factory_view = partial(
    view_config,
    context=HardwareFactory,
    permission='public')   # This can probably remain public


@hardware_factory_view(request_method="GET", renderer='json')
def default_hardware_view(request):
    """ Returns all hardware models """
    hardware = get_all_hardware()
    hardware_dict = [json.loads(dumps(obj.to_mongo())) for obj in hardware]
    return {"hardware": hardware_dict}


@hardware_factory_view(request_method='POST', renderer='json')
def add_hardware(request):
    """ Add new hardware to the database """
    data = request.json_body
    hardware_id = None
    if 'hardware_id' in data:
        hardware_id = data['hardware_id'] or None

    category = data['category'] or None
    if not category:
        return not_found(message="Category {} not found".format(category))

    # check if its an update
    if hardware_id:
        hardware = get_hardware(id_=hardware_id, category=category)
        if not hardware:
            return not_found(message="Hardware {} not found"
                             .format(hardware_id))
    else:
        hardware = Motherboard()

    # --- dont know if necessary
    result, errors = MotherboardSchema().load(data)
    if errors:
        return bad_request(message="Validation failed", errors=errors)
    # -------------------------
    populate(hardware, result)

    if 'record' in result:
        record = Record()
        populate(record, result['record'])
        hardware.records = record
    log.info(result)
    # doesnt work with records yet:D
    hardware.save()
    return {
        "message": "succes"
    }
