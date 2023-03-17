from flask_combo_jsonapi import ResourceList, ResourceDetail
from blog.schemas import TagSchema
from blog.models.models import Tag
from blog.models.database import db


class TagList(ResourceList):
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag,
    }


class TagDetail(ResourceDetail):
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag,
    }