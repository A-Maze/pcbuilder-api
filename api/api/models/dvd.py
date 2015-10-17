from meta import db
from models.hardware import Hardware


class dvd(Hardware):
    drive_bay = db.StringField(max_length=200)
    Optical_drive_type = db.StringField(max_length=200)
    hard_drive_bus = db.StringField(max_length=200)
    dvd_read_speed = db.StringField(max_length=200)
    dvd_Writing_speed_sl = db.StringField(max_length=200)
    dvd_Writing_speed_dl = db.StringField(max_length=200)
    dvd_Rewrite_speed = db.StringField(max_length=200)
    cd_read_speed = db.StringField(max_length=200)
    cd_writing_speed = db.StringField(max_length=200)
    colors = db.StringField(max_length=200)
