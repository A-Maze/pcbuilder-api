from meta import db
from models.hardware import Hardware


class Harddrive(Hardware):
    Serie = db.StringField(max_length=200)
    Product = db.StringField(max_length=200)
    Opslagcapaciteit = db.StringField(max_length=200)
    Hardeschijf_bus = db.StringField(max_length=200)
    Behuizing_bay_intern = db.StringField(max_length=200)
    Hoogte = db.StringField(max_length=200)
    Rotatiesnelheid = db.StringField(max_length=200)
    Drive_cache = db.StringField(max_length=200)
    Command_Queuing = db.StringField(max_length=200)
    Stroomverbruik_lezen = db.StringField(max_length=200)
    Stroomverbruik_schrijven = db.StringField(max_length=200)
    Prijs_per_GB = db.StringField(max_length=200)
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
