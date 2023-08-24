from professors import db

class ProfessorAreaOfInterestModel(db.Model):
    """
    primary key: professor_id and area_of_interest_id
    """

    __tablename__ = 'professor_area_of_interest'

    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), primary_key=True, nullable=False)
    area_of_interest_id = db.Column(db.Integer, primary_key=True, nullable=False)


    def json(self):
        return {'professor_id': self.professor_id, 'area_of_interest_id': self.area_of_interest_id}