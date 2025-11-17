# Advent of Code 2017 Day 21
# Author:   Rachael Judy
# Purpose:  expanding array art

from collections import Counter
import numpy as np

import parseMod

ready = False
day = 21
stage = 'b'
year = 2017

parseMod.createDataFile(year=year, day=day)

to_str = lambda array: '/'.join(''.join(inner) for inner in array)
to_arr = lambda string:  np.array([list(line) for line in string.split('/')])
rules = {  # all 2x2-> and 3x3-> rules, accounting for flips/rotations
    to_str(arr): v for a, _, v in parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv", ' ')
    for arr in (to_arr(a), np.flip(to_arr(a), axis=0), np.flip(to_arr(a), axis=1), np.flip(to_arr(a), axis=(0, 1)),
                np.rot90(to_arr(a)), np.flip(np.rot90(to_arr(a)), axis=0),
                np.flip(np.rot90(to_arr(a)), axis=1), np.flip(np.rot90(to_arr(a)), axis=(0, 1)))}

# mapping of single steps on independent blocks and of three steps on independent 3x3 blocks
step1 = {rin: (Counter({out: 1}) if rin.count('/') == 1 else Counter([to_str(to_arr(out)[i:i+2,j:j+2]) for i in range(0, 4, 2) for j in range(0, 4, 2)])) for rin, out in rules.items()}
step3 = dict()
for rule in rules:
    if len(rule) > 5:
        blocks2 = np.block([[to_arr(step1[to_str(to_arr(rules[rule])[x:x + 2, y:y + 2])].most_common(1)[0][0])
                             for y in (0, 2)] for x in (0, 2)])  # 6x6
        blocks3 = np.block([[to_arr(step1[to_str(blocks2[x:x + 2, y:y + 2])].most_common(1)[0][0])
                             for y in (0, 2, 4)] for x in (0, 2, 4)])  # 9x9
        step3[rule] = Counter([to_str(blocks3[i:i + 3, j:j + 3]) for i in range(0, 9, 3) for j in range(0, 9, 3)])

# move forward in steps of three as long as possible, then switch to single steps
steps = 18 if stage == 'b' else 5
pattern_counts = Counter({'.#./..#/###': 1})
for _ in range(steps // 3):
    pattern_counts = sum((step3[p] for p in pattern_counts for _ in range(pattern_counts[p])), Counter())
for _ in range(steps % 3):
    pattern_counts = sum((step1[p] for p in pattern_counts for _ in range(pattern_counts[p])), Counter())
result = sum(pattern.count('#') * pattern_counts[pattern] for pattern in pattern_counts)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
