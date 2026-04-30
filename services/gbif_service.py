import requests

def fetch_species(species_name):
    url = f"https://api.gbif.org/v1/species/search?q={species_name}"

    try:
        response = requests.get(url)
        data = response.json()
        return data.get("results", [])
    except:
        return []
