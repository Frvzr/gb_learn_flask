from blog.app import create_app
# from blog.models.database import db
# from blog.models.models import User, Article

app = create_app()

# @app.cli.command('init-db')
# def init_db():
#     """
#     Run in your terminal:
#     flask init-db
#     """
#     db.create_all()
#     print("done!")

# @app.cli.command("create-users")
# def create_users():
#     """
#     Run in your terminal:
#     flask create-users
#     > done! created users: <User #1 'admin'> <User #2 'james'>
#     """
    
#     admin = User(username="admin1", email='admin1@admin.com', password='admin', is_staff=True)
#     db.session.add(admin)
#     db.session.commit()
#     print("done! created users:", admin)

# @app.cli.command("create-article")
# def create_article():
#     """
#     Run in your terminal:
#     flask create-article
#     > done! created users: <Article #1> 
#     """
    
#     first_article = Article(title="first", text="forst article", user_id=1)
#     db.session.add(first_article)
#     db.session.commit()
#     print("done! created article:", first_article)