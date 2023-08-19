from professors import db

class UniversityRankModel(db.Model):
    """
    primary key: id
    other fields: name, rank, area_of_interest_id
    """

    __tablename__ = 'university_rank'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    rank = db.Column(db.Integer, nullable=True)
    area_of_interest_id = db.Column(db.Integer, nullable=True)
    relation = db.relationship('ProfessorModel', backref='universityrankmodel', cascade='all, delete')



    def json(self):
        return {'id': self.id, 'name': self.name, 'rank': self.rank, 'area_of_interest_id': self.area_of_interest_id}