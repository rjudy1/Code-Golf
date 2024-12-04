# Advent of Code 2024 Day 4
# Author:   Rachael Judy
# Purpose:  Find patterns in word search O(n^2)

import csv
import parseMod

ready = True
day = 4
stage = 'a'  # 2514, 1888
year = 2024

parseMod.createDataFile(year=year, day=day)
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    reader = csv.reader(file)
    grid = [row[0] for row in reader]

result = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if stage == 'a':
            # horizontal
            if j + 3 < len(grid[0]) and (''.join(grid[i][j:j + 4]) == 'XMAS' or ''.join(grid[i][j:j + 4]) == 'SAMX'):
                result += 1  # could use regex for this, then transpose and regex again for vertical
            # vertical
            if i + 3 < len(grid) and\
                    (''.join([grid[i][j], grid[i + 1][j], grid[i + 2][j], grid[i + 3][j]]) == 'XMAS' or
                     ''.join([grid[i][j], grid[i + 1][j], grid[i + 2][j], grid[i + 3][j]]) == 'SAMX'):
                result += 1
            # backslash diagonal
            if i + 3 < len(grid) and j + 3 < len(grid[0]) and\
                    (''.join([grid[i][j], grid[i + 1][j + 1], grid[i + 2][j + 2], grid[i + 3][j + 3]]) == 'XMAS' or
                     ''.join([grid[i][j], grid[i + 1][j + 1], grid[i + 2][j + 2], grid[i + 3][j + 3]]) == 'SAMX'):
                result += 1
            # forward slash diagonal
            if i + 3 < len(grid) and j - 3 >= 0 and\
                    (''.join([grid[i][j], grid[i + 1][j - 1], grid[i + 2][j - 2], grid[i + 3][j - 3]]) == 'XMAS' or
                     ''.join([grid[i][j], grid[i + 1][j - 1], grid[i + 2][j - 2], grid[i + 3][j - 3]]) == 'SAMX'):
                result += 1
        elif stage == 'b':  # check for X-MAS shape
            if i + 2 < len(grid) and j + 2 < len(grid[0]) and\
                    ((''.join([grid[i][j], grid[i + 1][j + 1], grid[i + 2][j + 2]]) == 'MAS' or
                     ''.join([grid[i][j], grid[i + 1][j + 1], grid[i + 2][j + 2]]) == 'SAM') and
                     (''.join([grid[i][j + 2], grid[i + 1][j + 1], grid[i + 2][j]]) == 'MAS' or
                      ''.join([grid[i][j + 2], grid[i + 1][j + 1], grid[i + 2][j]]) == 'SAM')):
                result += 1

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
