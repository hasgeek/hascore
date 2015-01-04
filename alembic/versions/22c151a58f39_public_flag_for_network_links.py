"""Public flag for network links

Revision ID: 22c151a58f39
Revises: 17e97c01b387
Create Date: 2015-01-04 22:06:28.133153

"""

# revision identifiers, used by Alembic.
revision = '22c151a58f39'
down_revision = '17e97c01b387'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('networklink', sa.Column('public', sa.Boolean(), nullable=False, server_default="1"))
    op.alter_column('networklink', 'public', server_default=None)


def downgrade():
    op.drop_column('networklink', 'public')
