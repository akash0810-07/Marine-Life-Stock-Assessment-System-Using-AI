def predict_population(species_name, current_population):
    """Simple population prediction based on current data"""
    try:
        # Basic prediction: assume 5% annual growth
        predicted_population = current_population * (1.05)
        return round(predicted_population)
    except Exception as e:
        print(f"Error predicting population: {e}")
        return None
