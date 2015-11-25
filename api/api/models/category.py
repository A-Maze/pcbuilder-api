import logging

from mongoengine import (Document,
                         StringField, EmbeddedDocumentListField)

from hardware import Hardware  # noqa

log = logging.getLogger(__name__)


class Category(Document):
    name = StringField(max_length=120)
    products = EmbeddedDocumentListField('Hardware')
    product_schema = StringField()

    def get_product(self, key):
        return self.products.exclude(
                                    _id=key,
                                    ean=key,
                                    sku=key).first()


def get_all_categories():
    return Category.objects.all()


def get_category_by_name(name):
    return Category.objects(name=name).first()
