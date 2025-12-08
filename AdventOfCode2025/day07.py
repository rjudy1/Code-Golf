# Advent of Code 2025 Day 7
# Author:   Rachael Judy
# Purpose:  count path splits and unique paths to end

from functools import cache

import aocd
from mycookie import cookie

ready = True
day = 7
stage = 'a'

data = aocd.get_data(cookie, day, 2025).splitlines()

@cache
def traverse_diagram(x, y):
    if y == len(data):
        return 1
    if data[y][x] == '^':
        global splits
        splits += 1
        return traverse_diagram(x - 1, y + 2) + traverse_diagram(x + 1, y + 2)
    return traverse_diagram(x, y + 2)

splits = 0
unique_paths = traverse_diagram(data[0].index('S'), 0)
result = unique_paths if stage == 'b' else splits

print(f'stage {stage} result (ready={ready}): \n{result}')
if ready:
    aocd.submit(result, part=stage, day=day, year=2025, session=cookie)
