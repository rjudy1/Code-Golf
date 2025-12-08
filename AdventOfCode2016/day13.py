# Advent of Code 2016 Day 13
# Author:   Rachael Judy
# Purpose:  infinite positive maze min steps to target and distinct reachable locations

from collections import deque

import parseMod

ready = True
day = 13
stage = 'b'
year = 2016

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSVInts('data/' + str(day).zfill(2) + 'data.csv')[0]

q, vis = deque([(1 + 1j, 0)]), {1 + 1j}
is_clear = lambda p, fav: bin(int((x:=p.real)*x + 3*x + 2*x*(y:=p.imag) + y + y*y + fav))[2::].count('1') % 2 == 0
while q:
    pos, steps = q.popleft()
    if stage == 'a' and pos == 31+39j:  break
    if stage == 'b' and steps == 50:    continue
    for dx in {1j, -1j, 1, -1}:
        if (pos+dx).real >= 0 and (pos+dx).imag >= 0 and pos+dx not in vis and is_clear(pos+dx, data):
            q.append((pos+dx, steps+1))
            vis.add(pos+dx)
result = len(vis) if stage == 'b' else steps

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
