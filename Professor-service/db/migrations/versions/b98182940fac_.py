"""empty message

Revision ID: b98182940fac
Revises: 
Create Date: 2023-08-14 01:23:17.706329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b98182940fac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('publication',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=500), nullable=False),
    sa.Column('doi', sa.String(length=500), nullable=False),
    sa.Column('link', sa.String(length=500), nullable=True),
    sa.Column('abstract', sa.String(length=5000), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('venue', sa.String(length=500), nullable=True),
    sa.Column('citation', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('doi'),
    sa.UniqueConstraint('title')
    )
    op.create_table('university_rank',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('rank', sa.Integer(), nullable=True),
    sa.Column('area_of_interest_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('professor',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('university_id', sa.Integer(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['university_id'], ['university_rank.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('professor_publication',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('publication_id', sa.Integer(), nullable=False),
    sa.Column('number_of_citations', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['publication_id'], ['publication.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('funding',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('funding_post', sa.String(length=1000), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('requirement_description', sa.String(length=1000), nullable=False),
    sa.Column('num_of_slot', sa.Integer(), nullable=False),
    sa.Column('professor_id', sa.Integer(), nullable=False),
    sa.Column('availability', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['professor_id'], ['professor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('professor_area_of_interest',
    sa.Column('professor_id', sa.Integer(), nullable=False),
    sa.Column('area_of_interest_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['professor_id'], ['professor.id'], ),
    sa.PrimaryKeyConstraint('professor_id', 'area_of_interest_id')
    )
    op.create_table('professor_feedback',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('professor_id', sa.Integer(), nullable=False),
    sa.Column('profile_id', sa.Integer(), nullable=False),
    sa.Column('feedback', sa.String(length=1000), nullable=False),
    sa.ForeignKeyConstraint(['professor_id'], ['professor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('professor_website_link',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('professor_id', sa.Integer(), nullable=False),
    sa.Column('website_link', sa.String(length=500), nullable=False),
    sa.Column('website_type', sa.String(length=200), nullable=False),
    sa.ForeignKeyConstraint(['professor_id'], ['professor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('on_going_research',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('research_field', sa.String(length=200), nullable=False),
    sa.Column('research_topic', sa.String(length=200), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=False),
    sa.Column('num_of_students', sa.Integer(), nullable=True),
    sa.Column('research_desc_link', sa.String(length=500), nullable=True),
    sa.Column('funding_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['funding_id'], ['funding.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('on_going_research_of_professor',
    sa.Column('professor_id', sa.Integer(), nullable=False),
    sa.Column('on_going_research_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['on_going_research_id'], ['on_going_research.id'], ),
    sa.ForeignKeyConstraint(['professor_id'], ['professor.id'], ),
    sa.PrimaryKeyConstraint('professor_id', 'on_going_research_id')
    )
    op.create_table('on_going_research_of_student',
    sa.Column('profile_id', sa.Integer(), nullable=False),
    sa.Column('on_going_research_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['on_going_research_id'], ['on_going_research.id'], ),
    sa.PrimaryKeyConstraint('profile_id', 'on_going_research_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('on_going_research_of_student')
    op.drop_table('on_going_research_of_professor')
    op.drop_table('on_going_research')
    op.drop_table('professor_website_link')
    op.drop_table('professor_feedback')
    op.drop_table('professor_area_of_interest')
    op.drop_table('funding')
    op.drop_table('professor_publication')
    op.drop_table('professor')
    op.drop_table('university_rank')
    op.drop_table('publication')
    # ### end Alembic commands ###