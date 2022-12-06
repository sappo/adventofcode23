import os
import sys
from typing import List

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import re
from utils import read


def print_stacks(stacks):
    max_crates = max(len(stack) for stack in stacks)
    for i in reversed(range(max_crates)):
        line = []
        for stack in stacks:
            try:
                line.append(stack[i])
            except IndexError:
                line.append(" ")
        print(" ".join(line))

    print(" ".join([str(x) for x in range(1, 10)]))
    print("")


def prepare_inital_stacks(lines) -> List[List[str]]:
    stacks = [[] for _ in range(9)]
    for line in reversed(lines[0:8]):
        for i in range(9):
            try:
                crate = line[(i * 4) + 1]
                if crate != " ":
                    stacks[i].append(crate)
            except IndexError:
                pass

    return stacks


lines = read.read_puzzle(5)
stacks = prepare_inital_stacks(lines)
print_stacks(stacks)

move_regex = re.compile(r"move (\d+) from (\d+) to (\d+)")

for instruction in lines[10:]:
    match = re.match(move_regex, instruction)
    if match:
        moves = int(match.group(1))
        from_stack = int(match.group(2))
        to_stack = int(match.group(3))
    else:
        raise Exception()

    for _ in range(moves):
        crate = stacks[from_stack - 1].pop()
        stacks[to_stack - 1].append(crate)

print_stacks(stacks)

top_crates = []
for stack in stacks:
    top_crates.append(stack[-1])

print(f"Top crates CrateMover 9001: {''.join(top_crates)}")

stacks = prepare_inital_stacks(lines)
print_stacks(stacks)

for instruction in lines[10:]:
    match = re.match(move_regex, instruction)
    if match:
        moves = int(match.group(1))
        from_stack = int(match.group(2))
        to_stack = int(match.group(3))
    else:
        raise Exception()

    crates_to_move = stacks[from_stack - 1][moves * -1 :]
    stacks[from_stack - 1] = stacks[from_stack - 1][: moves * -1]
    stacks[to_stack - 1] = stacks[to_stack - 1] + crates_to_move

top_crates = []
for stack in stacks:
    top_crates.append(stack[-1])

print(f"Top crates CrateMover 9001: {''.join(top_crates)}")
