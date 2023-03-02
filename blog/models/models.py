from sqlalchemy import Column, Integer, String, Boolean
from blog.models.database import db

class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(80), unique=True)
    password = Column(String(80))
    is_staff = Column(Boolean, nullable=False, default=False)
    
    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"