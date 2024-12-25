# Advent of Code 2024 Day 19
# Author:   Rachael Judy
# Purpose:  find out if patterns possible from subpatterns (regex easy for 1, dp works for both)

import functools
import re
import parseMod

ready = False
day = 19
stage = 'a'  # 220, 565600047715343
year = 2024

parseMod.createDataFile(year=year, day=day)
available, desired = parseMod.readCSV_chunk("data/" + str(day).zfill(2) + "data.csv")
available = {a.strip() for a in available[0].split(',')}

if stage == 'a':
    result = sum(1 for design in desired if re.fullmatch(re.compile('(' + '|'.join(available) + ')+'), design))
else:
    @functools.cache
    def dp(design):  # take possible prefixes
        return 1 if design == "" else sum(dp(design[len(p):]) for p in available if design.startswith(p))

    result = sum(dp(design) for design in desired)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
