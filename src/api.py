import requests

def main():
    artwork = input("enter an artwork name: ")
    artworks = get_artworks(query=artwork,limit=3)
    for artwork in artworks:
        print(f"*{artwork}")


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

    

main()









