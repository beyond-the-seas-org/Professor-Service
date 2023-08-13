from professors import db 

class ProfessorWebsiteLinkModel(db.Model):
    """
    primary key: id
    other fields: professor_id, website_link, website_type
    """

    __tablename__ = 'professor_website_link'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    website_link = db.Column(db.String(500), nullable=False)
    website_type = db.Column(db.String(200), nullable=False)


    def json(self):
        return {'id': self.id, 'professor_id': self.professor_id, 'website_link': self.website_link, 'website_type': self.website_type}