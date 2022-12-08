# Advent of Code 2022 Day 9
# Author:   Rachael Judy
# Date:     12/9/22
# Purpose:  check visibility from outside and inside grove of trees (dumb n^2 n^3 approach)

import parseMod

stage = 'b'
day = 9
year = 2022
parseMod.createDataFile(year=year, day=day)
trees = [[*map(int, row)] for row in parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")]


if stage == 'a':
    result = sum(sum(row) for row in visible)

else:
    result = max(max(row) for row in scene_score)

print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
