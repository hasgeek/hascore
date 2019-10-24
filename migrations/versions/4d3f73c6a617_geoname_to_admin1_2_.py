# -*- coding: utf-8 -*-
"""GeoName to admin1/2 foreign key references

Revision ID: 4d3f73c6a617
Revises: f18dfde53fd
Create Date: 2014-11-07 01:57:36.785298

"""

# revision identifiers, used by Alembic.
revision = '4d3f73c6a617'
down_revision = 'f18dfde53fd'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('geo_name', sa.Column('admin1_id', sa.Integer(), nullable=True))
    op.add_column('geo_name', sa.Column('admin2_id', sa.Integer(), nullable=True))

    # TODO by user:
    # >>> for geoname in models.GeoName.query:
    # ...   geoname.admin1code = geoname.admin1_ref
    # ...   geoname.admin2code = geoname.admin2_ref
    # ...
    # >>> db.session.commit
    # (or just reimport all geonames)


def downgrade():
    op.drop_column('geo_name', 'admin2_id')
    op.drop_column('geo_name', 'admin1_id')
