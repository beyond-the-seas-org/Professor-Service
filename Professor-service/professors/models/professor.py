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
    university_id = db.Column(db.Integer, db.ForeignKey('university_rank.id'), nullable=True)
    location = db.Column(db.String(500), nullable=True)
    image_link = db.Column(db.String(500), nullable=True)
    website_relation = db.relationship('ProfessorWebsiteLinkModel', backref='professorwebsitelinkmodel', cascade='all, delete')
    feedback_relation = db.relationship('ProfessorFeedbackModel', backref='professorfeedbackmodel', cascade='all, delete')
    area_of_interest_relation = db.relationship('ProfessorAreaOfInterestModel', backref='professorareaofinterestmodel', cascade='all, delete')
    funding_relation = db.relationship('FundingModel', backref='fundingmodel', cascade='all, delete')

    def json(self):
        return {'id': self.id, 'name': self.name, 'email': self.email, 'university_id': self.university_id, 'location': self.location, 'image_link': self.image_link}