from mongoengine import StringField
from models.hardware import Hardware


class Harddrive(Hardware):
    serie = StringField(max_length=200)
    product = StringField(max_length=200)
    storage = StringField(max_length=200)
    harddrive_bus = StringField(max_length=200)
    case_bay_intern = StringField(max_length=200)
    height = StringField(max_length=200)
    rotation_speed = StringField(max_length=200)
    drive_cache = StringField(max_length=200)
    command_queuing = StringField(max_length=200)
    power_reading = StringField(max_length=200)
    power_writing = StringField(max_length=200)
    prive_per_gb = StringField(max_length=200)
    Fabrieksgarantie = StringField(max_length=200)
    SSD_type = StringField(max_length=200)
    SSD_controller = StringField(max_length=200)
    SSD_eigenschappen = StringField(max_length=200)
    Hardeschijf_bus_intern = StringField(max_length=200)
    HDD_SSD_aansluiting = StringField(max_length=200)
    Lezen_sequentieel = StringField(max_length=200)
    Schrijven_sequentieel = StringField(max_length=200)
    Lezen_random_4K = StringField(max_length=200)
    Schrijven_random_4K = StringField(max_length=200)
    Verkoopstatus = StringField(max_length=200)
