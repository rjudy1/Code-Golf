# Advent of Code 2024 Day 2
# Author:   Rachael Judy
# Purpose:  Filter reports of increasing/decreasing in bounds, brute force

import parseMod
import copy

ready = False
day = 2
stage = 'b'  # 490, 536
year = 2024

parseMod.createDataFile(year=year, day=day)
array = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")


def is_safe(vals):
    if len(vals) <= 1: return True
    if vals[0] == vals[1]: return False
    dir = (vals[1] - vals[0]) / abs(vals[1] - vals[0])
    for i in range(1, len(vals)):
        if abs(vals[i] - vals[i-1]) < 1 or abs(vals[i] - vals[i-1]) > 3 or (vals[i] - vals[i-1])/abs(vals[i] - vals[i-1]) != dir:
            return False
    return True


result = 0
for row in array:
    row_values = [int(r) for r in row.split()]
    if is_safe(row_values): result += 1
    elif stage == 'b':
        for i in range(len(row_values)):
            values = copy.deepcopy(row_values)
            values.pop(i)
            if is_safe(values):
                result += 1
                break

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
