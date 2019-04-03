''"""empty message

Revision ID: migration.py
Revises: 
Create Date: 2019-04-01 18:20:56.930522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'migration.py'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_class_id'), 'class', ['id'], unique=False)
    op.create_index(op.f('ix_student_id'), 'student', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_student_id'), table_name='student')
    op.drop_index(op.f('ix_class_id'), table_name='class')
    # ### end Alembic commands ###