"""add_history_table

Revision ID: f5f4dea64453
Revises: d2df7d213bed
Create Date: 2024-03-29 09:06:49.187487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5f4dea64453'
down_revision = 'd2df7d213bed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_time', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('input_msg', sa.Text(), nullable=True),
    sa.Column('label', sa.Enum('POSITIVE', 'NEGATIVE', name='label_types'), nullable=True),
    sa.Column('score', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('history')
    # ### end Alembic commands ###
