# Advent of Code 2017 Day 13
# Author:   Rachael Judy
# Purpose:  moving scanners catching along top file

import parseMod

ready = False
day = 13
stage = 'b'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv")

scanners = {int(d.strip(':')): int(r) for d, r in data}
periods = {depth: 2 * (rng - 1) for depth, rng in scanners.items()}
if stage == 'a':
    result = sum(depth * rng for depth, rng in scanners.items() if depth % periods[depth] == 0)
else:
    for delay in range(100_000_000):
        if all((depth + delay) % period != 0 for depth, period in periods.items()):
            result = delay
            break

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
