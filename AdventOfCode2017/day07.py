# Advent of Code 2017 Day 7
# Author:   Rachael Judy
# Purpose:  find the base tower and the one that needs changed for balance

from collections import defaultdict, Counter
from functools import cache

import parseMod

ready = True
day = 7
stage = 'b'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv")

weight_dict, nodes_with_parents, child_tree = dict(), set(), defaultdict(list)
for name, weight, *rest in data:  # process into structures
    weight_dict[name] = int(weight[1:-1])
    if len(rest)>1:
        nodes_with_parents.update(p.strip(',') for p in rest[1:])
        child_tree[name].extend(p.strip(',') for p in rest[1:])
root = set(weight_dict).difference(set(nodes_with_parents)).pop()  # parentless node

# b) with 3+, locate the odd one out; with <=2, have to keep following both paths until one of the subtowers is wrong
queue, current_replacement = [root], None
weigh = cache(lambda node: weight_dict[node] + sum(map(weigh, child_tree[node])))
while queue:
    node = queue.pop(0)
    weights = [weigh(c) for c in child_tree[node]]
    counts = Counter(weights)

    if len(counts) <= 1 or len(weights) == 2:
        queue.extend(child_tree[node])
        continue
    [(common_w, _), (odd_w, _)] = counts.most_common(2)
    current_replacement = weight_dict[child_tree[node][weights.index(odd_w)]] + (common_w - odd_w)
    queue.append(child_tree[node][weights.index(odd_w)])

result = root if stage == 'a' else current_replacement

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
