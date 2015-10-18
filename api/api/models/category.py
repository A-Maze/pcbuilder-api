from mongoengine import Document, ReferenceField, ListField, StringField


class Category(Document):
    name = StringField(max_length=120)
    products = ListField(ReferenceField('Hardware'))


def get_all_categories():
    return Category.objects.all()


def get_category_by_id(id_):
    return Category.objects(id=id_).first()
