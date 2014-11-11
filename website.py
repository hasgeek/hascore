import sys
import os.path
sys.path.insert(0, os.path.dirname(__file__))
from hascore import app as application, init_for, views
init_for('production')
with application.test_request_context():
	views.networkbar.cache_networkbar_links()
