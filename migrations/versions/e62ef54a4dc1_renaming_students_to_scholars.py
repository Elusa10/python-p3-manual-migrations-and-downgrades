"""Renaming students to scholars

Revision ID: e62ef54a4dc1
Revises: bc93561491b8
Create Date: 2025-03-12 01:47:35.836674

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e62ef54a4dc1'
down_revision = 'bc93561491b8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    pass


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    pass
