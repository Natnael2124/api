import requests

def get_artworks(query,limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            params = {"q":query,"limit":limit}
            )
        response.raise_for_status()
        content = response.json()
        return [artwork["title"] for artwork in content["data"]]
    except requests.HTTPError:
        print("couldn't complete the request") 
        return