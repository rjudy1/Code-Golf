# Advent of Code 2016 Day 10
# Author:   Rachael Judy
# Purpose:  bots passing to fixed neighbors based on magnitude, find output bot and specific interaction

from collections import deque, defaultdict

import parseMod

ready = True
day = 10
stage = 'b'
year = 2016

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl('data/' + str(day).zfill(2) + 'data.csv', ' ')

storage = defaultdict(list)
[storage[l[4]+l[5]].append(int(l[1])) for l in data if l[0] == 'value']
dests = {l[0]+l[1]: (l[5]+l[6], l[10] + l[11]) for l in data if len(l) > 6}
queue = deque([key for key in storage if len(storage[key])>=2])
while queue:
    lowt, uppt = dests[bot := queue.popleft()]
    storage[lowt].append(low := min(storage[bot]))
    storage[uppt].append(high := max(storage[bot]))
    if low == 17 and high == 61 and stage == 'a':
        break
    if len(storage[lowt]) == 2 and not lowt.startswith('output'):
        queue.append(lowt)
    if len(storage[uppt]) == 2 and not uppt.startswith('output'):
        queue.append(uppt)
    storage[bot].clear()
result = bot.removeprefix('bot') if stage == 'a' else storage['output0'][0]*storage['output1'][0]*storage['output2'][0]

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
