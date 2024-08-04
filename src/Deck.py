class Deck:
    def __init__(self):
        self.DeckCards = card_deck = ["2C", "2S", "2D", "2H", "3C", "3S", "3D", "3H",
                                      "4C", "4S", "4D", "4H", "5C", "5S", "5D", "5H",
                                      "6C", "6S", "6D", "6H", "7C", "7S", "7D", "7H",
                                      "8C", "8S", "8D", "8H", "9C", "9S", "9D", "9H",
                                      "10C", "10S", "10D", "10H", "JC", "JS", "JD", "JH",
                                      "QC", "QS", "QD", "QH", "KC", "KS", "KD", "KH",
                                      "AC", "AS", "AD", "AH"]
        self.cardCount = 52

    def serveCard(self):
        if self.DeckCards:
            self.cardCount -= 1
            return self.DeckCards.pop()
        else:
            return None

    def addCard(self, card):
        self.DeckCards.append(card)
        self.cardCount += 1
