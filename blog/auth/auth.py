from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required
from blog.models.models import User


auth = Blueprint('auth', __name__, static_folder='../static')

login_manager = LoginManager()
login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth.login"))


__all__ = [
    "login_manager",
    "auth",
]
