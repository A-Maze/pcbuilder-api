from mongoengine import (StringField, DateTimeField, IntField, DecimalField,
                         EmbeddedDocument)
import datetime


class Record(EmbeddedDocument):
    price = DecimalField()
    product = IntField()
    webshop = StringField()
    date = DateTimeField(default=datetime.datetime.now)
