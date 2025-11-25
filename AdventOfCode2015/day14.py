# Advent of Code 2015 Day 14
# Author:   Rachael Judy
# Purpose:  reindeer positions with rest and speed cycles

from collections import defaultdict, namedtuple

import parseMod

ready = False
day = 14
stage = 'b'
year = 2015

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl('data/' + str(day).zfill(2) + 'data.csv')

Reindeer = namedtuple('Reindeer', ['speed', 'speed_t', 'cycle'])
rd = {l[0]: Reindeer(int(l[3]), int(l[6]), int(l[6]) + int(l[13])) for l in data}
pos = lambda t, r: (t // rd[r].cycle) * rd[r].speed * rd[r].speed_t + rd[r].speed * min(rd[r].speed_t, t % rd[r].cycle)

scores = defaultdict(int)
for t in range(1,2503+1):
    dist = {r: pos(t, r) for r in rd}
    for r in rd:
        scores[r] += 1 if dist[r] == max(dist.values()) else 0
result = max(scores.values()) if stage == 'b' else max(pos(2503, r) for r in rd)

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
