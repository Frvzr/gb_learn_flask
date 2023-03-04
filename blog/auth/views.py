from flask import Blueprint, render_template, request, redirect, url_for
from blog.models.models import User
from blog.auth.auth import auth
from flask_login import login_user, login_required, logout_user


@auth.route("/login", methods=["GET", "POST"], endpoint="login")
def login():
    if request.method == "GET":
        return render_template("auth/login.html")
    username = request.form.get("username")
    if not username:
        return render_template("auth/login.html", error="username not passed")
    user = User.query.filter_by(username=username).one_or_none()
    if user is None:
        return render_template("auth/login.html", error=f"no user {username!r} found")
    
    login_user(user)
    return redirect(url_for("users.list"))


@auth.route("/logout", endpoint="logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("users.list"))


@auth.route("/index")
@login_required
def secret_view():
    return render_template('index.html')

