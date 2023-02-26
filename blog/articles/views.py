from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound


articles_app = Blueprint("articles_app", __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {
    1: "Flask", 
    2: "Django", 
    3: "JSON:API"}

@articles_app.route("/", endpoint="list")
def articles_list():
    return render_template("articles/list.html", articles_app=ARTICLES)

@articles_app.route("/<int:pk>/")
def get_articles(pk: int):
    try:
        articles_name = ARTICLES[pk]
    except KeyError:
        raise NotFound(f"Articles {pk} doesn't exists")
    return render_template('articles/details.html', articles_id=pk, articles_name=articles_name)