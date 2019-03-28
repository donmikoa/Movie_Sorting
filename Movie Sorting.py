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





