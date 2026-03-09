from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
from datetime import datetime

app = Flask(__name__)

observations = []

RISK_DATA = [
    {"name": "Atlantic Bluefin Tuna", "sci": "Thunnus thynnus", "pct": 92, "level": "critical"},
    {"name": "Atlantic Cod", "sci": "Gadus morhua", "pct": 81, "level": "critical"},
    {"name": "Swordfish", "sci": "Xiphias gladius", "pct": 78, "level": "critical"},
    {"name": "Yellowfin Tuna", "sci": "Thunnus albacares", "pct": 67, "level": "high"},
    {"name": "Bluefin Grouper", "sci": "Epinephelus sp.", "pct": 61, "level": "high"},
    {"name": "North Sea Herring", "sci": "Clupea harengus", "pct": 44, "level": "moderate"},
    {"name": "Pacific Halibut", "sci": "Hippoglossus stenolepis", "pct": 28, "level": "low"},
    {"name": "Alaskan Pollock", "sci": "Gadus chalcogrammus", "pct": 19, "level": "low"},
]

QUOTA_DATA = [
    {"species": "Bluefin Tuna", "allowed": 100, "actual": 142},
    {"species": "Atlantic Cod", "allowed": 80, "actual": 91},
    {"species": "Swordfish", "allowed": 60, "actual": 55},
    {"species": "Yellowfin Tuna", "allowed": 120, "actual": 138},
    {"species": "N. Sea Herring", "allowed": 200, "actual": 180},
    {"species": "Haddock", "allowed": 90, "actual": 95},
]

MAP_POINTS = [
    {"lat": 36.7, "lng": -74.2, "species": "Bluefin Tuna", "count": 320, "risk": "critical", "ocean": "North Atlantic"},
    {"lat": 61.3, "lng": 4.1, "species": "Atlantic Cod", "count": 890, "risk": "critical", "ocean": "North Sea"},
    {"lat": 38.2, "lng": 2.3, "species": "Swordfish", "count": 210, "risk": "high", "ocean": "Mediterranean"},
    {"lat": -33.8, "lng": 151.2, "species": "Great White Shark", "count": 45, "risk": "moderate", "ocean": "Pacific"},
    {"lat": 20.5, "lng": -87.3, "species": "Grouper", "count": 560, "risk": "high", "ocean": "Caribbean"},
    {"lat": -58.1, "lng": -64.3, "species": "Humpback Whale", "count": 120, "risk": "low", "ocean": "Antarctic"},
    {"lat": 35.6, "lng": 139.7, "species": "Pacific Salmon", "count": 4200, "risk": "moderate", "ocean": "North Pacific"},
    {"lat": 64.1, "lng": -51.7, "species": "Arctic Cod", "count": 2100, "risk": "moderate", "ocean": "Arctic"},
    {"lat": -4.3, "lng": 15.3, "species": "Yellowfin Tuna", "count": 730, "risk": "high", "ocean": "Indian Ocean"},
]

GBIF_BASE = "https://api.gbif.org/v1"

def gbif_get(endpoint, params=None):
    try:
        r = requests.get(f"{GBIF_BASE}/{endpoint}", params=params, timeout=6)
        return r.json()
    except Exception:
        return {}

@app.route("/")
def index():
    fish_key = 11592253
    stats = {}
    try:
        occ = gbif_get("occurrence/search", {"taxonKey": fish_key, "limit": 0})
        spp = gbif_get("species/search", {"higherTaxonKey": fish_key, "rank": "SPECIES", "limit": 0})
        stats["obs_count"] = f"{occ.get('count', 142895):,}"
        stats["species_count"] = f"{min(spp.get('count', 1824), 9999):,}"
    except Exception:
        stats["obs_count"] = "142,895"
        stats["species_count"] = "1,824"

    stats["alerts"] = sum(1 for r in RISK_DATA if r["level"] == "critical")
    stats["health"] = 74
    stats["updated_at"] = datetime.now().strftime("%H:%M:%S")

    return render_template(
        "index.html",
        stats=stats,
        risk_data=RISK_DATA,
        quota_data=QUOTA_DATA,
        map_points=MAP_POINTS
    )

@app.route("/analysis")
def analysis():
    return render_template(
        "analysis.html",
        risk_data=RISK_DATA,
        quota_data=QUOTA_DATA,
        observations=observations
    )

@app.route("/api/species")
def api_species():
    q = request.args.get("q", "fish")
    limit = request.args.get("limit", 20)
    data = gbif_get("species/search", {"q": q, "rank": "SPECIES", "limit": limit})
    return jsonify(data.get("results", []))

@app.route("/api/observations/live")
def api_obs_live():
    data = gbif_get("occurrence/search", {
        "taxonKey": 11592253,
        "hasCoordinate": "true",
        "limit": 10
    })
    return jsonify(data.get("results", []))

@app.route("/api/risk")
def api_risk():
    return jsonify(RISK_DATA)

@app.route("/api/submit", methods=["POST"])
def api_submit():
    payload = request.json or {}
    required = ["species", "lat", "lng", "count"]
    if not all(payload.get(k) for k in required):
        return jsonify({"error": "Missing required fields"}), 400

    record = {
        "id": len(observations) + 1,
        "species": payload.get("species"),
        "sci_name": payload.get("sci_name", ""),
        "lat": float(payload.get("lat")),
        "lng": float(payload.get("lng")),
        "count": int(payload.get("count")),
        "risk": payload.get("risk", "low"),
        "observer": payload.get("observer", "Anonymous"),
        "notes": payload.get("notes", ""),
        "date": payload.get("date", datetime.now().strftime("%Y-%m-%d")),
        "submitted": datetime.now().isoformat(),
    }

    observations.append(record)

    return jsonify({
        "success": True,
        "id": record["id"],
        "record": record
    })

@app.route("/api/submissions")
def api_submissions():
    return jsonify(observations)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
