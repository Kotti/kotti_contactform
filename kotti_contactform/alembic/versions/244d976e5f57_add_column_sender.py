"""add column sender

Revision ID: 244d976e5f57
Revises: None
Create Date: 2012-06-27 14:26:30.826076

"""

# revision identifiers, used by Alembic.
revision = '244d976e5f57'
down_revision = '39ded03760da'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column


contact_form = table('contact_forms', column('sender', sa.String(255)))


def upgrade():
    op.add_column('contact_forms', sa.Column('sender', sa.String(255)))
    op.execute(contact_form.update().values({'sender': 'mail@domain.com'}))
    op.alter_column('contact_forms', 'sender', nullable=False)


def downgrade():
    op.drop_column('contact_forms', 'sender')
