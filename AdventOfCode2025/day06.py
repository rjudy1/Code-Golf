# Advent of Code 2025 Day 6
# Author:   Rachael Judy
# Purpose:  line and entire input transposed reverse polish

import numpy as np

import aocd
from mycookie import cookie

ready = True
day = 6
stage = 'a'

data = np.array([[*ln] for ln in aocd.get_data(cookie, day, 2025).splitlines()])
sps = [-1, *np.flatnonzero(np.all(data[:-1] == ' ', axis=0)), len(data[0])]

result = int(sum((np.sum if data[-1, sps[j] + 1] == '+' else np.prod)([int(''.join(r)) for r in block], dtype=np.uint64)
                 for j in range(len(sps) - 1)
                 for block in [data[:-1, sps[j] + 1:sps[j + 1]] if stage == 'a' else data[:-1, sps[j] + 1:sps[j + 1]].T]
                 ))

print(f'stage {stage} result (ready={ready}): \n{result}')
if ready:
    aocd.submit(result, part=stage, day=day, year=2025, session=cookie)
