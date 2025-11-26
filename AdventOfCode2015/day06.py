# Advent of Code 2015 Day 6
# Author:   Rachael Judy
# Purpose:  change chunks of values in array

import numpy as np

import parseMod

ready = True
day = 6
stage = 'a'
year = 2015

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl(f'data/{day:02d}data.csv', ' ')

lights = np.zeros((1000, 1000))
for line in data:
    x0, y0 = map(int, line[-3].split(','))
    xf, yf = map(int, line[-1].split(','))
    if line[0] == 'toggle':
        lights[x0:xf + 1, y0:yf + 1] = np.logical_not(lights[x0:xf + 1, y0:yf + 1]) if stage == 'a' else lights[x0:xf + 1, y0:yf + 1] + 2
    elif line[1] == 'off':
        lights[x0:xf + 1, y0:yf + 1] = 0 if stage == 'a' else np.maximum(lights[x0:xf + 1, y0:yf + 1] - 1, 0)
    else:
        lights[x0:xf + 1, y0:yf + 1] = 1 if stage == 'a' else lights[x0:xf + 1, y0:yf + 1] + 1
result = lights.sum()

if not ready:
    print(f'result: \n{result}')
elif ready:
    print('SUBMITTING RESULT: ', result)
    parseMod.submit(result, part=stage, day=day, year=year)
