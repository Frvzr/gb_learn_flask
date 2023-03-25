from flask import Blueprint, render_template
from blog.models.models import Author, Article
from flask_login import login_required
from werkzeug.exceptions import NotFound


author = Blueprint("authors", __name__, url_prefix='/authors', static_folder='../static')

@author.route('/', endpoint="list")
def author_list():
    authors = Author.query.all()
    return render_template(
        'authors/list.html',
        authors=authors,
    )

@author.route('/articles/<int:pk>', methods=['GET'])
@login_required
def get_articles_by_author(pk: int):
    _article = Article.query.join(Author.articles).filter(Author.id==pk)
    if _article is None:
        raise NotFound(f"Article #{pk} doesn't exist!")
    return render_template('authors/articles.html', author=_article)