from config import db

class Species(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    population = db.Column(db.Integer, nullable=True)
    
    def __repr__(self):
        return f'<Species {self.name}>'
