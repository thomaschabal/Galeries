"""empty message

Revision ID: 075d085d06a6
Revises: d4b4d55ae31e
Create Date: 2018-04-19 17:12:31.637072

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '075d085d06a6'
down_revision = 'd4b4d55ae31e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('cover_image_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'events', 'files', ['cover_image_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'events', type_='foreignkey')
    op.drop_column('events', 'cover_image_id')
    # ### end Alembic commands ###
