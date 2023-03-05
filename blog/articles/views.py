from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from blog.models.models import Article


articles_app = Blueprint("articles_app", __name__, url_prefix='/articles', static_folder='../static')

@articles_app.route("/", endpoint="list")
def articles_list():
    articles = Article.query.all()
    return render_template("articles/list.html", articles=articles)

@articles_app.route("/<int:pk>/")
def get_articles(pk: int):
    article = Article.query.filter_by(article_id=pk).one_or_none()
    if article is None:
        raise NotFound(f"Article #{pk} doesn't exist!")
    return render_template('articles/details.html', articles_app=article)