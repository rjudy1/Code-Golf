# Advent of Code 2017 Day 2
# Author:   Rachael Judy
# Purpose:  sum difference of largest and smallest values and then quotient of divisible numbers in row

import numpy as np

import parseMod

ready = True
day = 2
stage = 'b'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = np.array(parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv", delim='\t'), dtype=int)
print(data)

# r c^2 for b
result = sum(max(row)-min(row) for row in data) if stage == 'a' else\
    sum(max(row[i], row[j]) // min(row[i], row[j]) for row in data
        for i in range(len(row)) for j in range(i+1, len(row)) if max(row[i], row[j]) % min(row[i], row[j]) == 0)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
