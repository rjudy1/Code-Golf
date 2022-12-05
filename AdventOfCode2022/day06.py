# Advent of Code 2022 Day 6
# Author:   Rachael Judy
# Date:     12/6/22
# Purpose:

import parseMod

stage = 'a'
day = 6
year = 2022

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")

if stage == 'a':
    pass
else:
    pass

print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
