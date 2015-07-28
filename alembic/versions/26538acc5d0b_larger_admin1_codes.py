"""Larger admin1 codes

Revision ID: 26538acc5d0b
Revises: 3cacfc614ecd
Create Date: 2015-07-28 14:28:38.042314

"""

# revision identifiers, used by Alembic.
revision = '26538acc5d0b'
down_revision = '3cacfc614ecd'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column('geo_admin1_code', 'admin1_code', type_=sa.Unicode(8), existing_type=sa.Unicode(7))
    op.alter_column('geo_admin2_code', 'admin1_code', type_=sa.Unicode(8), existing_type=sa.Unicode(7))


def downgrade():
    op.alter_column('geo_admin2_code', 'admin1_code', type_=sa.Unicode(7), existing_type=sa.Unicode(8))
    op.alter_column('geo_admin1_code', 'admin1_code', type_=sa.Unicode(7), existing_type=sa.Unicode(8))
