class Dealer:
    def __init__(self):
        self.Cards = []

    def getNextCard(self):
        if self.Cards:
            return self.Cards.pop(0)
        else:
            return None

    def setNextCard(self, card):
        self.Cards.append(card)

    def shuffleCards(self):
        import random
        random.shuffle(self.CCards)