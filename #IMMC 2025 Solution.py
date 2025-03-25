# IMMC 2025 Solution (Schedule Implementation)

# Teams from the same continent face each other
# Factors in team strength (strong team more likely to win)
# Matchmaking based on performance
# No team faces each other twice
# Each team gets 5 home games and 5 away games
# Tiebreaker score to decide winner if tied for # of wins
#   Should be the sum of the FIBA rankings of the opponents they have faced in all of their rounds combined, where the lower it is the better

class Team:
    def __init__(self, country, points, teamsPlayed, fibaRank, homeLocation, games):
        self.country = country #string
        self.points = points #int, victory is worth 1 while draws are worth 0?
        self.teamsPlayed = teamsPlayed #{}, dynamic list
        self.fibaRank = fibaRank #int
        self.homeLocation = homeLocation #{latitude, longitude}
        #self.games = games #{wins, draws, losses}


