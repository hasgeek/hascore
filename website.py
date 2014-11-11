import sys
import os.path
import views
sys.path.insert(0, os.path.dirname(__file__))
from hascore import app as application, init_for
init_for('production')
with app.test_request_context():
	views.networkbar.cache_networkbar_links()
