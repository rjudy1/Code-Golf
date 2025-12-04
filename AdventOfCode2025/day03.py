# Advent of Code 2025 Day 3
# Author:   Rachael Judy
# Purpose:  find largest two/twelve digit number formable by pulling from string of numbers without changing order

import aocd
from mycookie import cookie

ready = True
day = 3
stage = 'a'

data = list(map(lambda line: list(map(int, line)), aocd.get_data(cookie, day, 2025).split('\n')))
jlt = lambda ns, dg, di=0: 10**(dg-1)*(f:=max(ns[di:len(ns)-dg+1])) + jlt(ns, dg-1, ns.index(f, di)+1) if dg != 0 else 0
result = sum(jlt(ns, 12 if stage == 'b' else 2) for ns in data)

print(f'stage {stage} result (ready={ready}): \n{result}')
if ready:
    aocd.submit(result, part=stage, day=day, year=2025, session=cookie)
