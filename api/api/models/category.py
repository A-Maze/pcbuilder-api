import logging
from mongoengine import (Document, ListField,
                         StringField, EmbeddedDocumentField)
from bson.objectid import ObjectId
from hardware import Hardware #noqa

log = logging.getLogger(__name__)


class Category(Document):
    name = StringField(max_length=120)
    products = ListField(EmbeddedDocumentField('Hardware'))

    def get_product(self, id_):
        key_id = ObjectId(id_)
        return [product for product in self.products if product.id == key_id][0]


def get_all_categories():
    return Category.objects.all()


def get_category_by_name(name):
    return Category.objects(name=name).first()
