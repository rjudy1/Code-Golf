# Advent of Code 2024 Day 3
# Author:   Rachael Judy
# Purpose:  look for regex patterns matching "mul\(\d+,\d+\)", "do\(\)", "don't\(\)" and process

import parseMod
import re

ready = False
day = 3
stage = 'b'  # 189527826, 63013756
year = 2024

parseMod.createDataFile(year=year, day=day)
memory = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")

result = 0
do_flag = True
for row in memory:
    match_map = {i.regs[0][0]: i.regs[0][1] for i in re.finditer("mul\(\\d+,\\d+\)", row)}
    dos = {i.regs[0][0] for i in re.finditer("do\(\)", row)}
    donts = {i.regs[0][0] for i in re.finditer("don't\(\)", row)}

    for i in sorted([*match_map.keys(), *dos, *donts]):
        if i in match_map and (do_flag or stage == 'a'):
            n1, n2 = row[i+4:match_map[i] - 1].split(',')
            result += int(n1) * int(n2)
        else:
            do_flag = (i in dos)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
