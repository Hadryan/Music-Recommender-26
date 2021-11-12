#recommendations, which user likse the most artist, save and quit, extra credit 3


data = {"John": ["Jej", "Ses", "Kek"], "Ioannis":["Sej"], "Jayson":["squink", "squonk"]}

def mostLikedArtists():
    """ Prints out the full name of the user who likes the most artists. Only
        one name is printed if there is a tie. If there are no users, an error 
        message is printed"""
    if data == {}:
        print("Sorry, no user found")
    else:
        mostLikes = ""
        value = 0
        for k, l in data.items():
            if len(l) > value:
                value = len(l)
                mostLikes = k
        print(mostLikes)
