import logging
from mongoengine import (Document,
                         StringField, EmbeddedDocumentListField,
                         GenericEmbeddedDocumentField)
from bson.objectid import ObjectId
from hardware import Hardware #noqa

log = logging.getLogger(__name__)


class Category(Document):
    name = StringField(max_length=120)
    products = EmbeddedDocumentListField('Hardware')
    product_schema = GenericEmbeddedDocumentField()

    def get_product(self, id_):
        key_id = ObjectId(id_)
        return self.products.get(_id=key_id)


def get_all_categories():
    return Category.objects.all()


def get_category_by_name(name):
    return Category.objects(name=name).first()
