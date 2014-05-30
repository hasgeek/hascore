# -*- coding: utf-8 -*-

from sqlalchemy.dialects.postgresql import ARRAY
from coaster.utils import make_name
from . import db, BaseMixin, BaseNameMixin
# from sqlalchemy.ext.declarative import declared_attr
# from sqlalchemy.sql import func

__all__ = ['GeoName', 'GeoCountryInfo', 'GeoAdmin1Code', 'GeoAdmin2Code', 'GeoAltName']


class GeoCountryInfo(BaseNameMixin, db.Model):
    __tablename__ = 'geo_country_info'

    geonameid = db.synonym('id')
    geoname = db.relationship('GeoName', uselist=False,
        primaryjoin='GeoCountryInfo.id == foreign(GeoName.id)',
        backref='has_country')
    iso_alpha2 = db.Column(db.CHAR(2), unique=True)
    iso_alpha3 = db.Column(db.CHAR(3), unique=True)
    iso_numeric = db.Column(db.Integer)
    fips_code = db.Column(db.Unicode(3))
    capital = db.Column(db.Unicode(200))
    area_in_sqkm = db.Column(db.Numeric)
    population = db.Column(db.BigInteger)
    continent = db.Column(db.CHAR(2))
    tld = db.Column(db.Unicode(3))
    currency_code = db.Column(db.CHAR(3))
    currency_name = db.Column(db.Unicode(13))
    phone = db.Column(db.Unicode(16))
    postal_code_format = db.Column(db.Unicode(55))
    postal_code_regex = db.Column(db.Unicode(155))
    languages = db.Column(ARRAY(db.Unicode(7), dimensions=1))
    neighbours = db.Column(ARRAY(db.CHAR(2), dimensions=1))
    equivalent_fips_code = db.Column(db.Unicode(3))

    # @declared_attr
    # def __table_args__(cls):
    #     return (db.Index('ix_geo_country_info_title',
    #         func.to_tsvector("english", cls.title),
    #         postgresql_using='gin'),)

    def __repr__(self):
        return '<GeoCountryInfo %d "%s">' % (self.geonameid, self.title)


class GeoName(BaseNameMixin, db.Model):
    __tablename__ = 'geo_name'

    geonameid = db.synonym('id')
    ascii_title = db.Column(db.String(200))
    latitude = db.Column(db.Numeric)
    longitude = db.Column(db.Numeric)
    fclass = db.Column(db.CHAR(1))
    fcode = db.Column(db.Unicode(10))
    country_id = db.Column('country', db.CHAR(2), db.ForeignKey('geo_country_info.iso_alpha2'))
    country = db.relationship('GeoCountryInfo')
    cc2 = db.Column(db.Unicode(60))
    admin1 = db.Column(db.Unicode(20))
    admin1code = db.relationship('GeoAdmin1Code', uselist=False,
        primaryjoin='and_(GeoName.country_id == foreign(GeoAdmin1Code.country_id), '
            'GeoName.admin1 == foreign(GeoAdmin1Code.admin1_code))')
    admin2 = db.Column(db.Unicode(80))
    admin2code = db.relationship('GeoAdmin2Code', uselist=False,
        primaryjoin='and_(GeoName.country_id == foreign(GeoAdmin2Code.country_id), '
            'GeoName.admin1 == foreign(GeoAdmin2Code.admin1_code), '
            'GeoName.admin2 == foreign(GeoAdmin2Code.admin2_code))')
    admin3 = db.Column(db.Unicode(20))
    admin4 = db.Column(db.Unicode(20))
    population = db.Column(db.BigInteger)
    elevation = db.Column(db.Integer)
    dem = db.Column(db.Integer)  # Digital Elevation Model
    timezone = db.Column(db.Unicode(40))
    moddate = db.Column(db.Date)

    # @declared_attr
    # def __table_args__(cls):
    #     return (
    #         db.Index('ix_geo_name_title',
    #             func.to_tsvector("english", cls.title),
    #             postgresql_using='gin'),
    #         db.Index('ix_geo_name_ascii_title',
    #             func.to_tsvector("english", cls.ascii_title),
    #             postgresql_using='gin'),

    @property
    def short_title(self):
        if self.has_country:
            return self.has_country.title
        elif self.has_admin1code:
            return self.admin1code.title
        elif self.has_admin2code:
            return self.admin2code.title
        else:
            return self.ascii_title or self.title

    @property
    def geoname(self):
        return self

    def make_name(self, reserved=[]):
        if self.ascii_title:
            usetitle = self.ascii_title
            if self.fclass == u'A' and self.fcode.startswith(u'PCL'):
                if u'of the' in usetitle:
                    usetitle = usetitle.split(u'of the')[-1].strip()
                elif u'of The' in usetitle:
                    usetitle = usetitle.split(u'of The')[-1].strip()
                elif u'of' in usetitle:
                    usetitle = usetitle.split(u'of')[-1].strip()
            elif self.fclass == u'A' and self.fcode == 'ADM1':
                usetitle = usetitle.replace(u'State of', '').replace(u'Union Territory of', '').strip()

            if self.id:
                checkused = lambda c: bool(c in reserved or
                    GeoName.query.filter(GeoName.id != self.id).filter_by(name=c).count())
            else:
                checkused = lambda c: bool(c in reserved or GeoName.query.filter_by(name=c).count())
            self.name = make_name(usetitle, maxlength=250, checkused=checkused)

    def __repr__(self):
        return '<GeoName %d %s %s %s "%s">' % (self.geonameid, self.country_id, self.fclass, self.fcode, self.ascii_title)

    def related_geonames(self):
        related = {}
        if self.admin2code and self.admin2code.geonameid != self.geonameid:
            related['admin2'] = self.admin2code.geoname
        if self.admin1code and self.admin1code.geonameid != self.geonameid:
            related['admin1'] = self.admin1code.geoname
        if self.country and self.country.geonameid != self.geonameid:
            related['country'] = self.country.geoname
        return related

    def as_dict(self, related=True, alternate_titles=True):
        return {
            'geonameid': self.geonameid,
            'name': self.name,
            'title': self.title,
            'ascii_title': self.ascii_title,
            'short_title': self.short_title,
            'latitude': unicode(self.latitude),
            'longitude': unicode(self.longitude),
            'fclass': self.fclass,
            'fcode': self.fcode,
            'country': self.country_id,
            'cc2': self.cc2,
            'admin1': self.admin1,
            'admin2': self.admin2,
            'admin3': self.admin3,
            'admin4': self.admin4,
            'is_country': bool(self.has_country),
            'is_admin1': bool(self.has_admin1code),
            'is_admin2': bool(self.has_admin2code),
            'population': self.population,
            'elevation': self.elevation,
            'dem': self.dem,
            'timezone': self.timezone,
            'moddate': self.moddate.strftime('%Y-%m-%d') if self.moddate else None,
            'related': dict([(k, v.as_dict(related=False, alternate_titles=False))
                for (k, v) in self.related_geonames().items()]) if related else [],
            'alternate_titles': [{
                'lang': a.lang,
                'title': a.title,
                'is_preferred_name': a.is_preferred_name,
                'is_short_name': a.is_short_name,
                'is_colloquial': a.is_colloquial,
                'is_historic': a.is_historic,
                } for a in self.alternate_titles] if alternate_titles else []
            }

    @classmethod
    def get(cls, name):
        return cls.query.filter_by(name=name).one_or_none()

    @classmethod
    def get_by_title(cls, titles, lang=None):
        results = set()
        if isinstance(titles, basestring):
            titles = [titles]
        for title in titles:
            if lang:
                results.update([r.geoname for r in GeoAltName.query.filter(
                    db.func.lower(GeoAltName.title) == title.lower(), GeoAltName.lang == lang).all() if r.geoname])
            else:
                results.update([r.geoname for r in GeoAltName.query.filter(
                    db.func.lower(GeoAltName.title) == title.lower()).all() if r.geoname])
        return sorted(list(results), key=lambda g: ({'A': 1, 'P': 2}.get(g.fclass, 0), g.population), reverse=True)


class GeoAltName(BaseMixin, db.Model):
    __tablename__ = 'geo_alt_name'

    geonameid = db.Column(None, db.ForeignKey('geo_name.id'), nullable=False)
    geoname = db.relationship(GeoName, backref=db.backref('alternate_titles', cascade='all, delete-orphan'))
    lang = db.Column(db.Unicode(7), nullable=True)
    title = db.Column(db.Unicode(200), nullable=False)
    is_preferred_name = db.Column(db.Boolean, nullable=False)
    is_short_name = db.Column(db.Boolean, nullable=False)
    is_colloquial = db.Column(db.Boolean, nullable=False)
    is_historic = db.Column(db.Boolean, nullable=False)


class GeoAdmin1Code(BaseMixin, db.Model):
    __tablename__ = 'geo_admin1_code'

    geonameid = db.synonym('id')
    geoname = db.relationship('GeoName', uselist=False,
        primaryjoin='GeoAdmin1Code.id == foreign(GeoName.id)',
        backref='has_admin1code')
    title = db.Column(db.Unicode(200))
    ascii_title = db.Column(db.Unicode(200))
    country_id = db.Column('country', db.CHAR(2), db.ForeignKey('geo_country_info.iso_alpha2'))
    country = db.relationship('GeoCountryInfo')
    admin1_code = db.Column(db.Unicode(7))

    def __repr__(self):
        return '<GeoAdmin1Code %d "%s">' % (self.geonameid, self.ascii_title)


class GeoAdmin2Code(BaseMixin, db.Model):
    __tablename__ = 'geo_admin2_code'

    geonameid = db.synonym('id')
    geoname = db.relationship('GeoName', uselist=False,
        primaryjoin='GeoAdmin2Code.id == foreign(GeoName.id)',
        backref='has_admin2code')
    title = db.Column(db.Unicode(200))
    ascii_title = db.Column(db.Unicode(200))
    country_id = db.Column('country', db.CHAR(2), db.ForeignKey('geo_country_info.iso_alpha2'))
    country = db.relationship('GeoCountryInfo')
    admin1_code = db.Column(db.Unicode(7))
    admin2_code = db.Column(db.Unicode(23))

    def __repr__(self):
        return '<GeoAdmin2Code %d "%s">' % (self.geonameid, self.ascii_title)
