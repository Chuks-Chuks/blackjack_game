class CardScores:
    def __init__(self, player_cards):
        self.player_cards = player_cards

    def calculate_score(self):
        total = sum(self.player_cards)

        if total == 21 and len(self.player_cards) == 2:
            total = 0
            return total

        if 11 in self.player_cards and total > 21:
            self.player_cards.remove(11)
            self.player_cards.append(1)
        return total


class Compare:
    def __init__(self, player_score, compt_score):
        self.player_score = player_score
        self.compt_score = compt_score

    def compare(self):
        if self.player_score == 0:
            print("Blackjack. You win!")
            return True
        elif self.compt_score == 0:
            print("Blackjack. You lose.")
            return False
        elif self.player_score > 21:
            print("You went over! You lost!")
            return False
        elif self.compt_score > 21:
            print("The computer went over! You win!")
            return True
        elif self.player_score > self.compt_score:
            print("You win!")
            return True
        elif self.compt_score > self.player_score:
            print("You lose!")
            return False
        else:
            print("It's a draw!")
