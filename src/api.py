from museme.artists import get_artists

def main():
    artist = input("enter an artist name: ")
    artists = get_artists(query=artist,limit=3)
    for artist in artists:
        print(f"*{artist}")




    

main()









