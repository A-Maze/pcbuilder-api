from meta import db
from models.hardware import Hardware


class PowerSupply(Hardware):
    power_watt = db.StringField(max_length=200)
    product = db.StringField(max_length=200)
    _12v_rails = db.StringField(max_length=200)
    capacity_12v1_rail = db.StringField(max_length=200)
    power_certification = db.StringField(max_length=200)
    number_of_sata_connectors = db.StringField(max_length=200)
    number_molex_connectors = db.StringField(max_length=200)
    pci_express_connectors = db.StringField(max_length=200)
    number_6_pins_connections = db.StringField(max_length=200)
    number_6_2_pins_connections = db.StringField(max_length=200)
    modular = db.StringField(max_length=200)
    number_of_fans = db.StringField(max_length=200)
    diameter_fan = db.StringField(max_length=200)
    cooling_type = db.StringField(max_length=200)
    fan_location = db.StringField(max_length=200)
    Power_type = db.StringField(max_length=200)
    power_surge_protection = db.StringField(max_length=200)
    width = db.StringField(max_length=200)
    height = db.StringField(max_length=200)
    depth = db.StringField(max_length=200)
    warranty = db.StringField(max_length=200)
    particulars = db.StringField(max_length=200)
