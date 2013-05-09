# -*- coding: utf-8 -*-

from flask import render_template

from hascore import app


@app.route('/1/networkbar/networkbar.js')
def networkbar_js():
    """
    Return networkbar as a JS resource.
    """
    return render_template('networkbar.js'), 200, [
        ('Content-Type', 'text/javascript; charset=utf-8')]
