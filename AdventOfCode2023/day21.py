# Advent of Code 2023 Day 21
# Author:   Rachael Judy
# Date:     12/21/23
# Purpose:  Find positions possible at exact number of steps, then with infinite grid from pattern

import parseMod

ready = False
day = 21
stage = 'b'  # 3746, 623540829615589
year = 2023

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")

G = {i+j*1j: c for i,r in enumerate(data) for j,c in enumerate(r) if c in '.S'}  # dictionary of position to value

done = []
todo = {x for x in G if G[x] == 'S'}  # find start with queue
cmod = lambda x: complex(x.real % 131, x.imag % 131)  #

for s in range(3 * len(data)):
    if s == 64 and stage == 'a':
        result = len(todo)
        break
    if s % len(data) == 65: done.append(len(todo)) # dont care about other states
    todo = {p+d for d in {1, -1, 1j, -1j}
                for p in todo if complex((p+d).real % 131, (p+d).imag % 131) in G}

if stage == 'b':
    f = lambda n, a, b, c: a+n*(b-a+(n-1)*(c-b-b+a)//2)
    result = f(26501365 // 131, *done)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
