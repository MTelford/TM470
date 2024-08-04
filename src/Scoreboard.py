class Scoreboard:
    def __init__(self):
        self.PlayerOneScore = 0
        self.PlayerTwoScore = 0

    def setPlayerScore(self, player, score):
        if player == 1:
            self.PlayerOneScore = score
        elif player == 2:
            self.PlayerTwoScore = score

    def getPlayerScore(self, player):
        if player == 1:
            return self.PlayerOneScore
        elif player == 2:
            return self.PlayerTwoScore
