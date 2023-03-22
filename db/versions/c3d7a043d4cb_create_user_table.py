"""create user table

Revision ID: c3d7a043d4cb
Revises: 
Create Date: 2023-03-17 03:16:18.002579

"""
import enum
from alembic import op
from typing import Tuple
from sqlalchemy import Enum, Column, ForeignKey, Integer, String, func, TIMESTAMP

# revision identifiers, used by Alembic.
revision = 'c3d7a043d4cb'
down_revision = None
branch_labels = None
depends_on = None

class UserRole(enum.Enum):
    admin = 1
    user = 2

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
        'users',
        Column('id', Integer, primary_key=True),
        Column('name', String(50), nullable=False),
        Column('email', String(256), nullable=False, unique=True),
        Column('hashed_password', String(256), nullable=False),
        Column('role', Enum(UserRole)),
        *timestamps()
    )


def downgrade() -> None:
    op.drop_table('users')
