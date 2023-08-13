from professors import db

class OnGoingResearchOfProfessorModel(db.Model):
    """
    primary key: professor_id and on_going_research_id
    """

    __tablename__ = 'on_going_research_of_professor'

    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), primary_key=True, nullable=False)
    on_going_research_id = db.Column(db.Integer, db.ForeignKey('on_going_research.id'), primary_key=True, nullable=False)


    def json(self):
        return {'professor_id': self.professor_id, 'on_going_research_id': self.on_going_research_id}