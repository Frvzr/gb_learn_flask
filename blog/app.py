from flask import Flask
from blog import commands
from blog.extensions import migrate
from blog.models import User
from blog.auth.views import auth
from blog.user.views import user
from blog.articles.views import articles_app
from blog.models.database import db
from blog.auth.auth import login_manager


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('blog.config')

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(articles_app)
    app.register_blueprint(auth)


def register_commands(app: Flask):
    app.cli.add_command(commands.create_init_user)
    app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_article)

