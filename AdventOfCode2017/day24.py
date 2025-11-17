# Advent of Code 2017 Day 24
# Author:   Rachael Judy
# Purpose:  build highest strength bridge with two sided nodes (memoized dfs with bitmask)

from collections import defaultdict
from functools import lru_cache

import parseMod

ready = True
day = 24
stage = 'a'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv", '/')

# components and map
comps = [tuple(map(int, c)) for c in data]
port_nb = defaultdict(list, {p: [i for i, (a, b) in enumerate(comps) if p in (a, b)] for p in {x for pair in comps for x in pair}})

@lru_cache
def dfs(open_port=0, mask=(1 << len(comps)) - 1):  # default to starting conditions
    best_str, best_len_str = 0, (0, 0)   # strength, (length, strength)
    for i in port_nb[open_port]:  # check neighbors
        if mask & (1 << i):  # if component unused
            s, (l_len, l_str) = dfs(comps[i][1] if comps[i][0] == open_port else comps[i][0], mask ^ (1 << i))
            best_str, best_len_str = max(s+sum(comps[i]), best_str), max((l_len+1, l_str+sum(comps[i])), best_len_str)
    return best_str, best_len_str


result = dfs()[0] if stage == 'a' else dfs()[1][1]

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
