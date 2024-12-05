# Advent of Code 2024 Day 5
# Author:   Rachael Judy
# Purpose:  given instructions and ordering, build DAG with predecessors, validate and fix order

import collections
import numpy as np
import parseMod

ready = True
day = 5
stage = 'b'  # 5275, 6191
year = 2024

parseMod.createDataFile(year=year, day=day)
rules, instructions = parseMod.readCSV_chunk("data/" + str(day).zfill(2) + "data.csv")
rule_map = collections.defaultdict(lambda: set())
for rule in rules:
    a, b = rule.split('|')
    rule_map[b].add(a)

result = 0  # could make this functional but not a vibe
for line in [i.split(',') for i in instructions]:
    broken = np.count_nonzero([line[i+1] in rule_map[element] for i, element in enumerate(line[:-1])])
    result += (int(line[len(line)//2]) if not broken and stage=='a' else 0) + \
              (int({len(set(line).intersection(rule_map[element])): element for element in line}[len(line) // 2]) if broken and stage == 'b' else 0)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
