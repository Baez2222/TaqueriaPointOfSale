"""added email to users

Revision ID: 566c7ec0c312
Revises: 9eac5a034bad
Create Date: 2020-12-13 14:04:47.923556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '566c7ec0c312'
down_revision = '9eac5a034bad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=60), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###