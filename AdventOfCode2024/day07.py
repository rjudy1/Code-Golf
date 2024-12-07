# Advent of Code 2024 Day 7
# Author:   Rachael Judy
# Purpose:  find combination of operators (+,*,||) that make equations work (exponential horrificness)

import csv
import numpy as np

import parseMod

ready = True
day = 7
stage = 'b'
year = 2024

parseMod.createDataFile(year=year, day=day)
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    reader = csv.reader(file)
    equations = [row[0] for row in reader]

base = 2 if stage=='a' else 3
result = 0
for row in equations:
    a, operands = int(row.split(':')[0]), [int(o) for o in row.split(':')[1].split()]
    for i in range(base**(len(operands)-1)):
        # i to binary/ternary, 0s become mults, 1s become pluses, 2s become concats
        val = operands[0]
        for j, digit in enumerate(np.base_repr(i, base=base, padding=len(operands))[-len(operands)+1:]):
            if digit == '0':
                val *= operands[j+1]
            elif digit == '1':
                val += operands[j+1]
            else:
                val = int(''.join([str(val), str(operands[j + 1])]))
        if val == a:
            result += a
            break

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
