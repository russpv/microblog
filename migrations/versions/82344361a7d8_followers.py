"""followers

Revision ID: 82344361a7d8
Revises: 9dc0c7750a24
Create Date: 2019-08-22 16:47:38.197369

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82344361a7d8'
down_revision = '9dc0c7750a24'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
