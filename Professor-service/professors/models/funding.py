from professors import db 

class FundingModel(db.Model):
    """
    primary key: id
    other fields: funding_post, date, amount, requirement_description, num_of_slot, professor_id, availability(yes or no)
    """

    __tablename__ = 'funding'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    funding_post = db.Column(db.String(30000), nullable=False)
    date = db.Column(db.DateTime)
    amount = db.Column(db.Integer, nullable=False)
    requirement_description = db.Column(db.String(5000), nullable=False)
    num_of_slot = db.Column(db.Integer, nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    availability = db.Column(db.Boolean, nullable=False)

    ongoingresearch = db.relationship('OnGoingResearchModel', backref='fundingmodel', cascade='all, delete')
    fundingfields = db.relationship('FundingFieldsModel', backref='fundingmodel', cascade='all, delete')


    def json(self):
        return {'id': self.id, 'funding_post': self.funding_post, 'date': self.date, 'amount': self.amount, 'requirement_description': self.requirement_description, 'num_of_slot': self.num_of_slot, 'professor_id': self.professor_id, 'availability': self.availability}