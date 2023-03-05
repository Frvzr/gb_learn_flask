from flask import render_template, request, redirect, url_for, flash
from blog.models.models import User
from blog.auth.auth import auth
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash
from werkzeug.exceptions import NotFound
from blog.forms.auth import LoginForm

@auth.route('/login', methods=('GET',))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))

    return render_template('auth/login.html', form=LoginForm(request.form))

@auth.route('/login', methods=('POST',))
def login_post():
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if not user or not user.check_password(form.password.data):
            flash('Check your login details')
            return redirect(url_for('.login'))

        login_user(user)
        return redirect(url_for('users.profile', pk=user.id))

    return render_template('auth/login.html', form=form)


@auth.route("/logout", endpoint="logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("users.list"))


@auth.route("/index")
@login_required
def secret_view():
    return render_template('index.html')

