import requests

def get_artists(query,limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/agents/search",
            params = {"q":query,"limit":limit}
            )
        response.raise_for_status()
        content = response.json()
        return [artist["title"] for artist in content["data"]]
    except requests.HTTPError:
        print("couldn't complete the request") 
        return