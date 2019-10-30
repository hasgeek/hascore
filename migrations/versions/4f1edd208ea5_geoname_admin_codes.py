# -*- coding: utf-8 -*-
"""Geoname admin codes

Revision ID: 4f1edd208ea5
Revises: 360b99aa4993
Create Date: 2014-05-30 17:24:33.702247

"""

# revision identifiers, used by Alembic.
revision = '4f1edd208ea5'
down_revision = '360b99aa4993'

from alembic import op
from sqlalchemy.dialects import postgresql
import sqlalchemy as sa


def upgrade():
    op.alter_column('geo_name', 'country', type_=sa.CHAR(length=2))
    op.create_table(
        'geo_admin1_code',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('title', sa.Unicode(length=200), nullable=True),
        sa.Column('ascii_title', sa.Unicode(length=200), nullable=True),
        sa.Column('country', sa.CHAR(length=2), nullable=True),
        sa.Column('admin1_code', sa.Unicode(7), nullable=True),
        sa.ForeignKeyConstraint(['country'], ['geo_country_info.iso_alpha2']),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'geo_admin2_code',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('title', sa.Unicode(length=200), nullable=True),
        sa.Column('ascii_title', sa.Unicode(length=200), nullable=True),
        sa.Column('country', sa.CHAR(length=2), nullable=True),
        sa.Column('admin1_code', sa.Unicode(7), nullable=True),
        sa.Column('admin2_code', sa.Unicode(23), nullable=True),
        sa.ForeignKeyConstraint(['country'], ['geo_country_info.iso_alpha2']),
        sa.PrimaryKeyConstraint('id'),
    )
    op.drop_table('geo_alt_name')


def downgrade():
    op.create_table(
        'geo_alt_name',
        sa.Column(
            'created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False
        ),
        sa.Column(
            'updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False
        ),
        sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column(
            'iso_language', sa.VARCHAR(length=7), autoincrement=False, nullable=True
        ),
        sa.Column(
            'alternate_name', sa.VARCHAR(length=200), autoincrement=False, nullable=True
        ),
        sa.Column(
            'is_preferred_name', sa.BOOLEAN(), autoincrement=False, nullable=True
        ),
        sa.Column('is_short_name', sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.Column('is_colloquial', sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.Column('is_historic', sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(['id'], [u'geo_name.id'], name=u'geo_alt_name_id_fkey'),
        sa.PrimaryKeyConstraint('id', name=u'geo_alt_name_pkey'),
    )
    op.drop_table('geo_admin2_code')
    op.drop_table('geo_admin1_code')
    op.alter_column('geo_name', 'country', type_=sa.VARCHAR(length=2))
