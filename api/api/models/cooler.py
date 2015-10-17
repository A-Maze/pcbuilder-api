from mongoengine import StringField
from models.hardware import Hardware


class Cooler(Hardware):
    Socket = StringField(max_length=200)
    connection_processor_cooling = StringField(max_length=200)
    heatpipes = StringField(max_length=200)
    volume = StringField(max_length=200)
    rotational_speed_min = StringField(max_length=200)
    rotational_speed_max = StringField(max_length=200)
    type_cooling = StringField(max_length=200)
    height = StringField(max_length=200)
    diameter = StringField(max_length=200)
    colors = StringField(max_length=200)
    materials = StringField(max_length=200)
    warranty = StringField(max_length=200)
    particulars = StringField(max_length=200)
