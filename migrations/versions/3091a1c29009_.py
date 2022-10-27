"""empty message

Revision ID: 3091a1c29009
Revises: 50c7707d6949
Create Date: 2022-10-04 10:52:30.677283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3091a1c29009'
down_revision = '50c7707d6949'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('price', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###