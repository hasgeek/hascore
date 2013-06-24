# -*- coding: utf-8 -*-

from flask.ext.admin.contrib.sqlamodel import ModelView
from .. import lastuser
from ..models import db, NetworkLink


class AuthModelView(ModelView):
    def is_accessible(self):
        return lastuser.has_permission('siteadmin')


def init_admin(admin):
    admin.add_view(AuthModelView(NetworkLink, db.session))
