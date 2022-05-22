import random

from models.player import Player


def play_game(player1, player2):
    if player1.choice == player2.choice:
        return None
    elif player1.choice == "Rock":
        if player2.choice == "Paper":
            return player2
        elif player2.choice == "Scissors":
            return player1
    elif player1.choice == "Paper":
        if player2.choice == "Rock":
            return player1
        elif player2.choice == "Scissors":
            return player2
    elif player1.choice == "Scissors":
        if player2.choice == "Rock":
            return player2
        elif player2.choice == "Paper":
            return player1


def create_computer_player():
    choices = ["Rock", "Paper", "Scissors"]
    computer = Player("Computer", random.choice(choices))
    return computer
