from professors import db 

class FieldModel(db.Model):

    """
    primary key: id
    other fields: name
    """

    __tablename__ = 'field'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(500), nullable=False, unique=True)

    # create a json method
    def json(self):
        return {
            'id': self.id,
            'name': self.name
        }