#!/usr/bin/env python3
import random
import time

options_list = ["rock", "paper", "scissors"]
running = True
instructions = """
Here are the rules:
- Rock beats scissors
- Scissors beats paper
- Paper beats rock
"""

while running:
    print(instructions)
    time.sleep(1)

    player = None
    while player not in options_list:
        player = input("Pick your hand - (rock, paper or scissors): ")
    opponent = random.choice(options_list)   
    print(f"Player: {player}")
    print(f"Opponent: {opponent}")

    if player == opponent:
        print("It's a tie!")
    elif player == "rock":
        if opponent == "paper":
            print("You lose.")
        else:
            print("You win!")
    elif player == "paper":
        if opponent == "rock":
            print("You win!")
        else:
            print("You lose.")
    elif player == "scissors":
        if opponent == "rock":
            print("You lose.")
        else:
            print("You win!")
    
    time.sleep(1)
    another_game = None
    while another_game != "n" and another_game != "y":
        another_game = input("Play again? (y/n) ")
    if another_game == "n":
        running = False
        print("Thanks for playing!")
        time.sleep(1)