#  User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.


def make_album(title, artist, tracks=""):
    if tracks:
        album = {title: artist, "tracks": tracks}
    else:
        album = {title: artist}

    return album


while True:
    print("\nMake your own album.")
    print("Press q to quit the program.\n")

    album_title = input("Enter the title of the Album: ")
    if album_title == "q":
        break

    album_artist = input("Enter the artish of the album")
    if album_artist == "q":
        break

    print(make_album(album_title, album_artist))
