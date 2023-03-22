"""create post table

Revision ID: 8e8a6a51567f
Revises: c3d7a043d4cb
Create Date: 2023-03-17 03:58:59.103160

"""
from alembic import op
from typing import Tuple
from sqlalchemy import Enum, Column, ForeignKey, Integer, String, func, TIMESTAMP

# revision identifiers, used by Alembic.
revision = '8e8a6a51567f'
down_revision = 'c3d7a043d4cb'
branch_labels = None
depends_on = None

def timestamps() -> Tuple[Column, Column]:
    return (
        Column(
            "created_at",
            TIMESTAMP(timezone=True),
            nullable=False,
            server_default=func.now(),
        ),
        Column(
            "updated_at",
            TIMESTAMP(timezone=True),
            nullable=False,
            server_default=func.now(),
            onupdate=func.current_timestamp(),
        ),
    )

def upgrade() -> None:
    op.create_table(
        'posts',
        Column('id', Integer, primary_key=True),
        Column('title', String(256), nullable=False),
        Column('content', String(256)),
        Column('owner_id', Integer, ForeignKey('users.id'), index=True),
        *timestamps()
    )


def downgrade() -> None:
    op.drop_table('posts')
