# Advent of Code 2023 Day 19
# Author:   Rachael Judy
# Date:     12/19/23
# Purpose:  Split ranges based on sequential conditionals (kind of obnoxious conditional/loop set up)

from collections import defaultdict
import math
import parseMod

ready = True
day = 19
stage = 'a'
year = 2023

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_chunk("data/" + str(day).zfill(2) + "data.csv")

workflow_ranges = defaultdict(lambda: list())  # splits from each workflow
order = ['x', 'm', 'a', 's']
for row in data[0]:
    ranges_to_split = [((1, 4000), (1, 4000), (1, 4000), (1, 4000))]  # each starts with full range to sort
    for rule in row.split('{')[1][:-1].split(','):
        if ':' not in rule:
            workflow_ranges[row.split('{')[0]].extend([(*group, rule) for group in ranges_to_split])
        else:
            comp, dest = rule.split(':')
            new_ranges = list()
            for group in ranges_to_split:
                if group[order.index(rule[0])][0] <= int(comp[2:]) <= group[order.index(rule[0])][1]:
                    if comp[1] == '<':
                        workflow_ranges[row.split('{')[0]].append((*((group[i][0], int(comp[2:]) - 1) if order.index(rule[0]) == i else group[i] for i in range(4)), dest))
                        new_ranges.append(tuple((int(comp[2:]), group[i][1]) if order.index(rule[0]) == i else group[i] for i in range(4)))
                    elif comp[1] == '>':
                        workflow_ranges[row.split('{')[0]].append((*((int(comp[2:]) + 1, group[order.index(rule[0])][1]) if order.index(rule[0]) == i else group[i] for i in range(4)), dest))
                        new_ranges.append(tuple((group[order.index(rule[0])][0], int(comp[2:])) if order.index(rule[0]) == i else group[i] for i in range(4)))
            ranges_to_split = new_ranges

queue = [*workflow_ranges['in']]
accepted_ranges = set()
while len(queue):  # split ranges starting from 'in'
    xr, mr, ar, sr, dest = queue.pop(0)
    bounds = [xr, mr, ar, sr]
    if dest == 'A':
        accepted_ranges.add((xr, mr, ar, sr))
        continue
    elif dest == 'R':
        continue

    end_loop = False
    for group in workflow_ranges[dest]:
        if group[0][0] <= xr[0] and xr[1] <= group[0][1] and group[1][0] <= mr[0] and mr[1] <= group[1][1] \
                and group[2][0] <= ar[0] and ar[1] <= group[2][1] and group[3][0] <= sr[0] and sr[1] <= group[3][1]:
            queue.append((xr, mr, ar, sr, group[4]))  # fully contained, follow path
            break

        for i in range(4):  # find first difference to be split and queue it
            if group[i][0] <= bounds[i][0] <= group[i][1] < bounds[i][1]:
                queue.append(tuple([*(bounds[j] for j in range(i)), (bounds[i][0], group[i][1]), *(bounds[j] for j in range(i+1, 4)), group[4]]))
                queue.append(tuple([*(bounds[j] for j in range(i)), (group[i][1] + 1, bounds[i][1]), *(bounds[j] for j in range(i+1, 4)), dest]))
            elif bounds[i][0] < group[i][0] <= group[i][1] < bounds[i][1]:
                queue.append(tuple([*(bounds[j] for j in range(i)), (bounds[i][0], group[i][0] - 1), *(bounds[j] for j in range(i+1, 4)), dest]))
                queue.append(tuple([*(bounds[j] for j in range(i)), (group[i][0], group[i][1]), *(bounds[j] for j in range(i+1, 4)), group[4]]))
                queue.append(tuple([*(bounds[j] for j in range(i)), (group[i][1] + 1, bounds[i][1]), *(bounds[j] for j in range(i+1, 4)), dest]))
            elif bounds[i][0] < group[i][0] <= bounds[i][1] <= group[i][1]:
                queue.append(tuple([*(bounds[j] for j in range(i)), (bounds[i][0], group[i][0] - 1), *(bounds[j] for j in range(i+1, 4)), dest]))
                queue.append(tuple([*(bounds[j] for j in range(i)), (group[i][0], bounds[i][1]), *(bounds[j] for j in range(i+1, 4)), group[4]]))

            if group[i][0] <= bounds[i][0] <= group[i][1] < bounds[i][1] or\
                    bounds[i][0] < group[i][0] <= group[i][1] < bounds[i][1] or\
                    bounds[i][0] < group[i][0] <= bounds[i][1] <= group[i][1]:
                end_loop = True
                break
        if end_loop:
            break

if stage == 'a':
    result = 0
    for row in data[1]:
        x, m, a, s = (int(key.split('=')[1]) for key in row[1:-1].split(','))
        for group in accepted_ranges:
            if group[0][0] <= x <= group[0][1] and group[1][0] <= m <= group[1][1] \
                    and group[2][0] <= a <= group[2][1] and group[3][0] <= s <= group[3][1]:  # if all match
                result += x+m+a+s
                break
else:
    result = 0
    for group in accepted_ranges:
        result += math.prod(group[i][1] - group[i][0] + 1 for i in range(4))

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
