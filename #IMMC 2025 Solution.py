# IMMC 2025 Solution (Schedule Implementation)

# Teams from the same continent face each other
# Factors in team strength (strong team more likely to win)
# Matchmaking based on performance
# No team faces each other twice
# Each team gets 5 home games and 5 away games
# Tiebreaker score to decide winner if tied for # of wins
#   Should be the sum of the FIBA rankings of the opponents they have faced in all of their rounds combined, where the lower it is the better

import math

#
class Team:
    def __init__(self, country, fibaRank, homeLocation):
        self.country = country #string
        self.points = 0 #int, victory is worth 1 while draws are worth 0
        self.teamsPlayed = [] #dynamic list
        self.tiebreakerScore = 0 #int, accumulator
        self.fibaRank = fibaRank #int
        self.homeLocation = homeLocation #{latitude, longitude}

def createTeams():

    teams = []

    #Oceania
    teams.append(Team("Australia", 7, [-35.4735, 149.0124])) #canberra 35.4735° S, 149.0124° E
    teams.append(Team("New Zealand", 22, [-41.2866, 174.7756]))
    
    #North America
    teams.append(Team("United States of America", 1, [38.8951, -77.0364]))
    teams.append(Team("Canada", 6, [45.4166, -75.6980]))
   
    #South America
    teams.append(Team("Brazil", 12, [-15.7797, -47.9297]))
    teams.append(Team("Argentina", 8, [-34.6051, -58.4004]))
    teams.append(Team("Venezuela", 25, [10.4880, -66.8792]))
    teams.append(Team("Colombia", 55, [4.6097, -74.0818]))

    #Africa
    teams.append(Team("Egypt", 37, [30.0392, 31.2394]))
    teams.append(Team("Nigeria", 42, [9.0574, 7.4898]))

    #Asia
    teams.append(Team("Japan", 21, [35.6895, 139.6917]))
    teams.append(Team("Türkiye", 27, [39.9199, 32.8543]))
    teams.append(Team("China", 30, [39.9075, 116.3972]))
    teams.append(Team("Iran", 28, [35.6944, 51.4215]))

    #Europe
    teams.append(Team("Germany", 3, [52.5244, 13.4105]))
    teams.append(Team("France", 4, [48.8534, 2.3488]))
    teams.append(Team("Spain", 5, [40.4165, -3.7026]))
    teams.append(Team("Serbia", 2, [44.8176, 20.4633]))
    teams.append(Team("Lithuania", 10, [54.6892, 25.2798]))
    teams.append(Team("Latvia", 9, [56.9460, 24.1059]))

    #the following are 4 additional teams, totalling 24 country teams!
    #Africa
    teams.append(Team("Côte d'Ivoire", 31, [5.3453, -4.0268]))
    teams.append(Team("Tunisia", 36, [36.8190, 10.1658]))
    
    #North America
    teams.append(Team("Mexico", 26, [19.4273, -99.1419]))
    teams.append(Team("Dominican Republic", 18, [18.4896, -69.9018]))

    return teams

#returns a boolean, determined by whether two countries have already played against each other
def alreadyPaired(teamOne, teamTwo):
    if teamTwo.country in teamOne.teamsPlayed:
        return True
    else:
        return False

#returns a float, uses haversine formula to calculate the distance between two team's cities
def distance(teamOne, teamTwo):
    #convert latitude and longitude from degrees to radians
    lat1 = math.radians(teamOne.homeLocation[0])
    long1 = math.radians(teamOne.homeLocation[1])

    lat2 = math.radians(teamTwo.homeLocation[0])
    long2 = math.radians(teamTwo.homeLocation[1])

    #define the radius (earth's radius in kilometers)
    r = 6378

    #calculate differences between the latitutdes and longitudes
    deltaLat = lat2 - lat1
    deltaLong = long2 - long1

    #use the haversine formula
    a = math.sin(deltaLat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(deltaLong / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    #distance is radius * c
    return r * c

def main(): 
    teams = createTeams()
    #print(teams[0].country)
    print(distance(teams[0], teams[1]))
    
#main method call
main()