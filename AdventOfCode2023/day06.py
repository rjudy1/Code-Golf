# Advent of Code 2023 Day 6
# Author:   Rachael Judy
# Date:     12/6/23
# Purpose:  use rootfinder for dist_traveled = time_held * (time - time_held) > distance, find time_held

import math
import numpy as np

import parseMod

ready = True
day = 6
stage = 'b'

year = 2023

parseMod.createDataFile(year=year, day=day)
array = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")

times_str, distances_str = array[0].strip().split()[1:], array[1].strip().split()[1:]
if stage == 'b':
    times_str, distances_str = [''.join(times_str)],  [''.join(distances_str)]

# solving -x^2 + time * x - distance = 0, return number of whole numbers between roots
result = math.prod(math.ceil(max(np.roots([-1, int(time), -int(distance)])))
                   - math.floor(min(np.roots([-1, int(time), -int(distance)]))) - 1
                   for time, distance in zip(times_str, distances_str))

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
