# -*- coding: utf-8 -*-
"""Use UserBase2

Revision ID: 3cacfc614ecd
Revises: 22c151a58f39
Create Date: 2015-01-04 23:53:11.991297

"""

# revision identifiers, used by Alembic.
revision = '3cacfc614ecd'
down_revision = '22c151a58f39'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column(
        'user', sa.Column('status', sa.Integer(), nullable=False, server_default='0')
    )
    op.alter_column('user', 'status', server_default=None)


def downgrade():
    op.drop_column('user', 'status')
