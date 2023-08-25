from professors import db

class LocationModel(db.Model):

    """
    primary key: id
    other fields: location_name(basically city name),area_type(rural or city),country_name,avg_living_cost(e.g 2500-3000$),weather,public_transportation,population,avg_income,summer_comfort_index(comfort_index is a measurement which indicate how much the weather is comfortable to live),winter_comfort_index,unemployment_rate(in %)
    """

    #db should bind to analytics database
    __bind_key__ = 'analytics'
    __tablename__ = 'location'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    location_name = db.Column(db.String(50), nullable=False)
    area_type = db.Column(db.String(50))
    country_name = db.Column(db.String(30), nullable=False)
    avg_living_cost = db.Column(db.Float)
    public_transportation = db.Column(db.String(100))
    population = db.Column(db.Integer)
    avg_income = db.Column(db.Float)
    summer_comfort_index = db.Column(db.Float) 
    winter_comfort_index = db.Column(db.Float)
    unemployment_rate = db.Column(db.Float)


    # create a json method
    def json(self):
        return {
            'id': self.id,
            'location_name': self.location_name,
            'area_type': self.area_type,
            'country_name': self.country_name,
            'avg_living_cost': self.avg_living_cost,
            'public_transportation':self.public_transportation,
            'avg_income':self.avg_income,
            'population':self.population,
            'summer_comfort_index':self.summer_comfort_index,
            'winter_comfort_index':self.winter_comfort_index,
            'unemployment_rate': self.unemployment_rate

        }