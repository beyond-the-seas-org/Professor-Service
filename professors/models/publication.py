from professors import db

class PublicationModel(db.Model):

    """
    primary key: id
    other fields: title, doi, link, abstract, date, venue, citation, keywords, research_area
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
    keywords = db.Column(db.String(1000))
    research_area = db.Column(db.String(200))

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
            'citation': self.citation,
            'keywords': self.keywords,
            'research_area': self.research_area
        }