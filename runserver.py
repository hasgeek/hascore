#!/usr/bin/env python
from hascore import app
from hascore.models import db
db.create_all()
app.run(debug=True, port=8000)
