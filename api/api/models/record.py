from meta import db
import datetime


class Record(db.EmbeddedDocument):
    price = db.DecimalField()
    product = db.IntegerField()
    webshop = db.StringField(max_length=200)
    date = db.DateTimeField(default=datetime.datetime.now)
