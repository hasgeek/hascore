# -*- coding: utf-8 -*-

from hascore import app
from hascore.models import db, BaseMixin, BaseNameMixin
from hascore.models.user import User, default_user


class EventSeries(BaseNameMixin, db.Model):
    __tablename__ = 'event_series'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, default=default_user)
    user = db.relationship(User, primaryjoin=user_id == User.id,
        backref = db.backref('event_series', cascade='all, delete-orphan'))
    website = db.Column(db.Unicode(250), nullable=True)


class EventEdition(BaseNameMixin, db.Model):
    __tablename__ = 'event_edition'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, default=default_user)
    user = db.relationship(User, primaryjoin=user_id == User.id,
        backref = db.backref('editions', cascade='all, delete-orphan'))
    event_series_id = db.Column(db.Integer, db.ForeignKey('event_series.id'), nullable=False)
    event_series = db.relationship(EventSeries, primaryjoin=event_series_id == EventSeries.id,
        backref = db.backref('editions', cascade="all, delete-orphan"))
    tagline = db.Column(db.Unicode(250), nullable=False)
    description = db.Column(db.Text, default=u'', nullable=False)
    description_html = db.Column(db.Text, default=u'', nullable=False)
    datelocation = db.Column(db.Unicode(50), default=u'', nullable=False)
    website = db.Column(db.Unicode(250), nullable=True)
    public = db.Column(db.Boolean, nullable=False, default=False)


class EventRoom(BaseNameMixin, db.Model):
    __tablename__ = 'event_room'
    event_edition_id = db.Column(db.Integer, db.ForeignKey('event_edition.id'), nullable=False)
    event_edition = db.relationship(EventEdition, primaryjoin=event_edition_id == EventEdition.id,
        backref = ('rooms', cascade='all, delete-orphan'))


class EventSlot(BaseMixin, db.Model):
    __tablename__ = 'event_slot'


class EventSessionType(BaseMixin, db.Model):
    __tablename__ = 'event_session_type'


class EventSession(BaseNameMixin, db.Model):
    __tablename__ = 'event_session'
