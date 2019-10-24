# -*- coding: utf-8 -*-

from flask import render_template

from baseframe import networkbar_cache
from coaster.views import jsonp

from .. import app
from ..models import networkbar_data


@app.route('/1/networkbar/networkbar.js')
def networkbar_js():
    """
    Return networkbar as a JS resource.
    """
    return (
        render_template('networkbar.js'),
        200,
        [('Content-Type', 'text/javascript; charset=utf-8')],
    )


@app.route('/1/networkbar/networkbar.json')
def networkbar_json():
    """
    Return networkbar data.
    """
    return jsonp(links=networkbar_data())


def cache_networkbar_links():
    """
    Refresh networkbar cache.
    """
    networkbar_cache.delete('networkbar-links')
    data = networkbar_data()
    app.config['NETWORKBAR_LINKS'] = data
    networkbar_cache.set('networkbar_links', data)
