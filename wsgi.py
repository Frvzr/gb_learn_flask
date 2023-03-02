from blog.app import create_app
from blog.models.database import db
from blog.models.models import User

app = create_app()

@app.cli.command('init-db')
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()
    print("done!")

@app.cli.command("create-users")
def create_users():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    
    admin = User(username="admin", is_staff=True)
    james = User(username="james")
    db.session.add(admin)
    db.session.add(james)
    db.session.commit()
    print("done! created users:", admin, james)