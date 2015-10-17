from meta import db
from models.hardware import Hardware


class PowerSupply(Hardware):
    Vermogen_watt = db.StringField(max_length=200)
    Product = db.StringField(max_length=200)
    _12V_Rails = db.StringField(max_length=200)
    Capaciteit_12V1_rail = db.StringField(max_length=200)
    Voeding_certificering = db.StringField(max_length=200)
    Aantal_Sata_aansluitingen = db.StringField(max_length=200)
    Aantal_molex_aansluitingen = db.StringField(max_length=200)
    PCI_Express_aansluitingen = db.StringField(max_length=200)
    Aantal_6_pins_aansluitingen = db.StringField(max_length=200)
    Aantal_6_2_pins_aansluitingen = db.StringField(max_length=200)
    Modulair = db.StringField(max_length=200)
    Aantal_ventilatoren = db.StringField(max_length=200)
    Diameter_ventilator = db.StringField(max_length=200)
    Type_koeling = db.StringField(max_length=200)
    Ventilator_locatie = db.StringField(max_length=200)
    Voedingtype = db.StringField(max_length=200)
    Stroomspanningbeveiliging = db.StringField(max_length=200)
    Breedte = db.StringField(max_length=200)
    Hoogte = db.StringField(max_length=200)
    Diepte = db.StringField(max_length=200)
    Fabrieksgarantie = db.StringField(max_length=200)
    Bijzonderheden = db.StringField(max_length=200)
