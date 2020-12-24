# Advent of Code 2018 - Day 12

# Author:   Rachael Judy
# Date:     12/24/2020
# Purpose:  Perform extension of generations of plants (after generation 97 sum increases by 80 each generation
#           - print your pattern results to get your own increment) - look for ADJUST comment for things to change

import copy
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

inp = parseMod.readCSV_row('data/12pattern.csv', '\n')  # ADJUST
inc = 80  # ADJUST

initial = ['.' for _ in range(500)] + list(inp[0][15:]) + ['.' for _ in range(500)]
rules = {}
for line in inp[1:]:
    rules[line.split()[0]] = line.split()[2]


def calc_value(generations, initial):
    base = inc*(generations - (generations if generations <= 100 else 100))
    for i in range(generations if generations <= 100 else 100):
        current_config = copy.deepcopy(initial)
        for shift in range(2, len(initial)-2):
            current_config[shift] = rules[''.join(initial[shift-2:shift+3])]
        initial = copy.deepcopy(current_config)
        # print(sum((i-500) if c == '#' else 0 for i, c in enumerate(initial)) + base, i+1)  # ADJUST uncomment to see

    return sum((i-500) if c == '#' else 0 for i, c in enumerate(initial)) + base


print('part 1: ', calc_value(20, initial))
print('part 2: ', calc_value(50000000000, initial))  # start by testing 100 to see your inc and adjust inc  # ADJUST
