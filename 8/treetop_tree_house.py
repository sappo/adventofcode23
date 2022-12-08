import os
import sys
import pprint
from typing import List

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils import read

pp = pprint.PrettyPrinter(indent=2)

lines: List[str] = read.read_puzzle(8)

tree_grid = []
for line in lines:
    tree_grid.append([c for c in line.strip()])

pp.pprint(tree_grid)


def is_outer(grid: List[List[int]], x: int, y: int) -> bool:
    if x == 0 or y == 0:
        return True
    elif x == len(grid[0]) - 1 or y == len(grid) - 1:
        return True
    else:
        return False


def is_visible_from_the_left(grid: List[List[int]], x: int, y: int) -> bool:
    tree_size = grid[y][x]
    for i in range(0, x):
        print(f"{grid[y][i]} >= {tree_size}")
        if grid[y][i] >= tree_size:
            return False

    return True


def visible_trees_to_the_left(grid: List[List[int]], x: int, y: int) -> int:
    tree_size = grid[y][x]
    count = 0
    for i in reversed(range(0, x)):
        count += 1
        if grid[y][i] >= tree_size:
            break

    print(f"Visible tree lef {count}")
    return count


def is_visible_from_the_right(grid: List[List[int]], x: int, y: int) -> bool:
    tree_size = grid[y][x]
    for i in range(x + 1, len(grid[y])):
        if grid[y][i] >= tree_size:
            return False

    return True


def visible_trees_to_the_right(grid: List[List[int]], x: int, y: int) -> int:
    tree_size = grid[y][x]
    count = 0
    for i in range(x + 1, len(grid[y])):
        count += 1
        if grid[y][i] >= tree_size:
            break

    print(f"Visible tree rig {count}")
    return count


def is_visible_from_the_top(grid: List[List[int]], x: int, y: int) -> bool:
    tree_size = grid[y][x]
    for i in range(0, y):
        if grid[i][x] >= tree_size:
            return False

    return True


def visible_trees_to_the_top(grid: List[List[int]], x: int, y: int) -> int:
    tree_size = grid[y][x]
    count = 0
    for i in reversed(range(0, y)):
        count += 1
        if grid[i][x] >= tree_size:
            break

    print(f"Visible tree top {count}")
    return count


def is_visible_from_the_bottom(grid: List[List[int]], x: int, y: int) -> bool:
    tree_size = grid[y][x]
    for i in range(y + 1, len(grid)):
        if grid[i][x] >= tree_size:
            return False

    return True


def visible_trees_to_the_bottom(grid: List[List[int]], x: int, y: int) -> int:
    tree_size = grid[y][x]
    count = 0
    for i in range(y + 1, len(grid)):
        count += 1
        if grid[i][x] >= tree_size:
            break

    print(f"Visible tree bot {count}")
    return count


def is_visible(grid: List[List[int]], x: int, y: int) -> bool:
    if is_outer(grid, x, y):
        return True
    elif is_visible_from_the_left(grid, x, y):
        return True
    elif is_visible_from_the_right(grid, x, y):
        return True
    elif is_visible_from_the_top(grid, x, y):
        return True
    elif is_visible_from_the_bottom(grid, x, y):
        return True
    else:
        return False


def scenic_score(grid: List[List[int]], x: int, y: int):
    score = 1
    score *= visible_trees_to_the_left(grid, x, y)
    score *= visible_trees_to_the_right(grid, x, y)
    score *= visible_trees_to_the_top(grid, x, y)
    score *= visible_trees_to_the_bottom(grid, x, y)
    return score


visible_trees = 0
for y in range(0, len(tree_grid)):
    for x in range(0, len(tree_grid[0])):
        if is_visible(tree_grid, x, y):
            visible_trees += 1

print(f"No of visible_trees are: {visible_trees}")


max_scenic_score = 0
for y in range(0, len(tree_grid)):
    for x in range(0, len(tree_grid[0])):
        score = scenic_score(tree_grid, x, y)
        print(f"Scenic score for {tree_grid[y][x]}: {score}")
        max_scenic_score = max([max_scenic_score, score])

print(f"The highest scenic score is: {max_scenic_score}")
