"""Renaming students to scholars

Revision ID: bc93561491b8
Revises: 
Create Date: 2025-03-12 01:37:16.947036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc93561491b8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    pass


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    pass
