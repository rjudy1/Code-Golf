# Advent of Code 2016 Day 1
# Author:   Rachael Judy
# Purpose:  follow turn and move instructions, tracking visited


import parseMod

ready = False
day = 1
stage = 'a'
year = 2016

parseMod.createDataFile(year=year, day=day)
data = [x.strip() for x in parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv", ',')[0]]

pos, dir, visited = 0+0j, -1, {0}
for instr in data:
    dir *= -1j if instr[0]=='R' else 1j
    for i in range(int(instr[1:])):
        pos += dir
        if stage=='b' and pos in visited:
            result = abs(pos.real) + abs(pos.imag)
            break
        visited.add(pos)
    else:
        continue
    break
result = abs(pos.real) + abs(pos.imag) if stage == 'a' else result

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
