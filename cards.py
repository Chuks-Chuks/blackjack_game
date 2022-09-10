import random


class Card:
    def __init__(self):
        self.card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def deal_card(self):
        """Returns a random card from the selected deck. """
        card = random.choice(self.card)
        return card
