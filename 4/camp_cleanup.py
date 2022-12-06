import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils import read


pairs = read.read_puzzle(4)


fully_contained_assignments = 0
for pair in pairs:
    pair_assignments = [
        range(int(p.split("-")[0]), int(p.split("-")[1]) + 1) for p in pair.split(",")
    ]

    if set(pair_assignments[0]).issubset(pair_assignments[1]):
        fully_contained_assignments += 1
    elif set(pair_assignments[1]).issubset(pair_assignments[0]):
        fully_contained_assignments += 1

print(f"Number of fully contained assignments is: {fully_contained_assignments}")

overlapping_assignments = 0
for pair in pairs:
    pair_assignments = [
        range(int(p.split("-")[0]), int(p.split("-")[1]) + 1) for p in pair.split(",")
    ]

    if set(pair_assignments[0]).intersection(pair_assignments[1]):
        overlapping_assignments += 1
    elif set(pair_assignments[1]).intersection(pair_assignments[0]):
        overlapping_assignments += 1

print(f"Number of overlapping assignments is: {overlapping_assignments}")
