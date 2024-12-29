# Advent of Code 2024 Day 25
# Author:   Rachael Judy
# Purpose:  check if keys will fit in lock holes (not necessarily perfect match though)

import parseMod

ready = False
day = 25
stage = 'a'  # 3269
year = 2024

parseMod.createDataFile(year=year, day=day)
result, processed = 0, list()
for kl in parseMod.readCSV_chunk("data/" + str(day).zfill(2) + "data.csv"):
    blocked = {complex(i, j) for j in range(len(kl[0])) for i in range(len(kl)) if kl[i][j] == '#'}
    result += sum(map(lambda x: not blocked.intersection(x), processed))
    processed.append(blocked)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
