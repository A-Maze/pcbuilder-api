from meta import db
from models.hardware import Hardware


class Motherboard(Hardware):
    serie = db.StringField(max_length=200)
    product = db.StringField(max_length=200)
    socket = db.StringField(max_length=200)
    number_of_sockets = db.StringField(max_length=200)
    form_factor = db.StringField(max_length=200)
    bios_or_uefi = db.StringField(max_length=200)
    dual_or_single_bios_uefi = db.StringField(max_length=200)
    motherboard_chipset = db.StringField(max_length=200)
    memory_type = db.StringField(max_length=200)
    maximum_memory_size = db.StringField(max_length=200)
    hard_drive_bus = db.StringField(max_length=200)
    raid_modi = db.StringField(max_length=200)
    card_interface = db.StringField(max_length=200)
    number_of_pcie = db.StringField(max_length=200)
    link_interface = db.StringField(max_length=200)
    ethernet_connection = db.StringField(max_length=200)
    network_chip = db.StringField(max_length=200)
    bluetooth_available = db.StringField(max_length=200)
    usb_connection = db.StringField(max_length=200)
    video_out = db.StringField(max_length=200)
    connection = db.StringField(max_length=200)
    audio_channels = db.StringField(max_length=200)
    audio_outputs = db.StringField(max_length=200)
    audio_chips = db.StringField(max_length=200)
