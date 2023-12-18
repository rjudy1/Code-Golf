# Advent of Code 2023 Day 18
# Author:   Rachael Judy
# Date:     12/18/23
# Purpose:  Shoelace formula for area inside polygon

import parseMod

ready = True
day = 18
stage = 'b'
year = 2023

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv")


def solve(steps):
    corners, pos = list(), (0, 0)
    dirs = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1), '3': (-1, 0), '1': (1, 0), '0': (0, 1), '2': (0, -1)}
    for dir, quant in steps:
        corners.append((pos[0] + int(quant) * dirs[dir][0], pos[1] + int(quant) * dirs[dir][1]))
        pos = (pos[0] + int(quant) * dirs[dir][0], pos[1] + int(quant) * dirs[dir][1])
    return abs(sum(corners[idx][0] * corners[(idx+1)%len(corners)][1]
                   - corners[(idx+1)%len(corners)][0] * corners[idx][1] for idx in range(len(corners)))) // 2\
        + sum(s[1] for s in steps) // 2 + 1  # perimeter


if stage == 'a': result = solve(list((d, int(q)) for d, q, _ in data))
elif stage == 'b': result = solve(list((c[-2], int(c[2:-2], 16)) for _, _, c in data))


if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
