#recommendations, which user likse the most artist, save and quit, extra credit 3

data = {"John": ["Jej", "Ses", "Kek"], "Ioannis":["Sej"], "Jayson":["squink", "squonk"]}

def getRecommendations(currUser, prefs, userMap):
    ''' Gets recommendations for a user (currUser) based
    on the users in userMap (a dictionary)
    and the user's preferences in pref (a list).
    Returns a list of recommended artists. '''
    bestUser = findBestUser(currUser, prefs, userMap)
    recommendations = drop(prefs, userMap[bestUser])
    return recommendations

def findBestUser(currUser, prefs, userMap):
    ''' Find the user whose tastes are closest to the current
    user. Return the best user's name (a string) '''
    users = userMap.keys()
    bestUser = None
    bestScore = -1
    for user in users:
        score = numMatches(prefs, userMap[user])
        if score > bestScore and currUser != user:
            bestScore = score
            bestUser = user
    return bestUser

def drop(list1, list2):
    ''' Return a new list that contains only the elements in
    list2 that were NOT in list1. '''
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j += 1
    return list3

def numMatches( list1, list2 ):
    ''' return the number of elements that match between
    two sorted lists '''
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

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

def saveAndQuit():
    """ Saves all users to the current database. Creates a new database if one
        does not exist yet """
    with open("musicrecplus.txt", 'w') as file:
        for k,l in data.items():
            file.write(k+":")
            length = len(l)
            for i in range(length):
                if i < length - 1:
                    file.write(l[i]+",")
                else:
                    file.write(l[i]+"\n")