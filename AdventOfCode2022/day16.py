# Advent of Code 2022 Day 16
# Author:   Rachael Judy
# Date:     12/16/22
# Purpose:  djikstra preliminary filter to map, dfs with memoization of sequences, then find best combos in cache

import parseMod
import time

stage = 'b'
day = 16
year = 2022
parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")
start = time.time()
cache = dict()


def djikstra(tree, initial_node):
    costs = {v: 100 if v != initial_node else 0 for v in valves}
    to_explore = [initial_node]
    while len(to_explore):
        for path in tree[to_explore[0]]["paths"]:
            if costs[path] > costs[to_explore[0]]+1:
                costs[path] = costs[to_explore[0]]+1
                to_explore.append(path)
        to_explore.pop(0)
    return costs


def release(seq:str, time_available: int):
    global vmap
    released = 0
    for i in range(1, len(seq)):
        if time_available - vmap[seq[i - 1]]['paths'][seq[i]] <= 0: break
        released += (time_available - vmap[seq[i - 1]]['paths'][seq[i]]) * vmap[seq[i]]['release']
        time_available -= vmap[seq[i - 1]]['paths'][seq[i]]
    return released if i == len(seq)-1 else None


def dfs(sequence, time_remaining):
    global vmap, cache
    if time_remaining <= 0: return
    for key in vmap:
        if key in sequence: continue  # dependent on unique names
        if cache.get(sequence) is None:
            r = release(sequence+key, time_remaining)
            if r is not None:
                cache[sequence+key] = r
        else:
            r = release(sequence[-1]+key, time_remaining)
            if r is not None:
                cache[sequence+key] = cache[sequence] + r
        dfs(sequence+key, time_remaining-vmap[sequence[-1]]['paths'][key])


# preprocess valves into useful array
valves = dict()
useful_valves = ['AA']
for row in data:
    paths = [path.strip(',') for path in row.split(' ')[9:]]
    valves[row.split(' ')[1]] = {'release': int(row.split(' ')[4].split('=')[1].strip(';')), "paths":paths }
    if row.split(' ')[4] != 'rate=0;':
        useful_valves.append(row.split(' ')[1])

# construct a submap of cost to useful valves from every other useful valve indicated by single char
vmap = dict()
for v in useful_valves:
    cost_map = djikstra(valves, v)
    paths = {chr(65+useful_valves.index(valve)): cost_map[valve]+1 for valve in useful_valves}
    vmap[chr(65+useful_valves.index(v))] = {'release': valves[v]['release'], 'paths': paths}

if stage == 'a':
    dfs('A', 30)
    sorted_cache = sorted(list(cache.items()), key=lambda key: key[1])
    sorted_cache.reverse()
    result = sorted_cache[0][1]

else:
    dfs('A', 26)
    sorted_cache = sorted(list(cache.items()), key=lambda key: key[1])
    sorted_cache.reverse()
    result = 0
    for a in sorted_cache:
        for b in sorted_cache:
            if set(a[0][1:]).isdisjoint(set(b[0][1:])):
                if a[1]+b[1] - result <= 0: break
                result = max(result, a[1]+b[1])
        if a[1] < 900 or len(a[0]) <= len(useful_valves) / 2: break

print(f"Time: {time.time() - start}")
print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
