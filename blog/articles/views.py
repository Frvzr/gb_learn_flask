from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.exceptions import NotFound
from blog.models.models import Article, Author, Tag
from blog.forms.article import CreateArticleForm
from flask_login import login_required, current_user
from blog.models.database import db
from sqlalchemy.orm import joinedload, session
from sqlalchemy import select
from typing import Dict
import requests
from blog.config import API_URL

articles_app = Blueprint("articles_app", __name__, url_prefix='/articles', static_folder='../static')

@articles_app.route("/", methods=['GET'], endpoint="list")
def articles_list():
    _articles = Article.query.all()
    #count_articles: Dict = requests.get(f'{API_URL}/api/articles/event_get_count/').json()
    return render_template(
        'articles/list.html',
        articles=_articles,
        #count_articles=count_articles['count'],

    )


@articles_app.route("/<int:pk>/", methods=['GET'])
def get_articles(pk: int):
    _article: Article = Article.query.filter_by(article_id=pk).options(
joinedload(Article.tags)).one_or_none()

    if _article is None:
        raise NotFound(f"Article #{pk} doesn't exist!")
    return render_template('articles/details.html', articles_app=_article)


@articles_app.route('/create/', methods=['GET'])
@login_required
def create_article_form():
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]
    return render_template('articles/create.html', form=form)

@articles_app.route("/create/", methods=['POST'], endpoint="create")
@login_required
def create_article():
    form = CreateArticleForm(request.form)

    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]

    if form.validate_on_submit():
        _article = Article(title=form.title.data.strip(), text=form.text.data)

        if current_user.authors:
            _article.author_id = current_user.authors.id
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            _article.author_id = author.id
        
        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                _article.tags.append(tag)

        db.session.add(_article)
        db.session.commit()

        return redirect(url_for('articles_app.get_articles', pk=_article.article_id))
    
    return render_template('articles/create.html', form=form)


@articles_app.route("/tag/<int:pk>/", methods=['GET'])
@login_required
def get_articles_by_tag(pk: int):
    article = Article.query.join(Article.tags).filter(Tag.id==pk)
    if article is None:
        raise NotFound(f"Article #{pk} doesn't exist!")
    return render_template('articles/tags.html', articles_app=article)