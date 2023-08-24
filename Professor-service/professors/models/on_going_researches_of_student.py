from professors import db

class OnGoingResearchOfStudentModel(db.Model):
    """
    primary key: profile_id and on_going_research_id
    """

    __tablename__ = 'on_going_research_of_student'

    profile_id = db.Column(db.Integer, primary_key=True, nullable=False)
    on_going_research_id = db.Column(db.Integer, db.ForeignKey('on_going_research.id'), primary_key=True, nullable=False)


    def json(self):
        return {'profile_id': self.profile_id, 'on_going_research_id': self.on_going_research_id}