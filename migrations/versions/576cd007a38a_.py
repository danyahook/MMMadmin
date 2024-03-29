"""empty message

Revision ID: 576cd007a38a
Revises: 253cc9a1fee0
Create Date: 2020-04-01 19:47:47.852732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '576cd007a38a'
down_revision = '253cc9a1fee0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('percent',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('per_name', sa.VARCHAR(length=128), nullable=False),
    sa.Column('per_count', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('percent')
    # ### end Alembic commands ###
