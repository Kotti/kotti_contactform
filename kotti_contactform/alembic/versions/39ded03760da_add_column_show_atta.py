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


def upgrade():
    op.add_column('contact_forms', sa.Column('show_attachment', sa.Boolean))


def downgrade():
    op.drop_column('contact_forms', 'show_attachment')
