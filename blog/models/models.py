from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Table, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from blog.models.database import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash
from datetime import datetime


article_tag_association_table = Table(
    'article_tag_associations',
    db.metadata,
    Column('article_id', Integer, ForeignKey('articles.article_id'), nullable=False),
    Column('tag_id', Integer, ForeignKey('tags.id'), nullable=False)
)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(80), unique=True)
    first_name = Column(String(80))
    last_name = Column(String(80))
    password = Column(String(80))
    is_staff = Column(Boolean, default=False)
    
    authors = relationship('Author', backref='user', uselist=False)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.email} ({self.id})'

    # def __init__(self, username, email, first_name, last_name, password, is_staff):
    #     self.username = username
    #     self.email = email
    #     self.password = password
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.is_staff = is_staff

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)


class Author(db.Model):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False) 

    articles = relationship('Article', backref='author')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Article(db.Model):
    __tablename__ = 'articles'

    article_id = Column(Integer, primary_key=True)
    title = Column(String(255))
    text = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    created = Column(DateTime, default=datetime.utcnow)
    updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
        
    tags = relationship('Tag', secondary=article_tag_association_table, backref='articles')

    def __str__(self):
        return self.title


class Tag(db.Model):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    def __str__(self):
        return self.name

