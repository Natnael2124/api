import requests

def main():
    print("search the art institute of chicago")
    artist = input("enter an artist name: ")
    try:
        response = requests.get(
            "https://api.artic.edu./api/v1/artworks/search",
            {"q":artist}
            )
        response.raise_for_status()
    except HTTPError:
        print("couldn't complete the request") 
        return
    content = response.json()
    for artwork in content["data"]:
        print(f"{artwork['title']}")
    

main()









