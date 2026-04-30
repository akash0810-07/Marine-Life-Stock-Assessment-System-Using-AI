from flask import Blueprint, request, jsonify, render_template
from services.gbif_service import fetch_species
from services.prediction_service import predict_population
from models.species_model import Species
from config import db

species_bp = Blueprint('species', __name__)

@species_bp.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@species_bp.route("/search", methods=["POST"])
def search_species():
    name = request.form.get("name")

    if not name:
        return {"error": "Invalid input"}

    results = fetch_species(name)

    # Save first result in DB
    if results:
        species = Species(name=name, population=len(results))
        db.session.add(species)
        db.session.commit()

    return render_template("index.html", results=results)


@species_bp.route("/predict", methods=["GET"])
def predict():
    data = Species.query.all()
    populations = [s.population for s in data]

    prediction = predict_population(populations)

    return jsonify({"prediction": prediction})