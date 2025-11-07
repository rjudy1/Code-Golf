# Advent of Code 2017 Day 15
# Author:   Rachael Judy
# Purpose:  generators (story and implementation)


import parseMod

ready = True
day = 15
stage = 'b'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv")


def generator(seed: int, factor: int, mod: int = 1) -> int:
    while True:
        seed = seed * factor % 2147483647
        if seed % mod == 0:
            yield seed & 0xffff


A, B = int(data[0][-1]), int(data[1][-1])
if stage == 'a':
    gA, gB = generator(A, 16807), generator(B, 48271)
else:
    gA, gB = generator(A, 16807, 4), generator(B, 48271, 8)
result = sum(next(gA) == next(gB) for _ in range(40000000 if stage == 'a' else 5000000))

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
