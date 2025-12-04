# Advent of Code 2025 Day 4
# Author:   Rachael Judy
# Purpose:  remove rolls with less than four neighbors repeatedly

import numpy as np
from scipy.signal import convolve2d

import aocd
from mycookie import cookie

ready = True
day = 4
stage = 'b'

data = np.array([[c == '@' for c in l] for l in aocd.get_data(cookie, day, 2025).splitlines()], int)
result = 0
while True:
    data ^= (rem := data & (convolve2d(data, np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), mode='same') < 4))
    result += rem.sum()
    if not rem.any() or stage == 'a': break

print(f'stage {stage} result (ready={ready}): \n{result}')
if ready:
    aocd.submit(result, part=stage, day=day, year=2025, session=cookie)
