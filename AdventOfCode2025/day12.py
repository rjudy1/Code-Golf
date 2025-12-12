# Advent of Code 2025 Day 12
# Author:   Rachael Judy
# Purpose:  tetris required number of different presents in fixed size spaces (the presents are all liquid)

import aocd
from mycookie import cookie

ready = False
day = 12
stage = 'a'

trees, presents, working = set(), {}, 0
for i, ln in enumerate(aocd.get_data(cookie, day, 2025).splitlines()):
    if 'x' in ln:  # area under tree, required presents
        size_raw, *demands = ln.split()
        trees.add((tuple(map(int, size_raw.rstrip(':').split('x'))), tuple(map(int, demands))))
    if not ln:  # blank line, end of present
        presents[len(presents)], working = working, 0
    working += ln.count('#')

result = sum(1 for sz, dmds in trees if sz[0]*sz[1] >= sum(presents[i]*d for i, d in enumerate(dmds)))

print(f'stage {stage} result (ready={ready}): \n{result}')
if ready:
    aocd.submit(result, part=stage, day=day, year=2025, session=cookie)
