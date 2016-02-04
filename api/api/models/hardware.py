import datetime
from mongoengine import (StringField, DynamicEmbeddedDocument, ListField,
                         DateTimeField, EmbeddedDocumentField, ObjectIdField,
                         DictField)
from api.models.record import Record


class Hardware(DynamicEmbeddedDocument):
    _id = ObjectIdField()
    category = StringField(max_length=300)
    name = StringField(max_length=500)
    subname = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    image = StringField(max_length=500)
    ean = StringField(max_length=5000)
    sku = StringField(max_length=5000)
    links = DictField()
    brand = StringField(max_length=200)
    execution = StringField(max_length=200)
    records = ListField(EmbeddedDocumentField(Record))
    current_prices = DictField()
    date_modified = DateTimeField(default=datetime.datetime.now)
