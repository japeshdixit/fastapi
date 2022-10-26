"""add last colums to posts table

Revision ID: 18345d92415a
Revises: ee8c1c3d1241
Create Date: 2022-10-26 20:24:34.350892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18345d92415a'
down_revision = 'ee8c1c3d1241'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
