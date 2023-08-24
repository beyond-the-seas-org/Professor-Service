from professors import db

class OnGoingResearchModel(db.Model):
    """
    primary key: id
    other fields: research_field, research_topic, description, num_of_students, research_desc_link, funding_id
    """

    __tablename__ = 'on_going_research'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    research_field = db.Column(db.String(200), nullable=False)
    research_topic = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    num_of_students = db.Column(db.Integer, nullable=True)
    research_desc_link = db.Column(db.String(500), nullable=True)
    funding_id = db.Column(db.Integer, db.ForeignKey('funding.id'), nullable=True)
    students_on_going_research = db.relationship('OnGoingResearchOfStudentModel', backref='ongoingresearchmodel', cascade='all, delete')
    professor_on_going_research = db.relationship('OnGoingResearchOfProfessorModel', backref='ongoingresearchmodel', cascade='all, delete')


    def json(self):
        return {'id': self.id, 'research_field': self.research_field, 'research_topic': self.research_topic, 'description': self.description, 'num_of_students': self.num_of_students, 'research_desc_link': self.research_desc_link, 'funding_id': self.funding_id}