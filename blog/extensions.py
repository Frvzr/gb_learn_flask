from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_admin import Admin
from blog.admin.views import CustomAdminIndexView

migrate = Migrate()
csrf = CSRFProtect()
admin = Admin(
    index_view=CustomAdminIndexView(),
    name='Blog Admin Panel',
    template_mode='bootstrap4',
)