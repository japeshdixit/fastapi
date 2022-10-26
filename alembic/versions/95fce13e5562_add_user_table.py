"""add user table

Revision ID: 95fce13e5562
Revises: 0233f4871b61
Create Date: 2022-10-26 20:15:15.438601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95fce13e5562'
down_revision = '0233f4871b61'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                    server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
