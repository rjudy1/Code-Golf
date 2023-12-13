# Advent of Code 2023 Day 13
# Author:   Rachael Judy
# Date:     12/13/23
# Purpose:  find reflecting line, then alternate reflecting line made possible by one change,
# O(patterns * (m^2 n + m n^2)), could convert to bitmap and sum the XOR to be fancy

import parseMod

ready = True
day = 13
stage = 'b'  # 30535, 30844
year = 2023

parseMod.createDataFile(year=year, day=day)
mirrors = parseMod.readCSV_chunk("data/" + str(day).zfill(2) + "data.csv")


def check_horizontal(pattern: list, desired_differences: int = 0):
    for i in range(0, len(pattern) - 1):  # O(m)*O(mn), levenshtein distance per line
        if sum(sum(int(pattern[i-j][k] != pattern[i+j+1][k]) for k in range(len(pattern[0])))
               for j in range(0, min(len(pattern) - i - 1, i + 1))) == desired_differences:
            return i + 1
    return 0


result = sum(100 * check_horizontal(mirror, int(stage == 'b')) + check_horizontal(list(zip(*mirror)), int(stage == 'b'))
             for mirror in mirrors)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
