from mongoengine import (StringField, DateTimeField, IntField, DecimalField,
                         EmbeddedDocument)
import datetime


class Record(EmbeddedDocument):
    price = DecimalField()
    product = IntField()
    webshop = StringField(max_length=200)
    date = DateTimeField(default=datetime.datetime.now())
