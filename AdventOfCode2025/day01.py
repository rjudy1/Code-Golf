# Advent of Code 2025 Day 1
# Author:   Rachael Judy
# Purpose:  count turns of 100 tick dial that land on/pass zero

import aocd
from mycookie import cookie

ready = True
day = 1
stage = 'b'

data = aocd.get_data(cookie, day, 2025).split('\n')

p, result = 50, 0
for t in data:
    p += (dp := -int(t[1:]) if t[0] == 'L' else int(t[1:]))
    result += stage == 'a' and p % 100 == 0 or (stage == 'b' and (p <= 0 or p >= 100)) * (abs(p) // 100 + (0 >= p != dp))
    p %= 100

print(f'result: \n{result}; ready={ready}')
if ready:
    aocd.submit(result, part=stage, day=day, year=2025, session=cookie)
