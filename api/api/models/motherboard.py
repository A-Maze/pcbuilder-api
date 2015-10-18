from mongoengine import StringField
from api.models.hardware import Hardware


class Motherboard(Hardware):
    serie = StringField(max_length=200)
    product = StringField(max_length=200)
    socket = StringField(max_length=200)
    number_of_sockets = StringField(max_length=200)
    form_factor = StringField(max_length=200)
    bios_or_uefi = StringField(max_length=200)
    dual_or_single_bios_uefi = StringField(max_length=200)
    motherboard_chipset = StringField(max_length=200)
    memory_type = StringField(max_length=200)
    maximum_memory_size = StringField(max_length=200)
    hard_drive_bus = StringField(max_length=200)
    raid_modi = StringField(max_length=200)
    card_interface = StringField(max_length=200)
    number_of_pcie = StringField(max_length=200)
    link_interface = StringField(max_length=200)
    ethernet_connection = StringField(max_length=200)
    network_chip = StringField(max_length=200)
    bluetooth_available = StringField(max_length=200)
    usb_connection = StringField(max_length=200)
    video_out = StringField(max_length=200)
    connection = StringField(max_length=200)
    audio_channels = StringField(max_length=200)
    audio_outputs = StringField(max_length=200)
    audio_chips = StringField(max_length=200)
