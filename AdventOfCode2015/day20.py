# Advent of Code 2015 Day 20
# Author:   Rachael Judy
# Purpose:  count house gifts from elves that deliver only to multiples of their id

import parseMod

ready = False
day = 20
stage = 'b'
year = 2015

parseMod.createDataFile(year=year, day=day)
data = int(parseMod.readCSV_row(f'data/{day:02d}data.csv', ' ')[0])

presents = [0] * (data // 10 + 1)
for elf in range(1, len(presents)):
    for house in range(elf, min(len(presents), elf * (50 if stage != 'a' else float('inf')) + 1), elf):
        presents[house] += (10 if stage == 'a' else 11) * elf
result = next(i for i, v in enumerate(presents) if v >= data)

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
