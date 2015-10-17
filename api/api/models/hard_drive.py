from meta import db
from models.hardware import Hardware


class Harddrive(Hardware):
    serie = db.StringField(max_length=200)
    product = db.StringField(max_length=200)
    storage = db.StringField(max_length=200)
    harddrive_bus = db.StringField(max_length=200)
    case_bay_intern = db.StringField(max_length=200)
    height = db.StringField(max_length=200)
    rotation_speed = db.StringField(max_length=200)
    drive_cache = db.StringField(max_length=200)
    command_queuing = db.StringField(max_length=200)
    power_reading = db.StringField(max_length=200)
    power_writing = db.StringField(max_length=200)
    prive_per_gb = db.StringField(max_length=200)
    Fabrieksgarantie = db.StringField(max_length=200)
    SSD_type = db.StringField(max_length=200)
    SSD_controller = db.StringField(max_length=200)
    SSD_eigenschappen = db.StringField(max_length=200)
    Hardeschijf_bus_intern = db.StringField(max_length=200)
    HDD_SSD_aansluiting = db.StringField(max_length=200)
    Lezen_sequentieel = db.StringField(max_length=200)
    Schrijven_sequentieel = db.StringField(max_length=200)
    Lezen_random_4K = db.StringField(max_length=200)
    Schrijven_random_4K = db.StringField(max_length=200)
    Verkoopstatus = db.StringField(max_length=200)
