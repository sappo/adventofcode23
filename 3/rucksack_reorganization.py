import os
import sys
import string
from typing import List

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils import read

priorities = {char: ord(char) - 96 for char in string.ascii_lowercase}
priorities.update({char: ord(char) - 64 + 26 for char in string.ascii_uppercase})


rucksacks: List[str] = read.read_puzzle(3)

priorities_sum = 0
for rucksack in rucksacks:
    compartment_one = set(item for item in rucksack[0: int(len(rucksack) / 2)])
    compartment_two = set(item for item in rucksack[int(len(rucksack) / 2):])
    common_items = compartment_one.intersection(compartment_two)
    priorities_sum += sum([priorities[item] for item in common_items])

print(f"Sum of priorities between compartments: {priorities_sum}")


priorities_sum = 0
for i in range(0, len(rucksacks), 3):
    rucksack_one = set(item for item in rucksacks[i])
    rucksack_two = set(item for item in rucksacks[i + 1])
    rucksack_three = set(item for item in rucksacks[i + 2])

    common_items = set.intersection(rucksack_one, rucksack_two, rucksack_three)
    priorities_sum += sum([priorities[item] for item in common_items])

print(f"Sum of priorities between groups: {priorities_sum}")
