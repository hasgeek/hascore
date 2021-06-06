import os.path
import sys

__all__ = ['application']

sys.path.insert(0, os.path.dirname(__file__))
from hascore import app as application  # isort:skip
from hascore import views  # isort:skip

with application.test_request_context():
    views.networkbar.cache_networkbar_links()
