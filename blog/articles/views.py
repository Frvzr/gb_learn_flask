from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.exceptions import NotFound
from blog.models.models import Article, Author
from blog.forms.article import CreateArticleForm
from flask_login import login_required, current_user
from blog.models.database import db

articles_app = Blueprint("articles_app", __name__, url_prefix='/articles', static_folder='../static')

@articles_app.route("/", methods=['GET'], endpoint="list")
def articles_list():
    articles = Article.query.all()
    return render_template("articles/list.html", articles=articles)

@articles_app.route("/<int:pk>/", methods=['GET'])
def get_articles(pk: int):
    article: Article = Article.query.filter_by(article_id=pk).one_or_none()
    if article is None:
        raise NotFound(f"Article #{pk} doesn't exist!")
    return render_template('articles/details.html', articles_app=article)

@articles_app.route("/create/", methods=['GET', 'POST'], endpoint="create")
@login_required
def create_article():
    form = CreateArticleForm(request.form)
    errors = []

    if form.validate_on_submit():
        _article = Article(title=form.title.data.strip(), text=form.text.data)

        if current_user.authors:
            _article.authors_id = current_user.authors
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            _article.author_id= author.id

        db.session.add(_article)
        db.session.commit()

        return redirect(url_for('article.get_articles', article_id=_article.id))
    
    return render_template('articles/create.html', form=form, errors=errors)
