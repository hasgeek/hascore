# -*- coding: utf-8 -*-

from flask import render_template
from coaster.views import jsonp
from .. import app
from ..models import networkbar_data


@app.route('/1/networkbar/networkbar.js')
def networkbar_js():
    """
    Return networkbar as a JS resource.
    """
    return render_template('networkbar.js'), 200, [
        ('Content-Type', 'text/javascript; charset=utf-8')]


@app.route('/1/networkbar/networkbar.json')
def networkbar_json():
    """
    Return networkbar data.
    """
    # Load all links into SQLAlchemy identity map but loop through just the top-level
    return jsonp(networkbar_data())
