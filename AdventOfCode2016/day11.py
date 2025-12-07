# Advent of Code 2016 Day 11
# Author:   Rachael Judy
# Purpose:  bfs min steps to move items to a top floor without keeping invalid pairs together per step

from collections import deque
from itertools import combinations
import re

import parseMod

ready = True
day = 11
stage = 'a'
year = 2016

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row('data/' + str(day).zfill(2) + 'data.csv')

def bfs(initial_pairs):
    is_safe = lambda pairs: all(not ({i for i, (g, _) in enumerate(pairs) if g == f})
                                or all(pairs[c][0] == f for c in {i for i, (_, c) in enumerate(pairs) if c == f})
                                for f in range(4))

    q, vis = deque([(start_state := (tuple(sorted(initial_pairs)), 0), 0)]), {start_state}
    while q:
        (pairs, elv), steps = q.popleft()
        if pairs == tuple((3, 3) for _ in initial_pairs) and elv == 3:
            return steps

        items = [(i, "G") for i, (g, _) in enumerate(pairs) if g == elv] + [(i, "M") for i, (_, m) in enumerate(pairs) if m == elv]
        for move in list(combinations(items, 1)) + list(combinations(items, 2)):
            for nfl in (elv + 1, elv - 1):
                new_pairs = tuple(tuple(nfl if (i, 'G' if j == 0 else 'M') in move else v for j, v in enumerate(p)) for i, p in enumerate(pairs))
                if 0 <= nfl <= 3 and is_safe(new_pairs) and (state := (tuple(sorted(new_pairs)), nfl)) not in vis:
                    vis.add(state)
                    q.append((state, steps + 1))

gens = {m.group(1): fl for fl, ln in enumerate(data) for m in re.finditer(r"(\w+) generator", ln)}
chips = {m.group(1): fl for fl, ln in enumerate(data) for m in re.finditer(r"(\w+)-compatible microchip", ln)}
pairs = list((gens[el], chips[el]) for el in sorted(chips))
if stage == 'b':  # add bonus elements
    pairs.append((0, 0))
    pairs.append((0, 0))
result = bfs(pairs)

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
