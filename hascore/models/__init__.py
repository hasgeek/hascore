# -*- coding: utf-8 -*-

from flask.ext.sqlalchemy import SQLAlchemy
from hascore import app
from coaster.sqlalchemy import IdMixin, TimestampMixin, BaseMixin, BaseNameMixin

db = SQLAlchemy(app)

from hascore.models.user import *
from hascore.models.tag import *
