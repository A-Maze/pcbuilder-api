from meta import db
from models.hardware import Hardware


class dvd(Hardware):
    Drive_Bay = db.StringField(max_length=200)
    Optisch_stationtype = db.StringField(max_length=200)
    Hardeschijf_bus = db.StringField(max_length=200)
    DVD_Leessnelheid = db.StringField(max_length=200)
    DVD_Schrijfsnelheid_SL = db.StringField(max_length=200)
    DVD_Schrijfsnelheid_DL = db.StringField(max_length=200)
    DVD_Herschrijfsnelheid = db.StringField(max_length=200)
    CD_Leessnelheid = db.StringField(max_length=200)
    CD_Schrijfsnelheid = db.StringField(max_length=200)
    Kleuren = db.StringField(max_length=200)
    Verkoopstatus = db.StringField(max_length=200)
