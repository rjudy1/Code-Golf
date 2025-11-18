# Advent of Code 2016 Day 3
# Author:   Rachael Judy
# Purpose:  triangle inequality checks

import numpy as np

import parseMod

ready = True
day = 3
stage = 'b'
year = 2016

parseMod.createDataFile(year=year, day=day)
data = np.array([list(map(int, line.split())) for line in parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")])

vert = data.reshape(-1, 3, 3).transpose(0, 2, 1).reshape(-1, 3)
result = np.sum((data[:, 0] + data[:, 1] > data[:, 2]) & (data[:, 0] + data[:, 2] > data[:, 1]) & (data[:, 1] + data[:, 2] > data[:, 0])) if stage == 'a' \
    else np.sum((vert[:, 0] + vert[:, 1] > vert[:, 2]) & (vert[:, 0] + vert[:, 2] > vert[:, 1]) & (vert[:, 1] + vert[:, 2] > vert[:, 0]))

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
