from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from blog.models.database import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(80), unique=True)
    first_name = Column(String(80))
    password = Column(String(80))
    is_staff = Column(Boolean, nullable=False, default=False)
    
    atricles = relationship('Article', backref='user', lazy=True)
    
    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"


class Article(db.Model):
    __tablename__ = 'articles'

    article_id = Column(Integer, primary_key=True)
    title = Column(String(255))
    text = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f"<Article #{self.article_id} {self.title!r}>"