import datetime
from mongoengine import (StringField, Document, ListField, DateTimeField,
                         EmbeddedDocumentField, ReferenceField)
from record import Record



class Hardware(Document):
    category = ReferenceField('Category')
    name = StringField(max_length=500)
    subname = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    image = StringField(max_length=500)
    ean = StringField(max_length=200)
    sku = StringField(max_length=200)
    SKU = StringField(max_length=200)
    link = StringField(max_length=200)
    brand = StringField(max_length=200)
    execution = StringField(max_length=200)
    records = ListField(EmbeddedDocumentField(Record))
    date_modified = DateTimeField(default=datetime.datetime.now)