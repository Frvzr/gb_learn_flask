from flask import Flask
from blog.user.views import user
from blog.articles.views import articles_app
from blog.auth.views import auth
from blog.models.database import db
from blog.auth.auth import login_manager

def create_app() -> Flask:
    app = Flask(__name__)
    app.debug = True
    app.config['SECRET_KEY'] = 'sfdsdfsfffffsfdsdfsf'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    login_manager.init_app(app)
    register_blueprints(app)
    return app

def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(articles_app)
    app.register_blueprint(auth)
    

