"""Fixed typos

Revision ID: cbc142fd5ae7
Revises: 8a0320b9ef4a
Create Date: 2023-09-04 12:36:03.559883

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cbc142fd5ae7'
down_revision: Union[str, None] = '8a0320b9ef4a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
