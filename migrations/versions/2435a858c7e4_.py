"""empty message

Revision ID: 2435a858c7e4
Revises: 64c967bb1124
Create Date: 2018-10-13 16:35:54.438588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2435a858c7e4'
down_revision = '64c967bb1124'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###
