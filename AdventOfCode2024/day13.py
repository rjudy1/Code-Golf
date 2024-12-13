# Advent of Code 2024 Day 13
# Author:   Rachael Judy
# Purpose:  solve two variable system of equations (kind to have made pairs of buttons linearly independent,
#               and i guess estimate 100 for a was just for the combinatorial brute force people?)


import csv
import numpy as np

import parseMod

ready = True
day = 13
stage = 'b'  # 31897, 87596249540359
year = 2024

parseMod.createDataFile(year=year, day=day)
result = 0
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    reader = csv.reader(file, delimiter='\n')
    linear_equations = list()
    equation = np.zeros((2, 2))
    for i, row in enumerate(reader):
        if i % 4 == 3:
            equation = np.zeros((2,2))
            continue
        values = row[0].split()
        if i % 4 == 2:
            c = [int(values[1][2:-1])+(1e13 if stage == 'b' else 0), int(values[2][2:])+(1e13 if stage == 'b' else 0)]
            a, b = (np.linalg.solve(equation, c))  # I could solve the system of equations myself but why bother
            if 0 < a and 0 < b and np.array_equal(equation @ np.array([int(round(a)), int(round(b))]), c):  # correct float errors
                result += round(a) * 3 + round(b)
        else:
            equation[0:2, i % 4] = [int(values[2][2:-1]), int(values[3][2:])]

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
