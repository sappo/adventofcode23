import os
import sys
import pprint
from typing import List

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils import read

pp = pprint.PrettyPrinter(indent=2)

lines: List[str] = read.read_puzzle(9)


class Knot:
    def __init__(self, x: int, y: int, name=None):
        self.x = x
        self.y = y
        self.name = name

    def __eq__(self, other) -> bool:
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def move_in_direction(self, direction: str):
        if direction == "R":
            self += Knot(1, 0)
        elif direction == "L":
            self += Knot(-1, 0)
        elif direction == "U":
            self += Knot(0, 1)
        elif direction == "D":
            self += Knot(0, -1)
        else:
            raise Exception()

    def two_steps_away(self, other):
        if self.x + 2 == other.x and self.y == other.y:
            return Knot(1, 0)
        elif self.x - 2 == other.x and self.y == other.y:
            return Knot(-1, 0)
        elif self.y + 2 == other.y and self.x == other.x:
            return Knot(0, 1)
        elif self.y - 2 == other.y and self.x == other.x:
            return Knot(0, -1)

        elif self.x + 2 == other.x and self.y != other.y:
            if self.y < other.y:
                return Knot(1, 1)
            else:
                return Knot(1, -1)
        elif self.x - 2 == other.x and self.y != other.y:
            if self.y < other.y:
                return Knot(-1, 1)
            else:
                return Knot(-1, -1)
        elif self.y + 2 == other.y and self.x != other.x:
            if self.x < other.x:
                return Knot(1, 1)
            else:
                return Knot(-1, 1)
        elif self.y - 2 == other.y and self.x != other.x:
            if self.x < other.x:
                return Knot(1, -1)
            else:
                return Knot(-1, -1)

        else:
            Knot(0, 0)


def print_grid(rope: List[Knot]):
    min_x = min([knot.x for knot in rope])
    max_x = max([knot.x for knot in rope])
    min_y = min([knot.y for knot in rope])
    max_y = max([knot.y for knot in rope])

    for y in reversed(range(min([0, min_y]), max([6, max_y]))):
        line = ""
        for x in range(min([0, min_x]), max([6, max_x])):
            if Knot(x, y) in rope:
                line += f"{rope[rope.index(Knot(x,y))].name} "
            else:
                line += ". "
        print(line)

    print()


head = Knot(0, 0, "H")
rope = [head]
rope.extend([Knot(0, 0, i) for i in range(1, 10)])
tail_visited = set()
tail_visited.add(Knot(0, 0))

print("== Initial State ==")
print()
print_grid(rope)
for i, cmd in enumerate(lines):
    direction = cmd.split(" ")[0].strip()
    steps = int(cmd.split(" ")[1].strip())

    for _ in range(0, steps):
        head.move_in_direction(direction)

        for i, knot in enumerate(rope[1:]):
            prev_knot = rope[i]

            if move := knot.two_steps_away(prev_knot):
                knot += move
                if knot == rope[-1]:
                    tail_visited.add(Knot(knot.x, knot.y))


print(f"Positions visited at least once: {len(tail_visited)}")
