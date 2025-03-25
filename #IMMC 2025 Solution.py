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
    teams.append(Team("New Zealand", 22, []))
    
    teams.append(Team("United States of America", 1, []))
    teams.append(Team("Canada", 6, []))
   
    teams.append(Team(""))
    teams.append()
    teams.append()
    teams.append()
    teams.append()
    teams.append()
    teams.append()
    teams.append()
    teams.append()
    teams.append()
    teams.append()
    teams.append()
    teams.append()
    teams.append()
    teams.append()
    teams.append()

    #the following are the 4 additional teams, totalling 24 country teams!
    #teams.append()
    #teams.append()
    #teams.append()
    #teams.append()

    return teams



def main(): 
    teams = createTeams()
    print(teams[0])
    
#main method call
main()