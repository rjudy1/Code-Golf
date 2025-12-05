# Advent of Code 2025 Day 5
# Author:   Rachael Judy
# Purpose:  count numbers in input ranges and inputs in input ranges

import aocd
from mycookie import cookie

ready = True
day = 5
stage = 'a'

data = aocd.get_data(cookie, day, 2025).splitlines()
ranges = sorted([tuple(map(int, ln.split('-'))) for ln in data if '-' in ln])
ids = set(int(ln) for ln in data if ln and '-' not in ln)

folded_ranges, lc, uc = list(), 0, -1
for l, u in ranges:
    if l > uc + 1:
        folded_ranges.append((lc, uc))
        lc = l
    uc = max(u, uc)
folded_ranges.append((lc, uc))

result = sum(l <= id <= u for l, u in folded_ranges for id in ids) if stage == 'a' else sum(u-l+1 for l, u in folded_ranges)

print(f'stage {stage} result (ready={ready}): \n{result}')
if ready:
    aocd.submit(result, part=stage, day=day, year=2025, session=cookie)
