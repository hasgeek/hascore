# -*- coding: utf-8 -*-

from flask import Flask
from flask_migrate import Migrate
from flask_assets import Bundle
from flask_lastuser import Lastuser
from flask_lastuser.sqlalchemy import UserManager
from baseframe import baseframe, assets
import coaster.app

# First, make an app

app = Flask(__name__, instance_relative_config=True)
lastuser = Lastuser()

# Second, import the models and views

from . import models, views  # NOQA
from .models import db       # NOQA


# Configure the app
coaster.app.init_app(app)
db.init_app(app)
db.app = app
migrate = Migrate(app, db)

baseframe.init_app(app, requires=['baseframe'])
lastuser.init_app(app)
lastuser.init_usermanager(UserManager(models.db, models.User))
app.assets.register('js_networkbar',
    Bundle(assets.require('baseframe-networkbar.js'),
        filters='closure_js', output='js/baseframe-networkbar.js'))
app.assets.register('css_networkbar',
    Bundle(assets.require('baseframe-networkbar.css'),
        filters='cssmin', output='css/baseframe-networkbar.css'))
