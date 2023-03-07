"""empty message

Revision ID: bcb988533623
Revises: 
Create Date: 2023-03-06 15:32:52.503045

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcb988533623'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('input', sa.String(length=200), nullable=False),
    sa.Column('station', sa.String(length=200), nullable=True),
    sa.Column('direction', sa.String(length=200), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('success', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question')
    # ### end Alembic commands ###
