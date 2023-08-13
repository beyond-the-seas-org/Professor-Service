from professors import db 

class ProfessorFeedbackModel(db.Model):
    """
    primary key: id
    other fields: professor_id, profile_id, feedback
    """

    __tablename__ = 'professor_feedback'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    profile_id = db.Column(db.Integer, nullable=False)
    feedback = db.Column(db.String(1000), nullable=False)


    def json(self):
        return {'id': self.id, 'professor_id': self.professor_id, 'profile_id': self.profile_id, 'feedback': self.feedback}