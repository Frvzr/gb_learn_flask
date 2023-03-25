from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.models.database import db
from blog.models.models import User
from blog.schemas import UserSchema
from blog.permissions.user import UserListPermisson, UserPatchPermission


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
        'permission_get': [UserListPermisson],
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
            'short_format': [
            'id',
            'email',
            'first_name',
            'last_name',
            'is_staff',
        ],
        'permission_get': [UserListPermisson],
        'permission_patch': [UserPatchPermission],
    }