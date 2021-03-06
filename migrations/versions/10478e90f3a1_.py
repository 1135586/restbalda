"""empty message

Revision ID: 10478e90f3a1
Revises: None
Create Date: 2015-10-04 13:52:06.034302

"""

# revision identifiers, used by Alembic.
revision = '10478e90f3a1'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('scores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=20), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('scores')
    ### end Alembic commands ###
