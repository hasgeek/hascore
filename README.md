HasCore: HasGeek API
====================

![Build status](https://secure.travis-ci.org/hasgeek/hascore.png)
[![Coverage Status](https://coveralls.io/repos/hasgeek/hascore/badge.png?branch=master)](https://coveralls.io/r/hasgeek/hascore?branch=master)

Hascore provides helper API methods including the networkbar that is shown on all sites, and API endpoints for geolocation and language analysis.

-----
### NLTK

Hascore requires NLTK. You will need to install NLTK's corpus data. Be warned, this is about 1.8 GB:

    $ python -m nltk.downloader all
    
### Postgres

Hascore uses Postgres >=9.4 and Redis server for development. To set up a Postgres DB:

On OS X using the [Postgres App](http://postgresapp.com):

    $ createuser -d hascore 
    $ createdb -O hascore -W hasgeek

On any Linux distribution:

    $ sudo -u postgres createuser -d hascore
    $ sudo -u postgres createdb -O hascore hasgeek
    
* Edit the `\instance\setting-sample.py` to change the following variables: `SQLALCHEMY_DATABASE_URI` to `postgres://hasgeek:hasgeek@localhost/hascore_old`, `LASTUSER_CLIENT_ID` to`ID` and `LASTUSER_CLIENT_SECRET` to `pwd`

## Installation

Hascore runs on [Python](https://www.python.org) with the [Flask](http://flask.pocoo.org/) microframework. You can choose to set up your development environment in the following way:

#### Virutalenv + Pip/easy_install

[Virtualenv](docs.python-guide.org/en/latest/dev/virtualenvs/) is strongly recommended to ensure Hascore's elaborate and sometimes version-specific requirements doesn't clash with anything else.

1. Install the required libraries for Hascore in `requirements.txt` using `easy_install` or `pip`:

    `$ pip install -r requirements.txt`

   If you are using Mac OS X and had trouble installing Numpy, please see the instructions here:            
   (https://gist.github.com/goldsmith/7262122)

  
2. Finish configuration with:

    `$ python manange.py db create`

3. Before you run the server in development mode, make sure you have Postgres server and Redis server running as well. To start     Hascore:

    `$ python runserver.py`


