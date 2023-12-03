# Advent of Code 2023 Day 3
# Author:   Rachael Judy
# Date:     12/3/23
# Purpose:  parse numbers from lines of numbers and symbols

from collections import defaultdict
import math

import parseMod

ready = True
day = 3
stage = 'b'

year = 2023

parseMod.createDataFile(year=year, day=day)
array = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")

in_range = lambda r, c: 0 <= r < len(array) and 0 <= c < len(array[0])
result, asterick_adjacencies = 0, defaultdict(lambda: list())
for row, line in enumerate(array):
    temp, found_symbol, astericks = '', False, set()
    for col, letter in enumerate(line):
        if letter.isdigit():  # collect numbers from array
            temp += letter
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                if in_range(row + dx, col + dy) and not array[row + dx][col + dy].isdigit()\
                        and array[row + dx][col + dy] != '.':
                    if array[row + dx][col + dy] == '*':
                        astericks.add((row + dx, col + dy))
                    found_symbol = True
        if (col == len(line) - 1 or not letter.isdigit()) and temp != '':
            if found_symbol and stage == 'a':  # stage a sums digits
                result += int(temp)
            for a in astericks:  # stage b stores adjacent numbers to astericks
                asterick_adjacencies[a].append(int(temp))
            temp, found_symbol, astericks = '', False, set()

if stage == 'b':
    result = sum((math.prod(asterick_adjacencies[a]) if len(asterick_adjacencies[a]) == 2 else 0) for a in asterick_adjacencies)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
