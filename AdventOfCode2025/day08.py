# Advent of Code 2025 Day 8
# Author:   Rachael Judy
# Purpose:  count path splits and unique paths to end

from itertools import combinations
import math
import networkx as nx

import aocd
from mycookie import cookie

ready = True
day = 8
stage = 'b'

data = [[*map(int, ln.split(','))] for ln in aocd.get_data(cookie, day, 2025).splitlines()]
CG = nx.Graph()
for a, b in sorted(combinations(map(tuple, data), 2), key=lambda p: sum((ai-bi)**2 for ai, bi in zip(p[0], p[1]))):
    CG.add_edge(a, b)
    if stage == 'a' and CG.size() == 1000 or nx.number_connected_components(CG) == 1 and len(CG) == len(data): break
result = math.prod(len(sg) for sg in sorted(nx.connected_components(CG), key=len)[-3:]) if stage == 'a' else a[0] * b[0]

print(f'stage {stage} result (ready={ready}): \n{result}')
if ready:
    aocd.submit(result, part=stage, day=day, year=2025, session=cookie)
