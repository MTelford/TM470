class Networking:
    def __init__(self):
        self.PlayerOneData = None
        self.PlayerTwoData = None

    def setPlayerData(self, player, data):
        if player == 1:
            self.PlayerOneData = data
        elif player == 2:
            self.PlayerTwoData = data

    def getPlayerData(self, player):
        if player == 1:
            return self.PlayerOneData
        elif player == 2:
            return self.PlayerTwoData
