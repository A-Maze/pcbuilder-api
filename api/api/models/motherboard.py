from meta import db
from models.hardware import Hardware


class Motherboard(Hardware):
    Serie = db.StringField(max_length=200)
    Product = db.StringField(max_length=200)
    Socket = db.StringField(max_length=200)
    Aantal_socket = db.StringField(max_length=200)
    Form_Factor = db.StringField(max_length=200)
    BIOS_of_UEFI = db.StringField(max_length=200)
    Dual_of_Single_BIOS_UEFI = db.StringField(max_length=200)
    Moederbordchipset = db.StringField(max_length=200)
    Geheugentype = db.StringField(max_length=200)
    Maximum_geheugengrootte = db.StringField(max_length=200)
    Hardeschijf_bus = db.StringField(max_length=200)
    Raid_modi = db.StringField(max_length=200)
    Card_Interface = db.StringField(max_length=200)
    Aantal_PCIe = db.StringField(max_length=200)
    Link_Interface = db.StringField(max_length=200)
    Verbinding_Ethernet = db.StringField(max_length=200)
    Netwerkchip = db.StringField(max_length=200)
    Bluetooth_aanwezig = db.StringField(max_length=200)
    Verbinding_USB = db.StringField(max_length=200)
    Video_uit = db.StringField(max_length=200)
    Verbinding = db.StringField(max_length=200)
    Audio_kanalen = db.StringField(max_length=200)
    Audio_uitgangen = db.StringField(max_length=200)
    Audiochip = db.StringField(max_length=200)
