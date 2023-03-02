from flask import Flask
from blog.user.views import user
from blog.articles.views import articles_app
from blog.models.database import db

def create_app() -> Flask:
    app = Flask(__name__)
    #app.config['SECRET_KEY'] = 'sfdsdfsfffffsfdsdfsf'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    register_blueprints(app)
    return app

def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(articles_app)
