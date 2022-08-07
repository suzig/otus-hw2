"""empty message

Revision ID: 38bb177c3897
Revises: 
Create Date: 2022-08-04 23:09:00.000800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38bb177c3897'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('fullname', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###