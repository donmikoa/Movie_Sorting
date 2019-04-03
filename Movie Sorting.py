#This program has a list of some movies which will be sorted out based on some filters

moviesDict = {2005: [['Munich', 'Steven Spielberg']],
              2006: [['The Prestige', 'Christopher Nolan'], ['The Departed', 'Martin Scorsese']],
              2007: [['Into the Wild', 'Sean Penn']],
              2008: [['The Dark Knight', 'Christopher Nolan']],
              2009: [['Mary and Max', 'Adam Elliot']],
              2010: [["The King's Speech", 'Tom Hooper']],
              2011: [['The Artist', 'Michel Hazanavicius'], ['The Help', 'Tate Taylor']],
              2012: [['Argo', 'Ben Affleck']],
              2013: [['12 Years a Slave', 'Steve McQueen']],
              2014: [['Birdman', 'Alejandro G. Inarritu']],
              2015: [['Spotlight', 'Tom McCarthy']],
              2016: [['The BFG', 'Steven Spielberg']]}
year = int(input("Enter a year between 2005 and 2016:\n"))
if year < 2005 or year > 2016:
    print("N/A")
else:
    movies = moviesDict[year]
    for movie in movies:
        print(movie[0] + ", " + movie[1])
var = 1
print("")

while var == 1:
    print("MENU")
    print("Sort by:")
    print("y - Year")
    print("d - Director")
    print("t - Movie title")
    print("q - Quit")
    print("")
    option = input("Choose an option:\n")
    if option == 'y':
        for key in sorted(moviesDict.keys()):
            print(key, end=':')
            print("")
            for movie in moviesDict[key]:
                print("\t" + movie[0] + ", " + movie[1])
            print("")
    elif option == 'd':
        dirDict = {}
        for key in sorted(moviesDict.keys()):
            for movie in moviesDict[key]:
                dire = movie[1]
                if dire in dirDict:
                    dirDict[dire].append([movie[0], key])
                else:
                    dirDict[dire] = [[movie[0], key]]
        for key in sorted(dirDict.keys()):
            print(key, end=':')
            print("")
            for dire in dirDict[key]:
                print("\t" + str(dire[0]) + ", " + str(dire[1]))
            print("")
    elif option == 't':
        titleDict = {}
        for key in sorted(moviesDict.keys()):
            for movie in moviesDict[key]:
                title = movie[0]
                if title in titleDict:
                    titleDict[title].append([movie[1], key])
                else:
                    titleDict[title] = [[movie[1], key]]
        for key in sorted(titleDict.keys()):
            print(key, end=':')
            print("")
            for title in titleDict[key]:
                print("\t" + str(title[0]) + ", " + str(title[1]))
                print("")
            elif (option == 'q':
            break;
        else:
            print("Invalid option")









