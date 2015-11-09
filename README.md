HasCore: HasGeek API
====================

![Build status](https://secure.travis-ci.org/hasgeek/hascore.png)
[![Coverage Status](https://coveralls.io/repos/hasgeek/hascore/badge.png?branch=master)](https://coveralls.io/r/hasgeek/hascore?branch=master)

Hascore provides helper API methods including the networkbar that is shown
on all sites, and API endpoints for geolocation and language analysis.

##How to install HasCore on your machine.

Git clone the HasCore repo or fork it from HasGeek repo and then clone the forked repo,if you wish to send pull requests.

Hascore requires NLTK. You will need to install NLTK's corpus data. Be warned, this is about 1.8 GB:

   `$ python -m nltk.downloader all`

If you wish to run hascore in virtual environment, then create a virtual environment in same folder where you cloned the HasCore repo.

   `$ virtualenv <name of your virtual environment>`

Follow the link http://docs.python-guide.org/en/latest/dev/virtualenvs/, to learn more about virtual environments.

Activate the virtual environment.

   `$ source <name of the virtual environment>/bin/activate`

Install the required libraries for HasCore.

   `$ pip install -r requirements.txt`

If you are using Mac OS X and had trouble installing Numpy, please see the instructions here: https://gist.github.com/goldsmith/7262122

Note: psycong2 requires PostgreSQL server installation.

Copy the setting-sample.py file in instance folder to development.py  
   `$ cp settings-sample.py development.py`

Edit the following fields in development.py (where 'ID' and 'pwd' are the authentication obtained from HasGeek):

``` 
   SQLALCHEMY_DATABASE_URI = 'postgres://hasgeek:hasgeek@localhost/hascore_old'
   LASTUSER_CLIENT_ID = 'ID'
   LASTUSER_CLIENT_SECRET = 'pwd'
``` 

Create the PostgreSQL database by running the command:

   `$ python manange.py`

Assuming you have PostgreSQL and Redis server installed on your machine, run the HasCore server by running this command:

   `$ python runserver.py`


