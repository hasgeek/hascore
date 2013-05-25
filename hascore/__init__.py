# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.assets import Bundle
from flask.ext.lastuser import Lastuser
from flask.ext.lastuser.sqlalchemy import UserManager
from baseframe import baseframe, assets
import coaster.app

# First, make an app

app = Flask(__name__, instance_relative_config=True)
lastuser = Lastuser()

# Second, import the models and views

from . import models, views


# Configure the app
def init_for(env, createdb=False):
    coaster.app.init_app(app, env)
    # This is required before baseframe init:
    if createdb:
        models.db.create_all()
    app.config['NETWORKBAR_DATA'] = models.networkbar_data()

    baseframe.init_app(app, requires=['baseframe'])
    lastuser.init_app(app)
    lastuser.init_usermanager(UserManager(models.db, models.User))
    app.assets.register('js_networkbar',
        Bundle(assets.require('baseframe-networkbar.js'),
            filters='closure_js', output='js/baseframe-networkbar.js'))
    app.assets.register('css_networkbar',
        Bundle(assets.require('baseframe-networkbar.css'),
            filters='cssmin', output='css/baseframe-networkbar.css'))
