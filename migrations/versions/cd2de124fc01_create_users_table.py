"""Create users table

Revision ID: cd2de124fc01
Revises: d935d2f96209
Create Date: 2023-11-13 11:25:33.462335

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cd2de124fc01'
down_revision: Union[str, None] = 'd935d2f96209'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('crated_at', sa.DateTime(), nullable=True),
    sa.Column('refresh_token', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
