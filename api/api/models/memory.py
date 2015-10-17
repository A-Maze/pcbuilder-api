from meta import db
from models.hardware import Hardware


class Memory(Hardware):
    Geheugen_Specificatie = db.StringField(max_length=500)
    Serie = db.StringField(max_length=200)
    Product = db.StringField(max_length=200)
    Geheugengrootte = db.StringField(max_length=200)
    Aantal = db.StringField(max_length=200)
    Modulegrootte = db.StringField(max_length=200)
    Prijs_per_GB = db.StringField(max_length=200)
    Geheugentype = db.StringField(max_length=200)
    Geheugen_Specificatie = db.StringField(max_length=200)
    Low_Voltage_DDR = db.StringField(max_length=200)
    Geheugen_CAS_Latency = db.StringField(max_length=200)
    Spanning = db.StringField(max_length=200)
    Fabrieksgarantie = db.StringField(max_length=200)
    Bijzonderheden = db.StringField(max_length=200)
