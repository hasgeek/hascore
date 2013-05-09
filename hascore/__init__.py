# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.lastuser import Lastuser
from flask.ext.lastuser.sqlalchemy import UserManager
from baseframe import baseframe
import coaster.app

# First, make an app

app = Flask(__name__, instance_relative_config=True)
lastuser = Lastuser()

# Second, import the models and views

import hascore.models
import hascore.views


# Configure the app
def init_for(env):
    coaster.app.init_app(app, env)
    baseframe.init_app(app, requires=['baseframe'])
    lastuser.init_app(app)
    lastuser.init_usermanager(UserManager(hascore.models.db, hascore.models.User))
