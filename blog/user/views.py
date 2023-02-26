from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

user = Blueprint("users", __name__, url_prefix='/users', static_folder='../static')

USERS = {
    1: "James",
    2: "Brian",
    3: "Peter",
    }


@user.route("/", endpoint="list")
def user_list():
    return render_template("users/list.html", users=USERS)


@user.route("/<int:pk>/")
def get_user(pk: int):
    try:
        user_name = USERS[pk]
    except KeyError:
        raise NotFound(f"User #{pk} doesn't exist!")
        # return redirect('/users/')
    return render_template('users/details.html', user_id=pk, user_name=user_name)
