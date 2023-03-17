from blog.extensions import admin
from flask_admin.contrib.sqla import ModelView
from blog.models import models
from blog.models.database import db

admin.add_view(ModelView(models.Tag, db.session, category='Models'))
admin.add_view(ModelView(models.Article, db.session, category='Models'))
admin.add_view(ModelView(models.Author, db.session, category='Models'))