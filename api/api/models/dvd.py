from mongoengine import StringField
from models.hardware import Hardware


class Dvd(Hardware):
    drive_bay = StringField(max_length=200)
    Optical_drive_type = StringField(max_length=200)
    hard_drive_bus = StringField(max_length=200)
    dvd_read_speed = StringField(max_length=200)
    dvd_Writing_speed_sl = StringField(max_length=200)
    dvd_Writing_speed_dl = StringField(max_length=200)
    dvd_Rewrite_speed = StringField(max_length=200)
    cd_read_speed = StringField(max_length=200)
    cd_writing_speed = StringField(max_length=200)
    colors = StringField(max_length=200)
