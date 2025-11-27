# Advent of Code 2015 Day 19
# Author:   Rachael Judy
# Purpose:  expand/reduce string molecule patterns to target

from collections import defaultdict
import functools
import math
import re

import parseMod

ready = False
day = 19
stage = 'b'
year = 2015

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl(f'data/{day:02d}data.csv', ' ')

inverse_swaps = {er:el for el, _, er in data[:-2]}
swaps = defaultdict(set)
for el, _, er in data[:-2]:
    swaps[el].add(er)
new_possible = lambda atom: {atom[:m.span()[0]] + v + atom[m.span()[1]:] for k, vs in swaps.items() for v in vs for m in re.finditer(re.compile(k), atom)}

@functools.cache
def old_possible(curr: str) -> set:
    return {curr[:m.span()[0]] + v + curr[m.span()[1]:] for k, v in inverse_swaps.items() for m in re.finditer(re.compile(k), curr)}

def dfs(curr, target, steps):
    global cache
    if curr == target:
        print(f'dfs found {steps}')
        return steps

    for m in old_possible(curr):
        if m not in cache:
            dfs(m, target, steps+1)
        cache[m] = min(cache[m], steps + 1)

result = len(new_possible(data[-1][0]))
if stage == 'b':
    # hidden grammar design specific approach
    tokens = re.findall(r'[A-Z][a-z]?', data[-1][0])
    result = len(tokens) - tokens.count('Rn') - tokens.count('Ar') - 2*tokens.count('Y') - 1

    # more general approach with massive search space, early discovery of e node depends on arbitrary set order
    # cache = defaultdict(lambda: math.inf)
    # dfs(data[-1][0], 'e', 0)
    # result = len(new_possible(data[-1][0])) if stage == 'a' else cache['e']

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
