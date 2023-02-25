from flask import Flask
from blog.user.views import user
from blog.articles.views import articles_app


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app.run()

def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(articles_app)

