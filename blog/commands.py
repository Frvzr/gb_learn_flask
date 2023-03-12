import click
from werkzeug.security import generate_password_hash

from blog.models.database import db


@click.command('create-init-user')
def create_init_user():
    from blog.models.models import User
    from wsgi import app

    with app.app_context():
        admin = User(username='Admin',email='admin@example.com', first_name="Ivan",  password=generate_password_hash('admin'))
        test = User(username='Test',email='test@example.com', first_name="Iv", password=generate_password_hash('test'))
        db.session.add(admin)
        db.session.add(test)
        db.session.commit()

@click.command('init-db')
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()
    print("done!")

@click.command("create-article")
def create_article():
    """
    Run in your terminal:
    flask create-article
    > done! created users: <Article #1> 
    """
    from blog.models.models import Article
    from wsgi import app

    with app.app_context():
        first_article = Article(title="first", text="first article", user_id=1)
        second = Article(title="Django", text="это высокоуровневый веб-фреймворк, написанный на языке Python, который позволяет быстро и эффективно создавать сложные веб-приложения. Он включает в себя множество готовых компонентов, таких как система аутентификации пользователей, ORM для работы с базами данных, система маршрутизации, шаблонизатор и многое другое.", user_id=2)
        db.session.add(first_article)
        db.session.add(second)
        db.session.commit()
        print("done! created article:", first_article)

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


@click.command("create-tags")
def create_init_tags():
    from blog.models.models import Tag
    from wsgi import app

    with app.app_context():
        tags = ('flask', 'django', 'python', 'SQL')
        for item in tags:
            tag = Tag(name=item)
            db.session.add(tag)
        db.session.commit()
    click.echo(f'Created tags: {",".join(tags)}')