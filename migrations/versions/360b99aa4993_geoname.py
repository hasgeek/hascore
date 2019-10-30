# -*- coding: utf-8 -*-
"""Geoname

Revision ID: 360b99aa4993
Revises: 48e05db3081f
Create Date: 2014-05-23 00:52:20.711061

"""

# revision identifiers, used by Alembic.
revision = '360b99aa4993'
down_revision = '48e05db3081f'

from alembic import op
from sqlalchemy.dialects import postgresql
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'geo_country_info',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('iso_alpha2', sa.CHAR(length=2), nullable=True),
        sa.Column('iso_alpha3', sa.CHAR(length=3), nullable=True),
        sa.Column('iso_numeric', sa.Integer(), nullable=True),
        sa.Column('fips_code', sa.Unicode(length=3), nullable=True),
        sa.Column('capital', sa.Unicode(length=200), nullable=True),
        sa.Column('area_in_sqkm', sa.Numeric(), nullable=True),
        sa.Column('population', sa.BigInteger(), nullable=True),
        sa.Column('continent', sa.CHAR(length=2), nullable=True),
        sa.Column('tld', sa.Unicode(length=3), nullable=True),
        sa.Column('currency_code', sa.CHAR(length=3), nullable=True),
        sa.Column('currency_name', sa.Unicode(length=13), nullable=True),
        sa.Column('phone', sa.Unicode(length=16), nullable=True),
        sa.Column('postal_code_format', sa.Unicode(length=55), nullable=True),
        sa.Column('postal_code_regex', sa.Unicode(length=155), nullable=True),
        sa.Column(
            'languages',
            postgresql.ARRAY(sa.Unicode(length=7), dimensions=1),
            nullable=True,
        ),
        sa.Column(
            'neighbours',
            postgresql.ARRAY(sa.CHAR(length=2), dimensions=1),
            nullable=True,
        ),
        sa.Column('equivalent_fips_code', sa.Unicode(length=3), nullable=True),
        sa.Column('name', sa.Unicode(length=250), nullable=False),
        sa.Column('title', sa.Unicode(length=250), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('iso_alpha2'),
        sa.UniqueConstraint('iso_alpha3'),
        sa.UniqueConstraint('name'),
    )
    op.create_table(
        'geo_name',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('ascii_title', sa.String(length=200), nullable=True),
        sa.Column(
            'alternate_titles',
            postgresql.ARRAY(sa.Unicode(length=200), dimensions=1),
            nullable=True,
        ),
        sa.Column('latitude', sa.Numeric(), nullable=True),
        sa.Column('longitude', sa.Numeric(), nullable=True),
        sa.Column('fclass', sa.CHAR(length=1), nullable=True),
        sa.Column('fcode', sa.Unicode(length=10), nullable=True),
        sa.Column('country', sa.Unicode(length=2), nullable=True),
        sa.Column('cc2', sa.Unicode(length=60), nullable=True),
        sa.Column('admin1', sa.Unicode(length=20), nullable=True),
        sa.Column('admin2', sa.Unicode(length=80), nullable=True),
        sa.Column('admin3', sa.Unicode(length=20), nullable=True),
        sa.Column('admin4', sa.Unicode(length=20), nullable=True),
        sa.Column('population', sa.BigInteger(), nullable=True),
        sa.Column('elevation', sa.Integer(), nullable=True),
        sa.Column('dem', sa.Integer(), nullable=True),
        sa.Column('timezone', sa.Unicode(length=40), nullable=True),
        sa.Column('moddate', sa.Date(), nullable=True),
        sa.Column('name', sa.Unicode(length=250), nullable=False),
        sa.Column('title', sa.Unicode(length=250), nullable=False),
        sa.ForeignKeyConstraint(['country'], ['geo_country_info.iso_alpha2']),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name'),
    )
    op.create_table(
        'geo_alt_name',
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('iso_language', sa.Unicode(length=7), nullable=True),
        sa.Column('alternate_name', sa.Unicode(length=200), nullable=True),
        sa.Column('is_preferred_name', sa.Boolean(), nullable=True),
        sa.Column('is_short_name', sa.Boolean(), nullable=True),
        sa.Column('is_colloquial', sa.Boolean(), nullable=True),
        sa.Column('is_historic', sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(['id'], ['geo_name.id']),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade():
    op.drop_table('geo_alt_name')
    op.drop_table('geo_name')
    op.drop_table('geo_country_info')
