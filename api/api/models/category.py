import logging
from mongoengine import (Document,
                         StringField, EmbeddedDocumentListField)
from mongoengine.queryset import DoesNotExist
from api.models.hardware import Hardware  # noqa

log = logging.getLogger(__name__)


class Category(Document):
    name = StringField(max_length=120)
    products = EmbeddedDocumentListField('Hardware')
    product_schema = StringField()

    def get_product(self, key):
        for product in self.products:
            if str(product._id) == key:
                return product
            elif product.ean and key in product.ean:
                return product
            elif product.sku and key in product.sku:
                return product
        raise DoesNotExist


def get_all_categories():
    return Category.objects.all()


def get_category_by_name(name):
    return Category.objects(name=name).first()
