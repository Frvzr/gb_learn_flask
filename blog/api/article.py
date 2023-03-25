from flask_combo_jsonapi import ResourceList, ResourceDetail
from combojsonapi.event.resource import EventsResource

from blog.models.database import db
from blog.models.models import Article
from blog.schemas import ArticleSchema



class ArtcicleListEvent(EventsResource):

    def event_get_count(self):
        return {'count': Article.query.count()}
    

class ArticleDetailEvent(EventsResource):

    def event_count_by_author(self, **kwargs):
        return {'count':Article.query.filter(Article.author_id==kwargs['article_id']).count()}


class ArticleList(ResourceList):
    events = ArtcicleListEvent
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }


class ArticleDetail(ResourceDetail):
    events = ArticleDetailEvent
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }


