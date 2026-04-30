from flask import Flask
from config import db
from routes.species_routes import species_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///species.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(species_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)