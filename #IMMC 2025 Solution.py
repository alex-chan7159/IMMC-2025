# IMMC 2025 Solution (Schedule Implementation)

# Teams from the same continent face each other
# Factors in team strength (strong team more likely to win)
# Matchmaking based on performance
# No team faces each other twice
# Each team gets 5 home games and 5 away games
# Tiebreaker score to decide winner if tied for # of wins
#   Should be the sum of the FIBA rankings of the opponents they have faced in all of their rounds combined, where the lower it is the better

class Team:
    def __init__(self, country, fibaRank, homeLocation):
        self.country = country #string
        self.points = 0 #int, victory is worth 1 while draws are worth 0
        self.teamsPlayed = [] #dynamic list
        self.fibaRank = fibaRank #int
        self.homeLocation = homeLocation #{latitude, longitude}
        #self.games = games #{wins, draws, losses}

def createTeams():

    teams = []

    teams.append(Team("Australia", 7, [-35.4735, 149.0124])) #canberra 35.4735° S, 149.0124° E
    teams.append(Team("New Zealand", 22, [-41.2866, 174.7756]))
    
    teams.append(Team("United States of America", 1, [38.8951, -77.0364]))
    teams.append(Team("Canada", 6, [45.4166, -75.6980]))
   
    teams.append(Team("Brazil", 12, [-15.7797, -47.9297]))
    teams.append(Team("Argentina", 8, [-34.6051, -58.4004]))
    teams.append(Team("Venezuela", 25, [10.4880, -66.8792]))
    teams.append(Team("Colombia", 55, [4.6097, -74.0818]))

    teams.append(Team("Egypt", 37, [30.0392, 31.2394]))
    teams.append(Team("Nigeria", 42, [9.0574, 7.4898]))

    teams.append(Team("Japan", 21, [35.6895, 139.6917]))
    teams.append(Team("Türkiye", 27, [39.9199, 32.8543]))
    teams.append(Team("China", 30, [39.9075, 116.3972]))
    teams.append(Team("Iran", 28, [35.6944, 51.4215]))

    teams.append(Team("Germany", 3, [52.5244, 13.4105]))
    teams.append(Team("France", 4, [48.8534, 2.3488]))
    teams.append(Team("Spain", 5, [40.4165, -3.7026]))
    teams.append(Team("Serbia", 2, [44.8176, 20.4633]))
    teams.append(Team("Lithuania", 10, [54.6892, 25.2798]))
    teams.append(Team("Latvia", 9, [56.9460, 24.1059]))

    #the following are the 4 additional teams, totalling 24 country teams!
    #Africa
    teams.append(Team("Côte d'Ivoire", 31, [5.3453, -4.0268]))
    teams.append(Team("Tunisia", 36, [36.8190, 10.1658]))
    
    #North America
    teams.append(Team("Mexico", 26, [19.4273, -99.1419]))
    teams.append(Team("Dominican Republic", 18, [18.4896, -69.9018]))

    return teams


def main(): 
    teams = createTeams()
    print(teams[0].country)
    
#main method call
main()