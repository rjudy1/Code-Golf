# Advent of Code 2017 Day 3
# Author:   Rachael Judy
# Purpose:  use incrementing spiral and sum of existing neighbors spiral to find distance to value and value > input

from collections import defaultdict
import math

import parseMod

ready = True
day = 3
stage = 'a'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSVInts("data/" + str(day).zfill(2) + "data.csv")[0]

# no code needed for today but we'll write some for reference
# note sequence of odd squares from bottom right corner, find which side, get distance
if stage == 'a':
    r = math.ceil(math.sqrt(data)) + int(math.ceil(math.sqrt(data)) % 2 == 0)
    lr, s, m = r**2, r - 1, (r - 1) // 2
    result = m + abs(next(c - m - data for c in (lr - i*s for i in range(4)) if data <= c))
else:
    # for b, build the spiral
    x, y, steps, turn = 0, 0, 0, 0
    dirs, visited = [(1, 0), (0, 1), (-1, 0), (0, -1)], defaultdict(int, {(0, 0): 1})
    while True:
        visited[x, y] = sum(visited[x+dx, y+dy] for dx in [-1,0,1] for dy in [-1,0,1])
        if (result:=visited[x, y]) > data:
            break
        x, y = x+dirs[turn%4][0], y+dirs[turn%4][1]
        steps += 1
        if steps == turn//2+1:
            steps = 0
            turn += 1

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
