from meta import db
from models.hardware import Hardware


class HardDrive(Hardware):
    serie = db.StringField(max_length=200)
    product = db.StringField(max_length=200)
    storage = db.StringField(max_length=200)
    hard_drive_bus = db.StringField(max_length=200)
    case_bay_intern = db.StringField(max_length=200)
    height = db.StringField(max_length=200)
    rotation_speed = db.StringField(max_length=200)
    drive_cache = db.StringField(max_length=200)
    command_queuing = db.StringField(max_length=200)
    power_reading = db.StringField(max_length=200)
    power_writing = db.StringField(max_length=200)
    prive_per_gb = db.StringField(max_length=200)
    warranty = db.StringField(max_length=200)
    ssd_type = db.StringField(max_length=200)
    ssd_controller = db.StringField(max_length=200)
    ssd_properties = db.StringField(max_length=200)
    hard_drive_bus_intern = db.StringField(max_length=200)
    hdd_ssd_connection = db.StringField(max_length=200)
    sequential_read = db.StringField(max_length=200)
    sequential_write = db.StringField(max_length=200)
    read_random_4k = db.StringField(max_length=200)
    write_random_4k = db.StringField(max_length=200)
