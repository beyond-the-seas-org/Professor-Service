from professors import db

class ProfessorModel(db.Model):
    """
    primary key: id
    other fields: name, email, university_id, location_id
    """

    __tablename__ = 'professor'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=True)
    university_id = db.Column(db.Integer, db.ForeignKey('university.id'), nullable=True)
    location_id = db.Column(db.Integer, nullable=True)

    def json(self):
        return {'id': self.id, 'name': self.name, 'email': self.email, 'university_id': self.university_id, 'location_id': self.location_id}