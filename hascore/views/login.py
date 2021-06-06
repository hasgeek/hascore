import os

from flask import (
    Response,
    flash,
    g,
    get_flashed_messages,
    redirect,
    send_from_directory,
)

from coaster.views import get_next_url

from .. import app, lastuser
from ..models import db


@app.route('/')
def index():
    resp = []
    for category, msg in get_flashed_messages(with_categories=True):
        resp.append('-- %s: %s --' % (category, msg))
    if g.user:
        resp.append('User: %s' % g.user)
    resp.append("Hascore. Got a request?")
    return Response('\n'.join(resp), mimetype="text/plain")


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon',
    )


@app.route('/login')
@lastuser.login_handler
def login():
    return {'scope': 'id'}


@app.route('/logout')
@lastuser.logout_handler
def logout():
    flash("You are now logged out", category='info')
    return get_next_url()


@app.route('/login/redirect')
@lastuser.auth_handler
def lastuserauth():
    # Save the user object
    return redirect(get_next_url())


@app.route('/login/notify', methods=['POST'])
@lastuser.notification_handler
def lastusernotify(user):
    db.session.commit()


@lastuser.auth_error_handler
def lastuser_error(error, error_description=None, error_uri=None):
    if error == 'access_denied':
        flash("You denied the request to login", category='error')
        return redirect(get_next_url())
    return Response(
        "Error: %s\n"
        "Description: %s\n"
        "URI: %s" % (error, error_description, error_uri),
        mimetype="text/plain",
    )
