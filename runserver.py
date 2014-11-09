#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from hascore import app, init_for
init_for('dev')
with app.test_request_context():
	views.networkbar.cache_networkbar_links()

try:
    port = int(sys.argv[1])
except (IndexError, ValueError):
    port = 8070
app.run('0.0.0.0', port=port, debug=True)
