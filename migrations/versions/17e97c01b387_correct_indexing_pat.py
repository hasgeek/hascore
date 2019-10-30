# -*- coding: utf-8 -*-
"""Correct indexing pattern

Revision ID: 17e97c01b387
Revises: 4d3f73c6a617
Create Date: 2014-11-10 12:25:25.779476

"""

# revision identifiers, used by Alembic.
revision = '17e97c01b387'
down_revision = '4d3f73c6a617'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.drop_index('ix_geo_alt_name_title')
    op.drop_index('ix_geo_name_ascii_title')
    op.drop_index('ix_geo_name_title')
    op.drop_index('ix_geo_country_info_title')

    op.execute(
        sa.DDL(
            "CREATE INDEX ix_geo_country_info_title ON geo_country_info (lower(title) varchar_pattern_ops);"
        )
    )
    op.execute(
        sa.DDL(
            "CREATE INDEX ix_geo_name_title ON geo_name (lower(title) varchar_pattern_ops);"
        )
    )
    op.execute(
        sa.DDL(
            "CREATE INDEX ix_geo_name_ascii_title ON geo_name (lower(ascii_title) varchar_pattern_ops);"
        )
    )
    op.execute(
        sa.DDL(
            "CREATE INDEX ix_geo_alt_name_title ON geo_alt_name (lower(title) varchar_pattern_ops);"
        )
    )


def downgrade():
    op.drop_index('ix_geo_alt_name_title')
    op.drop_index('ix_geo_name_ascii_title')
    op.drop_index('ix_geo_name_title')
    op.drop_index('ix_geo_country_info_title')

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
