#!/usr/bin/env python
# -*- coding: utf-8 -*-

from coaster.manage import init_manager
from hascore import app
from hascore.models import db

if __name__ == '__main__':
    db.init_app(app)
    manager = init_manager(app, db)
    manager.run()
