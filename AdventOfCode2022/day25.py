# Advent of Code 2022 Day 25
# Author:   Rachael Judy
# Date:     12/25/22
# Purpose:  convert from shifted base 5 to decimal, sum, and shift back

import parseMod
import time
import numpy as np

stage = 'a'
day = 25
year = 2022
parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row(f"data/{str(day).zfill(2)}data.csv")
start = time.time()

# map both ways and total, then convert back to base 5 shifted
base5s = {'2': 2, 2: '2', '1': 1, 1: '1', '0': 0, 0: '0', '-': -1, -1: '-', '=': -2, -2: '='}
total = sum(sum(5 ** (len(row)-1-i) * base5s[row[i]] for i in range(len(row))) for row in data)
base5_total = [0] + [int(x) for x in np.base_repr(total, base=5)]
for i in range(len(base5_total)-1, -1, -1):
    if base5_total[i] > 2:
        base5_total[i] = base5s[base5_total[i] - 5]
        base5_total[i-1] += 1

result = ''.join(str(n) for n in (base5_total if base5_total[0] != 0 else base5_total[1:]))
print(f"Time: {time.time() - start}")
print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
