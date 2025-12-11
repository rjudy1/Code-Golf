# Advent of Code 2025 Day 11
# Author:   Rachael Judy
# Purpose:  count all paths from source to dest nodes in a graph

from collections import defaultdict
from functools import cache

import aocd
from mycookie import cookie

ready = True
day = 11
stage = 'b'

graph = defaultdict(set, {a.strip(':'): set(nbs) for a, *nbs in (ln.split() for ln in aocd.get_data(cookie, day, 2025).split('\n'))})
@cache
def npaths(n, tar):
    return 1 if n == tar else sum(npaths(c, tar) for c in graph[n])
result = npaths("you","out") if stage=='a' else npaths("svr","fft")* npaths("fft","dac")* npaths("dac","out")

print(f'stage {stage} result (ready={ready}): \n{result}')
if ready:
    aocd.submit(result, part=stage, day=day, year=2025, session=cookie)
