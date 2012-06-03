# -*- coding: utf-8 -*-

from coaster import makename
from hascore.models import db, BaseMixin

__all__ = ['Tag']


class Tag(BaseMixin, db.Model):
    __tablename__ = 'tag'
    name = db.Column(db.Unicode(80), unique=True, nullable=False)
    title = db.Column(db.Unicode(80), unique=True, nullable=False)

    @classmethod
    def get(cls, title):
        tag = cls.query.filter_by(title=title).first()
        if tag:
            return tag
        else:
            name = makename(title)
            # Is this name already in use? If yes, return it
            tag = cls.query.filter_by(name=name).first()
            if tag:
                return tag
            else:
                tag = Tag(name=name, title=title)
                db.session.add(tag)
                return tag

    def rename(self, title):
        name = makename(title)
        if self.query.filter_by(name=name).first() is not None:
            raise ValueError(u"Name already in use")
        else:
            self.name = name
            self.title = title
