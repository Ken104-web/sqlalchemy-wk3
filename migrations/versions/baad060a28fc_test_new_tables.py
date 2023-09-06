"""test new tables

Revision ID: baad060a28fc
Revises: 55d8660c5bfd
Create Date: 2023-09-06 12:21:37.531888

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'baad060a28fc'
down_revision: Union[str, None] = '55d8660c5bfd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
