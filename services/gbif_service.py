import requests

def fetch_species(species_name):
    """Fetch species data from GBIF API"""
    try:
        url = f"https://api.gbif.org/v1/species/search?q={species_name}"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            results = response.json().get('results', [])
            return results
        else:
            return []
    except Exception as e:
        print(f"Error fetching from GBIF: {e}")
        return []
