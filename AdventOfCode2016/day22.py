# Advent of Code 2016 Day 22
# Author:   Rachael Judy
# Purpose:  in grid of moveable/nonmovable nodes, find initial viable swaps and slide target piece into position

from collections import namedtuple, deque
from itertools import combinations

import parseMod

ready = True
day = 22
stage = 'b'
year = 2016

parseMod.createDataFile(year=year, day=day)
data = [[a.strip('T%') for a in ln.split()] for ln in parseMod.readCSV_row('data/' + str(day).zfill(2) + 'data.csv')]

Edge = namedtuple('Edge', ['sz', 'usd', 'opn'])
nodes = dict()
for ln in data[2:]:
    _, x, y = ln[0].split('-')
    nodes[int(x[1:])+1j*int(y[1:])] = Edge(int(ln[1]), int(ln[2]), int(ln[3]))

maxx, maxy = max(nodes, key=abs).real, max(nodes, key=abs).imag
data_loc = max(nodes, key=lambda n: n.real * int(n.imag == 0))
empty_pos = list(filter(lambda n: nodes[n].usd == 0, nodes))[0]
unmovable = set(p for p, n in nodes.items() if n.usd > nodes[empty_pos].sz)
q, v = deque([(empty_pos, data_loc, 0)]), {(empty_pos, data_loc)}
while q:
    emp, tloc, mv = q.popleft()
    if tloc == 0:  # accessible data
        break
    for dx in [1j, -1j, 1, -1]:
        if 0 <= (np := emp+dx).real <= maxx and 0 <= np.imag <= maxy \
                and (np, nt := emp if np == tloc else tloc) not in v and np not in unmovable:
            q.append((np, nt, mv+1))
            v.add((np, nt))

result = sum(0 < a.usd < b.opn or 0 < b.usd < a.opn for a, b in combinations(nodes.values(), 2)) if stage == 'a' else mv
print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
