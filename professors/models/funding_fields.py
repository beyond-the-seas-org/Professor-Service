from professors import db

class FundingFieldsModel(db.Model):
    """
    primary key: funding_id and field_id
    """

    __tablename__ = 'funding_fields'

    funding_id = db.Column(db.Integer, db.ForeignKey('funding.id'), primary_key=True, nullable=False)
    field_id = db.Column(db.Integer, primary_key=True, nullable=False)


    def json(self):
        return {'funding_id': self.funding_id, 'field_id': self.field_id}