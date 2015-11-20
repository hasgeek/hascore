HasCore: HasGeek API
====================

![Build status](https://secure.travis-ci.org/hasgeek/hascore.png)
[![Coverage Status](https://coveralls.io/repos/hasgeek/hascore/badge.png?branch=master)](https://coveralls.io/r/hasgeek/hascore?branch=master)

Hascore provides helper API methods including the networkbar that is shown on all sites, and API endpoints for geolocation and language analysis.

-----
### SETUP DEPENDENCIES

__NLTK__

Hascore requires NLTK. You will need to install NLTK's corpus data. Be warned, this is about 1.8 GB:

    $ python -m nltk.downloader all
    
__Postgres__

Hascore uses Postgres >=9.4 and Redis server for development. To set up a Postgres DB:

In OS X using the [Postgres App](http://postgresapp.com):

    $ # Add Postgres app to the path if it's not already in there
    $ export PATH="/Applications/Postgres.app/Contents/Versions/9.4/bin:$PATH"
    $ # Make the user and database
    $ createuser -d hascore 
    $ createdb -O hascore -W hascore

In any Linux distribution:

    $ sudo -u postgres createuser -d hascore
    $ sudo -u postgres createdb -O hascore hascore
    
Edit the `\instance\setting-sample.py` to change the following variables: `SQLALCHEMY_DATABASE_URI = postgres://hascore:YOUR_PASSWORD_HERE@localhost/hascore`,`LASTUSER_CLIENT_ID = CLIENT_ID` and `LASTUSER_CLIENT_SECRET = CLIENT_SECRET`. CLIENT_ID and CLIENT_SECRET are to be replaced with your actual Client ID and Client Secret registered from [HasGeek Auth](https://auth.hasgeek.com/).

## Installation

Hascore is a [Python](https://www.python.org) based [Flask](http://flask.pocoo.org/) app.

#### Virutalenv + Pip/easy_install

[Virtualenv](docs.python-guide.org/en/latest/dev/virtualenvs/) is strongly recommended to ensure Hascore's elaborate and sometimes version-specific requirements doesn't clash with anything else.

1. Install the required libraries for Hascore in `requirements.txt` using `easy_install` or `pip`:

    `$ pip install -r requirements.txt`

   If you are using OS X and had trouble installing Numpy, please see the instructions here:            
   (https://gist.github.com/goldsmith/7262122)

  
2. Finish configuration with:

    `$ python manage.py db create`
    
3. Add geographical data (GeoNames) to your DB with:

    `$ python /data/geoname.py dev`

4. Before you run the server in development mode, make sure you have Postgres server and Redis server running as well. To start Hascore:

   `$ python runserver.py`

### Usage

Hascore by default runs on port 8070. Access `http://localhost:8070/1/` followed by the module you want to query. For example:

   `$ localhost:8070/1/geo/parse_locations?q=Bhubaneswar`
