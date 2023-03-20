"""question and answer combination

Revision ID: 5a552a57613e
Revises: add902d9a541
Create Date: 2023-03-20 12:36:43.016212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a552a57613e'
down_revision = 'add902d9a541'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('answer', sa.String(), nullable=False),
    sa.Column('isCorrect', sa.Boolean(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('answer')
    # ### end Alembic commands ###
