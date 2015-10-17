from meta import db
import datetime


class History(db.EmbeddedDocument):
    price = db.DecimalField()
    webshop = db.StringField(max_length=200)
    date = db.DateTimeField(default=datetime.datetime.now)
