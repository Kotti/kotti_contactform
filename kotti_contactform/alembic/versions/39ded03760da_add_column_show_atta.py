"""add column show_attachment

Revision ID: 39ded03760da
Revises: None
Create Date: 2012-06-27 14:26:30.826076

"""

# revision identifiers, used by Alembic.
revision = '39ded03760da'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column


contact_form = table('contact_forms', column('show_attachment', sa.Boolean))


def upgrade():
    op.add_column('contact_forms', sa.Column('show_attachment', sa.Boolean))
    op.execute(contact_form.update().values({'show_attachment':True}))
    op.alter_column('contact_forms', 'show_attachment', nullable=False)


def downgrade():
    op.drop_column('contact_forms', 'show_attachment')
