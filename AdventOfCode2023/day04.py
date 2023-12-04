# Advent of Code 2023 Day 4
# Author:   Rachael Judy
# Date:     12/4/23
# Purpose:  scratchcard scoring based on match count

from collections import defaultdict

import parseMod

ready = True
day = 4
stage = 'b'

year = 2023

parseMod.createDataFile(year=year, day=day)
array = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")
array.reverse()  # key is to go backward for stage b since it always grabs consecutive cards

result, win_count_dict = 0, defaultdict(lambda: 1)
for num_r, card in enumerate(array):
    winning, possessed = card.split(':')[1].split('|')
    matches = set(int(n) for n in winning.strip().split()).intersection(set(int(n) for n in possessed.strip().split()))
    if matches and stage == 'a':
        result += pow(2, len(matches)-1)
    if stage == 'b':
        win_count_dict[len(array) - num_r - 1] += sum(win_count_dict[len(array) - num_r + c] for c in range(len(matches)))
        result += win_count_dict[len(array) - num_r - 1]

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
