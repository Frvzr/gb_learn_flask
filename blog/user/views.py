from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.exceptions import NotFound
from blog.models import User
from flask_login import login_required, current_user, login_user
from blog.forms.user import UserRegisterForm
from werkzeug.security import generate_password_hash
from blog.models.database import db


user = Blueprint("users", __name__, url_prefix='/users', static_folder='../static')


@user.route('register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('users.profile', pk=current_user.id))
    
    form = UserRegisterForm(request.form)
    
    errors = []
    if request.method == 'POST' and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append('email already exists')
            return render_template('users/register.html', form=form)

        _user = User(
            username=form.username.data,
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password=generate_password_hash(form.password.data),
        )

        db.session.add(_user)
        db.session.commit()

        login_user(_user)

    return render_template(
        'users/register.html',
        form=form,
        errors=errors,
    )

@user.route('/', endpoint="list")
def user_list():
    users = User.query.all()
    return render_template(
        'users/list.html',
        users=users,
    )


@user.route('/<int:pk>')
@login_required
def profile(pk: int):
    selected_user = User.query.filter_by(id=pk).one_or_none()
    if not selected_user:
        raise NotFound(f"User #{pk} doesn't exist!")

    return render_template(
        'users/details.html',
        user=selected_user,
    )
