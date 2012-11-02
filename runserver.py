#!/usr/bin/env python
from hascore import app, init_for
from hascore.models import db
init_for('dev')
db.create_all()
app.run('0.0.0.0', debug=True, port=8070)
