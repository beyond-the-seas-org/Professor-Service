from professors import db 

class ProfessorPublicationModel(db.Model):
    """
    primary key: id
    other fields: publication_id, professor_id
    """

    __tablename__ = 'professor_publication'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    publication_id = db.Column(db.Integer, db.ForeignKey('publication.id'), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    publication_relation = db.relationship('PublicationModel', backref='professorpublicationmodel', cascade='all, delete')


    def json(self):
        return {'id': self.id, 'publication_id': self.publication_id, 'professor_id': self.professor_id}