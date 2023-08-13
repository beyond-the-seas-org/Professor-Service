from app import db

class PublicationModel(db.Model):

    """
    primary key: id
    other fields: title, doi, link, abstract, date, venue, citation
    """

    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String(500), nullable=False, unique=True)
    doi = db.Column(db.String(500), nullable=False, unique=True)
    link = db.Column(db.String(500))
    abstract = db.Column(db.String(5000))
    date = db.Column(db.DateTime) # yyyy-mm-dd
    venue = db.Column(db.String(500))
    citation = db.Column(db.Integer)

    # create a json method
    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'doi': self.doi,
            'link': self.link,
            'abstract': self.abstract,
            'date': self.date,
            'venue': self.venue,
            'citation': self.citation
        }