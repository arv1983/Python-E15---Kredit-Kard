"""Create user

Revision ID: 97035e8e22de
Revises: 
Create Date: 2021-06-30 11:21:08.068383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97035e8e22de'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.Text(), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###