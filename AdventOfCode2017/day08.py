# Advent of Code 2017 Day 8
# Author:   Rachael Judy
# Purpose:  CPU instructions, find max register

from collections import defaultdict

import parseMod

ready = False
day = 8
stage = 'b'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv")

regs, result = defaultdict(int), 0
for r, op, m, _, rc, opc, mc in data:
    regs[r] += (int(m) if op == 'inc' else -int(m)) if eval(f'{regs[rc]}{opc}{mc}') else 0  # eval slow/unsafe but for the compactness
    result = max(result, regs[r])
result = max(regs.values()) if stage == 'a' else result

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
