from mongoengine import Document, ReferenceField, ListField, StringField
from hardware import Hardware #noqa


class Category(Document):
    name = StringField(max_length=120)
    products = ListField(ReferenceField('Hardware'))

    def product(self, id_):
        return (item for item in self.product if item[id] == id_).next()


def get_all_categories():
    return Category.objects.all()


def get_category_by_name(name):
    return Category.objects(name=name).first()
