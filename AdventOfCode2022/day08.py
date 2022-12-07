# Advent of Code 2022 Day 8
# Author:   Rachael Judy
# Date:     12/8/22
# Purpose:

import parseMod

stage = 'a'
day = 8
year = 2022

parseMod.createDataFile(year=year, day=day)
commands = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")


if stage == 'a':
    result = find_result(tree, 100000)
else:
    result = find_resultb(tree, min(30000000, 30000000 - 70000000 + tree.size))

print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
