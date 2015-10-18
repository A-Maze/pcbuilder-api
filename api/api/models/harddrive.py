from mongoengine import StringField, IntField
from models.hardware import Hardware


class HardDrive(Hardware):
    hardware_id = IntField()
    serie = StringField(max_length=200)
    product = StringField(max_length=200)
    storage = StringField(max_length=200)
    hard_drive_bus = StringField(max_length=200)
    case_bay_intern = StringField(max_length=200)
    height = StringField(max_length=200)
    rotation_speed = StringField(max_length=200)
    drive_cache = StringField(max_length=200)
    command_queuing = StringField(max_length=200)
    power_reading = StringField(max_length=200)
    power_writing = StringField(max_length=200)
    prive_per_gb = StringField(max_length=200)
    warranty = StringField(max_length=200)
    ssd_type = StringField(max_length=200)
    ssd_controller = StringField(max_length=200)
    ssd_properties = StringField(max_length=200)
    hard_drive_bus_intern = StringField(max_length=200)
    hdd_ssd_connection = StringField(max_length=200)
    sequential_read = StringField(max_length=200)
    sequential_write = StringField(max_length=200)
    read_random_4k = StringField(max_length=200)
    write_random_4k = StringField(max_length=200)
