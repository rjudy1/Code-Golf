# Advent of Code 2023 Day 11
# Author:   Rachael Judy
# Date:     12/11/23
# Purpose:  find manhattan distance between galaxies with empty rows/cols expanding
# could have been under 15 seconds for b but embarrassingly forgot to subtract 1 (cry)

import itertools
import parseMod

ready = True
day = 11
stage = 'b'
year = 2023

parseMod.createDataFile(year=year, day=day)
map = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")

# store locations of all galaxies and empty rows/cols
galaxies = set()
for i, row in enumerate(map):
    for j, col in enumerate(row):
        if col == '#':
            galaxies.add((i, j))
empty_rows = {i for (i, _) in filter(lambda row: row[1].find('#') == -1, enumerate(map))}
empty_cols = {i for (i, _) in filter(lambda col: ''.join(col[1]).find('#') == -1, enumerate(list(zip(*map))))}

result = 0
expansion = 1 if stage == 'a' else 999999  # expansion_multiplier - 1
for g0, g1 in itertools.combinations(galaxies, 2):
    result += abs(g0[0] - g1[0]) + abs(g0[1] - g1[1]) \
              + sum(expansion if min(g0[0], g1[0]) < row < max(g0[0], g1[0]) else 0 for row in empty_rows) \
              + sum(expansion if min(g0[1], g1[1]) < col < max(g0[1], g1[1]) else 0 for col in empty_cols)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
