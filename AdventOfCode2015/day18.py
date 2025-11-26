# Advent of Code 2015 Day 18
# Author:   Rachael Judy
# Purpose:  100 steps of conways

import numpy as np
from scipy.signal import convolve2d

import parseMod

ready = True
day = 18
stage = 'a'
year = 2015

parseMod.createDataFile(year=year, day=day)
data = np.array([[c == '#' for c in row] for row in parseMod.readCSV_row(f"data/{day:02d}data.csv")], dtype=bool)
corner_mask = np.zeros_like(data, dtype=bool)
if stage == 'b':
    data[[0, 0, -1, -1], [0, -1, 0, -1]] = corner_mask[[0, 0, -1, -1], [0, -1, 0, -1]] = True
for _ in range(100):
    data = (data & (((nb := convolve2d(data, np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), mode='same')) == 2) | (nb == 3))) | (~data & (nb == 3)) | corner_mask
result = np.count_nonzero(data)

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
