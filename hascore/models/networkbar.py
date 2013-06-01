# -*- coding: utf-8 -*-

from sqlalchemy.ext.orderinglist import ordering_list
from . import db, BaseNameMixin

__all__ = ['NetworkLink', 'networkbar_data']


class NetworkLink(BaseNameMixin, db.Model):
    __tablename__ = 'networklink'

    #: URL to link to
    url = db.Column(db.Unicode(250), nullable=True)
    #: Is this a menu section separator?
    sep = db.Column(db.Boolean, default=False)
    #: Sequence number for ordering
    seq = db.Column(db.SmallInteger, nullable=False)
    #: Parent for submenus
    parent_id = db.Column(None, db.ForeignKey('networklink.id'), nullable=True)
    parent = db.relationship('NetworkLink', remote_side='NetworkLink.id',
        backref=db.backref('children', order_by=seq, collection_class=ordering_list('seq')))

    def __repr__(self):
        return u'<NetworkLink {seq} {name} "{title}">'.format(
            seq=self.seq, name=self.name, title=self.title)


def dictify_networklink(link):
    return {'name': link.name,
            'title': link.title,
            'url': link.url,
            'sep': link.sep,
            'children': [dictify_networklink(l) for l in link.children] if link.children else None
        }


def networkbar_data():
    # Load all links into SQLAlchemy identity map but loop through just the top-level.
    # Subitems will be retrieved from the identity map without additional queries.
    return [dictify_networklink(l) for l in NetworkLink.query.all() if l.parent is None]
