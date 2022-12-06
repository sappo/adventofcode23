import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils import read


lines = read.read_puzzle(1)
cals_per_elf = read.group_int_lines(lines)

cal_sums = [sum(cals) for cals in cals_per_elf]

max_cal = max(cal_sums)

print(f"Most cals carried by an elf is: {max_cal}")

top3_cals = sorted(cal_sums, reverse=True)[:3]
cal_sum_top3 = sum(top3_cals)

print(f"Sum of top 3 cals carried by elfs is: {cal_sum_top3}")
