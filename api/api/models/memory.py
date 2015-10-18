from mongoengine import StringField
from models.hardware import Hardware


class Memory(Hardware):
    memory_specification = StringField(max_length=500)
    serie = StringField(max_length=200)
    product = StringField(max_length=200)
    memory_size = StringField(max_length=200)
    number = StringField(max_length=200)
    module_size = StringField(max_length=200)
    Price_per_gb = StringField(max_length=200)
    memory_type = StringField(max_length=200)
    memory_specification = StringField(max_length=200)
    low_voltage_ddr = StringField(max_length=200)
    memory_cas_latency = StringField(max_length=200)
    tension = StringField(max_length=200)
    warranty = StringField(max_length=200)
    particulars = StringField(max_length=200)
