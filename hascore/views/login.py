# -*- coding: utf-8 -*-

import os
from flask import g, send_from_directory, Response, redirect, get_flashed_messages, flash
from coaster.views import get_next_url

from .. import app, lastuser


@app.route('/')
def index():
    resp = []
    for category, msg in get_flashed_messages(with_categories=True):
        resp.append(u'-- %s: %s --' % (category, msg))
    if g.user:
        resp.append(u'User: %s' % g.user)
    resp.append(u"HasCore. Got a request?")
    return Response(u'\n'.join(resp), mimetype="text/plain")


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/login')
@lastuser.login_handler
def login():
    return {'scope': 'id'}


@app.route('/logout')
@lastuser.logout_handler
def logout():
    flash(u"You are now logged out", category='info')
    return get_next_url()


@app.route('/login/redirect')
@lastuser.auth_handler
def lastuserauth():
    # Save the user object
    return redirect(get_next_url())


@lastuser.auth_error_handler
def lastuser_error(error, error_description=None, error_uri=None):
    if error == 'access_denied':
        flash("You denied the request to login", category='error')
        return redirect(get_next_url())
    return Response(u"Error: %s\n"
                    u"Description: %s\n"
                    u"URI: %s" % (error, error_description, error_uri),
                    mimetype="text/plain")
