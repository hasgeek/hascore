HasCore: HasGeek API
====================

![Build status](https://secure.travis-ci.org/hasgeek/hascore.png)
[![Coverage Status](https://coveralls.io/repos/hasgeek/hascore/badge.png?branch=master)](https://coveralls.io/r/hasgeek/hascore?branch=master)

Hascore provides helper API methods including the networkbar that is shown
on all sites, and API endpoints for geolocation and language analysis.

Hascore requires NLTK. You will need to install NLTK's corpus data.
Be warned, this is about 1.8 GB:

    $ python -m nltk.downloader all

If you are using Mac OS X and had trouble installing Numpy, please see the
instructions here: https://gist.github.com/goldsmith/7262122

### Install

Ensure you have [Postgres]() installed and running. Setup the DB with:

    $ createuser hascore
    $ createdb -O hascore hascore

It's recommended to use [Virtualenv](docs.python-guide
.org/en/latest/dev/virtualenvs/). To install hascore, run:

    $ pip install -r requirements.txt

Run the server with:

    $ python runserver.py

### Usage

Hascore by default runs on port 8070. Access `http://localhost:8070/1/` followed
by the module you want to query. For example:
`localhost:8070/1/geo/parse_locations?q=goa`