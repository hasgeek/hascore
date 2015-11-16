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
