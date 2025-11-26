# Advent of Code 2015 Day 3
# Author:   Rachael Judy
# Purpose:  visited locations from steps

import parseMod

ready = True
day = 3
stage = 'b'
year = 2015

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row(f'data/{day:02d}data.csv')[0]

pos, visited = [0, 0] if stage == 'b' else [0], {0}
d = {'^': -1, 'v': 1, '<': -1j, '>': 1j}
for i, s in enumerate(data):
    pos[i & (len(pos)-1)] += d[s]
    visited.update(pos)
result = len(visited)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print('SUBMITTING RESULT: ', result)
    parseMod.submit(result, part=stage, day=day, year=year)
