from professors import db 

class StudentPublicationModel(db.Model):
    """
    primary key: id
    other fields: publication_id, student_id
    """

    __tablename__ = 'student_publication'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    publication_id = db.Column(db.Integer, db.ForeignKey('publication.id'), nullable=False)
    student_id = db.Column(db.Integer, nullable=False)
    publication_relation = db.relationship('PublicationModel', backref='studentpublicationmodel', cascade='all, delete')


    def json(self):
        return {'id': self.id, 'publication_id': self.publication_id, 'student_id': self.student_id}