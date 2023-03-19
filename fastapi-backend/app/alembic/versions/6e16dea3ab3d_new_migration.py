"""New Migration

Revision ID: 6e16dea3ab3d
Revises: 4c88f58f16a6
Create Date: 2023-02-17 22:50:24.468975

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e16dea3ab3d'
down_revision = '4c88f58f16a6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'author', ['name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'author', type_='unique')
    # ### end Alembic commands ###
