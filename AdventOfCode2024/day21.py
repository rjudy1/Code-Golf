# Advent of Code 2024 Day 21
# Author:   Rachael Judy
# Purpose:  recursively find series of buttons to push a series of keypads' buttons to enter code

import collections
import csv
from functools import cache
import parseMod

ready = True
day = 21
stage = 'b'  # 248108, 303836969158972
year = 2024

parseMod.createDataFile(year=year, day=day)

# mappings for two keypads
pos_to_numeric = {0: '7', 1j: '8', 2j: '9', 1: '4', 1+1j: '5', 1+2j: '6', 2: '1', 2+1j: '2', 2+2j: '3', 3+1j: '0', 3+2j: 'A'}
pos_to_directional = {1j: '^', 2j: 'A', 1: '<', 1+1j: 'v', 1+2j: '>'}


def dfs(path, mapping, shortest_paths):  # dfs populating the shortest paths dictionary
    dirs = {1j: '>', -1j: '<', 1: 'v', -1: '^'}
    dist_to_a = {'>': 1, '^': 1, 'v': 2, '<': 3, 'A': 0}  # used as tie breaker for paths
    if 2 < len(path) <= len(shortest_paths[mapping[path[0]], mapping[path[-1]]])+1:  # rate the path
        dir_changes = sum(1 for i in range(len(path)-2) if path[i+2]-path[i+1] != path[i+1]-path[i])
        current_path = shortest_paths[mapping[path[0]], mapping[path[-1]]][:-1]
        current_path_score = sum(1 for i in range(len(current_path)-1) if current_path[i+1] != current_path[i])
        if dir_changes < current_path_score or dir_changes == current_path_score and dist_to_a[dirs[path[-1] - path[-2]]] <= dist_to_a[current_path[-1]]:
            shortest_paths[mapping[path[0]], mapping[path[-1]]] = f"{''.join([dirs[path[i + 1] - path[i]] for i in range(len(path) - 1)])}A"

    for dx in dirs:
        if path[-1]+dx in mapping and path[-1]+dx not in path:
            shortest_paths[mapping[path[-1]], mapping[path[-1]+dx]] = f'{dirs[dx]}A'
            path.append(path[-1]+dx)
            dfs(path, mapping, shortest_paths)
            path.pop()


@cache
def get_len(seq, depth) -> int:  # get length of key presses to trigger sequence of directional buttons
    return len(seq) if depth == 0 else sum(get_len(directional_paths[(f'A{seq}'[i], f'A{seq}'[i + 1])], depth - 1) for i in range(len(seq)))


# generate least cost paths for every pair - could reduce redundant paths probably
numeric_paths = collections.defaultdict(lambda: '>^<>^<^>')
for source in pos_to_numeric:
    numeric_paths[pos_to_numeric[source], pos_to_numeric[source]] = 'A'
    dfs([source], pos_to_numeric, numeric_paths)
directional_paths = collections.defaultdict(lambda: '>^<>^<^>')
for source in pos_to_directional:
    directional_paths[pos_to_directional[source], pos_to_directional[source]] = 'A'
    dfs([source], pos_to_directional, directional_paths)

with open("data/" + str(day).zfill(2) + "data.csv") as file:
    result = sum(get_len(''.join([numeric_paths[f'A{code}'[i], f'A{code}'[i + 1]] for i in range(len(code))]), 2 if stage == 'a' else 25) * int(code[:-1]) for code in [row[1][0] for row in enumerate(csv.reader(file))])

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
