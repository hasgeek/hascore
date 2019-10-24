# -*- coding: utf-8 -*-
"""Text indexes

Revision ID: f18dfde53fd
Revises: 2afdc94224f0
Create Date: 2014-11-07 00:04:13.198196

"""

# revision identifiers, used by Alembic.
revision = 'f18dfde53fd'
down_revision = '2afdc94224f0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute(
        sa.DDL(
            "CREATE INDEX ix_geo_country_info_title ON geo_country_info (lower(title) text_pattern_ops);"
        )
    )
    op.execute(
        sa.DDL(
            "CREATE INDEX ix_geo_name_title ON geo_name (lower(title) text_pattern_ops);"
        )
    )
    op.execute(
        sa.DDL(
            "CREATE INDEX ix_geo_name_ascii_title ON geo_name (lower(ascii_title) text_pattern_ops);"
        )
    )
    op.execute(
        sa.DDL(
            "CREATE INDEX ix_geo_alt_name_title ON geo_alt_name (lower(title) text_pattern_ops);"
        )
    )
    op.create_index('ix_geo_alt_name_lang', 'geo_alt_name', ['lang'])


def downgrade():
    op.drop_index('ix_geo_alt_name_lang')
    op.drop_index('ix_geo_alt_name_title')
    op.drop_index('ix_geo_name_ascii_title')
    op.drop_index('ix_geo_name_title')
    op.drop_index('ix_geo_country_info_title')
