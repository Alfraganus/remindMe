"""create users  table

Revision ID: ad0aea46bde8
Revises: c61fe5979bed
Create Date: 2023-10-28 15:21:23.605389

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad0aea46bde8'
down_revision: Union[str, None] = 'c61fe5979bed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(255), nullable=False),
        sa.Column('name', sa.String(255)),
        sa.Column('surname', sa.String(255)),
        sa.Column('password', sa.String(500)),
        sa.Column('is_active', sa.Boolean()),
    )


def downgrade() -> None:
    op.drop_table('users')
