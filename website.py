import sys
import os.path
sys.path.insert(0, os.path.dirname(__file__))
from hascore import app as application, views
with application.test_request_context():
	views.networkbar.cache_networkbar_links()
