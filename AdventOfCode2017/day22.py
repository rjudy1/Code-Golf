# Advent of Code 2017 Day 22
# Author:   Rachael Judy
# Purpose:  simulation of virus spread with nodes changing state upon encounter

from collections import defaultdict
import parseMod

ready = True
day = 22
stage = 'b'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")

def step(steps, delta):
    p, d = len(data) // 2 + 1j * (len(data[0]) // 2), -1
    grid = defaultdict(int, {(i + j * 1j): 2 * int(data[i][j] == '#')
                             for i in range(len(data)) for j in range(len(data[i]))})
    ds = {0: 1j, 1: 1, 2: -1j, 3: -1}  # clean: left, weak: straight, infected: right, flagged: turn around
    for _ in range(steps):
        d *= ds[grid[p]]
        grid[p] = (grid[p] + delta) % 4
        yield grid[p] == 2
        p += d
result = sum(step(10_000 if stage=='a' else 10_000_000, int(stage == 'a')+1))

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
