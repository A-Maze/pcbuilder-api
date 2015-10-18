import json
import logging

from marshmallow import Schema, fields
from marshmallow.fields import String, Integer, Float

log = logging.getLogger(__name__)


class RecordSchema(Schema):
    price = Float(required=False)
    product = Integer(required=False)
    webshop = String(required=False)


class MotherboardSchema(Schema):
    category = String(required=False)
    name = String(required=False)
    subname = String(required=False)
    info = String(required=False)
    stock = String(required=False)
    image = String(required=False)
    ean = String(required=False)
    sku = String(required=False)
    SKU = String(required=False)
    link = String(required=False)
    brand = String(required=False)
    execution = String(required=False)
    serie = String(required=False)
    product = String(required=False)
    socket = String(required=False)
    number_of_sockets = String(required=False)
    form_factor = String(required=False)
    bios_or_uefi = String(required=False)
    dual_or_single_bios_uefi = String(required=False)
    motherboard_chipset = String(required=False)
    memory_type = String(required=False)
    maximum_memory_size = String(required=False)
    hard_drive_bus = String(required=False)
    raid_modi = String(required=False)
    card_interface = String(required=False)
    number_of_pcie = String(required=False)
    link_interface = String(required=False)
    ethernet_connection = String(required=False)
    network_chip = String(required=False)
    bluetooth_available = String(required=False)
    usb_connection = String(required=False)
    video_out = String(required=False)
    connection = String(required=False)
    audio_channels = String(required=False)
    audio_outputs = String(required=False)
    audio_chips = String(required=False)
    record = fields.Nested(RecordSchema, required=False)


# ----------
# FUNCTIONS
# ----------
def validate_json(dict_):
    log.info("-" * 80)
    log.info(dict_)
    log.info("-" * 80)
    try:
        json.loads(json.dumps(dict_))
        return True
    except ValueError:
        return False


def populate(obj, result):
    for key in result:
        try:
            if result[key] == 0:
                setattr(obj, key, 0)
            else:
                setattr(obj, key, result[key] or None)
        except:
            pass
    return obj
