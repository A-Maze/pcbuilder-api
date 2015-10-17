from meta import db
import datetime


class Hardware(db.Document):
    category = db.StringField(max_length=120)
    name = db.StringField(max_length=500)
    subname = db.StringField(max_length=500)
    info = db.StringField(max_length=500)
    stock = db.StringField(max_length=500)
    price = db.DecimalField()
    image = db.StringField(max_length=500)
    ean = db.StringField(max_length=200)
    sku = db.StringField(max_length=200)
    SKU = db.StringField(max_length=200)
    webshop = db.StringField(max_length=200)
    link = db.StringField(max_length=200)
    brand = db.StringField(max_length=200)
    Uitvoering = StringField(max_length=200)
    date_modified = db.DateTimeField(default=datetime.datetime.now)
