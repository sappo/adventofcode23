import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils import read
from enum import Enum


games = read.read_puzzle(2)

ROCKS = ["A", "X"]
PAPERS = ["B", "Y"]
SCISSORS = ["C", "Z"]


class HAND(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def get_hand(input: str) -> HAND:
    if input in ROCKS:
        return HAND.ROCK
    elif input in PAPERS:
        return HAND.PAPER
    elif input in SCISSORS:
        return HAND.SCISSORS
    else:
        raise Exception()


def get_expected_hand(opponent: HAND, input: str) -> HAND:
    if input == "X":  # lose
        if opponent == HAND.ROCK:
            return HAND.SCISSORS
        elif opponent == HAND.PAPER:
            return HAND.ROCK
        else:
            return HAND.PAPER
    elif input == "Y":  # draw
        return opponent
    elif input == "Z":  # win
        if opponent == HAND.ROCK:
            return HAND.PAPER
        elif opponent == HAND.PAPER:
            return HAND.SCISSORS
        else:
            return HAND.ROCK
    else:
        raise Exception()


def calculate_score(opponent: HAND, you: HAND) -> int:
    score = 0
    if you == HAND.ROCK:
        score += 1
    elif you == HAND.PAPER:
        score += 2
    elif you == HAND.SCISSORS:
        score += 3

    if opponent == you:
        score += 3  # draw
    elif opponent == HAND.ROCK and you == HAND.PAPER:
        score += 6  # won
    elif opponent == HAND.PAPER and you == HAND.SCISSORS:
        score += 6  # won
    elif opponent == HAND.SCISSORS and you == HAND.ROCK:
        score += 6  # won
    else:
        score += 0  # lost

    return score


total_score = 0
for game in games:
    opponent = get_hand(game.split(" ")[0].strip())
    you = get_hand(game.split(" ")[1].strip())
    total_score += calculate_score(opponent, you)
print(f"Your total score is: {total_score}")


total_score = 0
for game in games:
    opponent = get_hand(game.split(" ")[0].strip())
    you = get_expected_hand(opponent, game.split(" ")[1].strip())
    total_score += calculate_score(opponent, you)
print(f"Your total expected score is: {total_score}")
