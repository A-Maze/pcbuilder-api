from meta import db
from models.hardware import Hardware


class Cooler(Hardware):
    Socket = db.StringField(max_length=200)
    connection_processor_cooling = db.StringField(max_length=200)
    heatpipes = db.StringField(max_length=200)
    volume = db.StringField(max_length=200)
    rotational_speed_min = db.StringField(max_length=200)
    rotational_speed_max = db.StringField(max_length=200)
    type_cooling = db.StringField(max_length=200)
    height = db.StringField(max_length=200)
    diameter = db.StringField(max_length=200)
    colors = db.StringField(max_length=200)
    materials = db.StringField(max_length=200)
    warranty = db.StringField(max_length=200)
    particulars = db.StringField(max_length=200)
