from meta import db
from models.hardware import Hardware


class Memory(Hardware):
    memory_specification = db.StringField(max_length=500)
    serie = db.StringField(max_length=200)
    product = db.StringField(max_length=200)
    memory_size = db.StringField(max_length=200)
    number = db.StringField(max_length=200)
    module_size = db.StringField(max_length=200)
    Price_per_gb = db.StringField(max_length=200)
    memory_type = db.StringField(max_length=200)
    memory_specification = db.StringField(max_length=200)
    low_voltage_ddr = db.StringField(max_length=200)
    memory_cas_latency = db.StringField(max_length=200)
    tension = db.StringField(max_length=200)
    warranty = db.StringField(max_length=200)
    particulars = db.StringField(max_length=200)
