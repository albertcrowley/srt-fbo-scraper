"""add publish_date to notice

Revision ID: 5ea574c26608
Revises: 48a836bedb3f
Create Date: 2020-02-07 10:29:25.835136

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import engine_from_config
from sqlalchemy.engine import reflection


# revision identifiers, used by Alembic.
revision = '5ea574c26608'
down_revision = '48a836bedb3f'
branch_labels = None
depends_on = None


def table_has_column(table, column):
    """Check table has a column. Usefule before trying to add or drop the column
    in an alembic migration file.

    Arguments:
        table {str} -- name of the table
        column {str} -- name of the column

    Returns:
        [bool] -- True if the table has the column. False otherwise.
    """
    config = op.get_context().config
    engine = engine_from_config(
        config.get_section(config.config_ini_section), prefix='sqlalchemy.')
    insp = reflection.Inspector.from_engine(engine)
    has_column = False
    for col in insp.get_columns(table):
        if column not in col['name']:
            continue
        has_column = True

    return has_column


def upgrade():
    if table_has_column('notice', 'publish_date'):
        pass
    else:
        op.add_column('notice', sa.Column('publish_date',
                                          sa.DateTime,
                                          nullable=True))


def downgrade():
    op.drop_column('notice', 'publish_date')

