"""add email and date_of_birth to users

Revision ID: 22aa8055d928
Revises: bcf4efd6d386
Create Date: 2025-03-23 23:26:11.011375
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22aa8055d928'
down_revision: Union[str, None] = 'bcf4efd6d386'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Add columns and a named unique constraint
    op.add_column('users', sa.Column(
        'email', sa.String(length=255), nullable=False))
    op.add_column('users', sa.Column(
        'date_of_birth', sa.Date(), nullable=True))
    op.create_unique_constraint('uq_users_email', 'users', [
                                'email'])  # Named constraint


def downgrade() -> None:
    """Downgrade schema."""
    # Drop the named constraint and columns
    # Reference the named constraint
    op.drop_constraint('uq_users_email', 'users', type_='unique')
    op.drop_column('users', 'date_of_birth')
    op.drop_column('users', 'email')
