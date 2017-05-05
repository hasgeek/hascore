"""Init

Revision ID: 48e05db3081f
Revises: None
Create Date: 2014-05-23 00:19:42.037970

"""

# revision identifiers, used by Alembic.
revision = '48e05db3081f'
down_revision = None

from alembic import op
import sqlalchemy as sa
from coaster.sqlalchemy import JsonDict


def upgrade():
    op.create_table('networklink',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('url', sa.Unicode(length=250), nullable=True),
        sa.Column('sep', sa.Boolean(), nullable=True),
        sa.Column('seq', sa.SmallInteger(), nullable=False),
        sa.Column('parent_id', sa.Integer(), nullable=True),
        sa.Column('name', sa.Unicode(length=250), nullable=False),
        sa.Column('title', sa.Unicode(length=250), nullable=False),
        sa.ForeignKeyConstraint(['parent_id'], ['networklink.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
        )
    op.create_table('user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('username', sa.Unicode(length=80), nullable=True),
        sa.Column('lastuser_token_scope', sa.Unicode(length=250), nullable=True),
        sa.Column('lastuser_token_type', sa.Unicode(length=250), nullable=True),
        sa.Column('userid', sa.String(length=22), nullable=False),
        sa.Column('lastuser_token', sa.String(length=22), nullable=True),
        sa.Column('fullname', sa.Unicode(length=80), nullable=False),
        sa.Column('email', sa.Unicode(length=80), nullable=True),
        sa.Column('userinfo', JsonDict(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('lastuser_token'),
        sa.UniqueConstraint('userid'),
        sa.UniqueConstraint('username')
        )


def downgrade():
    op.drop_table('user')
    op.drop_table('networklink')
