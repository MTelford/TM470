class Player:
    def __init__(self, name='', location=''):
        self.Name = name
        self.Location = location

    def getName(self):
        return self.Name

    def getLocation(self):
        return self.Location

    def setName(self, name):
        self.Name = name

    def setLocation(self, location):
        self.Location = location