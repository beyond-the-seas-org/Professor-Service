from professors import db

class StudentAreaOfInterestModel(db.Model):
    """
    primary key: student_id and area_of_interest_id
    """

    __tablename__ = 'student_area_of_interest'

    student_id = db.Column(db.Integer, primary_key=True, nullable=False)
    area_of_interest_id = db.Column(db.Integer, primary_key=True, nullable=False)


    def json(self):
        return {'student_id': self.student_id, 'area_of_interest_id': self.area_of_interest_id}