# -*- coding: utf-8 -*-

from coaster.views import jsonp, requestargs
from baseframe import cache
from .. import app
from ..models import GeoName


@app.route('/1/geo/get_by_name')
@requestargs('name')
@cache.memoize(timeout=86400)
def geo_get_by_name(name):
    if name.isdigit():
        geoname = GeoName.query.get(int(name))
    else:
        geoname = GeoName.get(name)
    return jsonp({'status': 'ok', 'result': geoname.as_dict()} if geoname else {'status': 'error', 'error': 'not_found'})


@app.route('/1/geo/get_by_title')
@requestargs('title[]', 'lang')
@cache.memoize(timeout=86400)
def geo_get_by_title(title, lang=None):
    return jsonp({'status': 'ok', 'result': [g.as_dict() for g in GeoName.get_by_title(title, lang)]})


@app.route('/1/geo/parse_locations')
@requestargs('q', 'special[]', 'lang', 'bias[]')
def geo_parse_location(q, special=[], lang=None, bias=[]):
    result = GeoName.parse_locations(q, special, lang, bias)
    for item in result:
        if 'geoname' in item:
                item['geoname'] = item['geoname'].as_dict()
    return jsonp({'status': 'ok', 'result': result})
