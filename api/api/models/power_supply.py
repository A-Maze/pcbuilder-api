from mongoengine import StringField
from models.hardware import Hardware


class PowerSupply(Hardware):
    power_watt = StringField(max_length=200)
    product = StringField(max_length=200)
    _12v_rails = StringField(max_length=200)
    capacity_12v1_rail = StringField(max_length=200)
    power_certification = StringField(max_length=200)
    number_of_sata_connectors = StringField(max_length=200)
    number_molex_connectors = StringField(max_length=200)
    pci_express_connectors = StringField(max_length=200)
    number_6_pins_connections = StringField(max_length=200)
    number_6_2_pins_connections = StringField(max_length=200)
    modular = StringField(max_length=200)
    number_of_fans = StringField(max_length=200)
    diameter_fan = StringField(max_length=200)
    cooling_type = StringField(max_length=200)
    fan_location = StringField(max_length=200)
    Power_type = StringField(max_length=200)
    power_surge_protection = StringField(max_length=200)
    width = StringField(max_length=200)
    height = StringField(max_length=200)
    depth = StringField(max_length=200)
    warranty = StringField(max_length=200)
    particulars = StringField(max_length=200)
