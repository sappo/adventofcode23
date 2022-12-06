from typing import List

EMPTY_LINE = "\n"


def read_puzzle(day: int):
    with open(f"{day}/input", "r") as puzzle:
        lines = puzzle.readlines()

    return [line for line in lines]


def group_int_lines(lines: List[str]) -> List[List[int]]:
    empty_lines = lines.count(EMPTY_LINE)
    grouped_lines: List[List[int]] = [[] for _ in range(empty_lines + 1)]
    group_index = 0
    for line in lines:
        if line == EMPTY_LINE:
            group_index += 1
        else:
            grouped_lines[group_index].append(int(line.strip(" \n")))

    return grouped_lines
