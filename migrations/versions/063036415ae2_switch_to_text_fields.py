"""Switch to text fields

Revision ID: 063036415ae2
Revises: 26538acc5d0b
Create Date: 2019-10-30 12:14:15.543076

"""

# revision identifiers, used by Alembic.
revision = '063036415ae2'
down_revision = '26538acc5d0b'

from alembic import op
import sqlalchemy as sa

text_columns = [
    # Table name, column name, column length (for downgrade)
    ('geo_country_info', 'capital', 200),
    ('geo_country_info', 'currency_name', 13),
    ('geo_country_info', 'postal_code_format', 55),
    ('geo_country_info', 'postal_code_regex', 155),
    ('geo_admin1_code', 'title', 200),
    ('geo_admin1_code', 'ascii_title', 200),
    ('geo_admin1_code', 'admin1_code', 8),
    ('geo_admin2_code', 'title', 200),
    ('geo_admin2_code', 'ascii_title', 200),
    ('geo_admin2_code', 'admin1_code', 8),
    ('geo_admin2_code', 'admin2_code', 23),
    ('geo_name', 'ascii_title', 200),
    ('geo_name', 'fcode', 10),
    ('geo_name', 'cc2', 60),
    ('geo_name', 'admin1', 20),
    ('geo_name', 'admin2', 80),
    ('geo_name', 'admin3', 20),
    ('geo_name', 'admin4', 20),
    ('geo_name', 'timezone', 40),
    ('geo_alt_name', 'lang', 7),
    ('geo_alt_name', 'title', 200),
]


def upgrade():
    for table, column, length in text_columns:
        op.alter_column(
            table, column, type_=sa.UnicodeText(), existing_type=sa.Unicode(length)
        )


def downgrade():
    for table, column, length in reversed(text_columns):
        op.alter_column(
            table, column, type_=sa.Unicode(length), existing_type=sa.UnicodeText()
        )
