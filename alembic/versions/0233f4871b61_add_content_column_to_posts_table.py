"""add content column to posts table

Revision ID: 0233f4871b61
Revises: b0af9e6eec37
Create Date: 2022-10-26 20:07:09.583969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0233f4871b61'
down_revision = 'b0af9e6eec37'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    
    pass


def downgrade() -> None:
    op.drop_column("posts","content")
    pass
