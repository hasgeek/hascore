# -*- coding: utf-8 -*-
"""Geoname alt names

Revision ID: 2afdc94224f0
Revises: 4f1edd208ea5
Create Date: 2014-05-30 23:36:32.259252

"""

# revision identifiers, used by Alembic.
revision = '2afdc94224f0'
down_revision = '4f1edd208ea5'

from alembic import op
from sqlalchemy.dialects import postgresql
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'geo_alt_name',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('geonameid', sa.Integer(), nullable=False),
        sa.Column('lang', sa.Unicode(length=7), nullable=True),
        sa.Column('title', sa.Unicode(length=200), nullable=False),
        sa.Column('is_preferred_name', sa.Boolean(), nullable=False),
        sa.Column('is_short_name', sa.Boolean(), nullable=False),
        sa.Column('is_colloquial', sa.Boolean(), nullable=False),
        sa.Column('is_historic', sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(['geonameid'], ['geo_name.id']),
        sa.PrimaryKeyConstraint('id'),
    )
    op.drop_column('geo_name', 'alternate_titles')


def downgrade():
    op.add_column(
        'geo_name',
        sa.Column(
            'alternate_titles', postgresql.ARRAY(sa.VARCHAR(length=200)), nullable=True
        ),
    )
    op.drop_table('geo_alt_name')
