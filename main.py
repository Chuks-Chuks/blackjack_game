from art import logo
from replit import clear
from cards import Card
from card_scores import CardScores, Compare
from bet_compute import Stake


def blackjack():
    card = Card()
    user_cards = []
    computer_cards = []
    print(logo)
    total = int(input("How much do you have to play? £"))
    stake = int(input("How much do you want to stake? £"))

    def continue_game():
        for deal in range(2):
            user_cards.append(card.deal_card())
            computer_cards.append(card.deal_card())

        user = CardScores(user_cards)
        computer = CardScores(computer_cards)
        while True:

            user_score = user.calculate_score()
            computer_score = computer.calculate_score()
            print(f"\tYour hand: {user_cards}, your score: {user_score}.")
            print(f"\tComputer's first card: {computer_cards[0]}.")

            if user_score == 0 or computer_score == 0 or user_score > 21:
                break
            else:
                play_again = input(
                    "Do you want to draw another card? Type 'y' to draw another card or 'n' to quit.\n").lower()
                if play_again == "y":
                    user_cards.append(card.deal_card())
                else:
                    break
        while computer_score < 17:
            computer_cards.append(card.deal_card())
            computer_score = computer.calculate_score()
        return user_score, computer_score

    scores = continue_game()
    check_scores = Compare(scores[0], scores[1])
    staking = Stake(total, stake)
    new_total = staking.stake_compute(check_scores.compare())
    print(f"\tYou have a total value of £{new_total}.")
    print(f"\tYour final hand: {user_cards}, your final score: {scores[0]}.")
    print(f"\tComputer's final hand: {computer_cards}, computer's final score: {scores[1]}.")
    while True:
        cont_game = input("Do you want to continue playing? Type 'y' to continue or 'n' to quit.\n")
        if cont_game == "y":
            clear()
            print(logo)
            if new_total > 0:
                total = new_total
                user_cards = []
                computer_cards = []
                print(f'Your current balance is: £{total}')
                stake = int(input("How much do you want to stake? £"))
                new_score = continue_game()
                check_scores = Compare(new_score[0], new_score[1])
                staking = Stake(total, stake)
                new_total = staking.stake_compute(check_scores.compare())
                print(f"\tYou have a total value of £{new_total}.")
                print(f"\tYour final hand: {user_cards}, your final score: {new_score[0]}.")
                print(f"\tComputer's final hand: {computer_cards}, computer's final score: {new_score[1]}.")
            else:
                break
        else:
            break


restart = input("Do you want to play a game of Blackjack? Type 'y' to play or 'n' to quit.\n")
if restart == "y":
    clear()
    blackjack()
