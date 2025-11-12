# Advent of Code 2017 Day 23
# Author:   Rachael Judy
# Purpose:  count composites in a range (disguised as jumbled assembly)

import sympy

import parseMod

ready = True
day = 23
stage = 'a'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv", ' ')

# examination of assembly and running d18 cpu leads to reduction to composite count assuming everyone has same program with different b
result = (int(data[0][2])-2)**2 if stage == 'a' else\
    sum(not sympy.isprime(b) for b in range(int(data[0][2])*100+100000, int(data[0][2])*100+117001, -int(data[-2][2])))

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
