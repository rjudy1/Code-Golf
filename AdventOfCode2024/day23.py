# Advent of Code 2024 Day 23
# Author:   Rachael Judy
# Purpose:  3-clique containing historian, then maximal clique (np-hard, why not)

import collections
import csv
import itertools
import parseMod

ready = True
day = 23
stage = 'b'  # 1075, az,cg,ei,hz,jc,km,kt,mv,sv,sx,wc,wq,xy
year = 2024

parseMod.createDataFile(year=year, day=day)
adjacency_lists = collections.defaultdict(set)
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    for i, row in enumerate(csv.reader(file)):
        a,b = row[0].split('-')
        adjacency_lists[a].add(b)
        adjacency_lists[b].add(a)

if stage == 'a':  # naive, could at least pull historian but eh
    result = len({tuple(sorted([n0,n1,n2])) for n0,n1,n2 in itertools.combinations(adjacency_lists, 3)
                  if (n1[0]=='t' or n2[0]=='t' or n0[0]=='t') and
                  n1 in adjacency_lists[n2] and n2 in adjacency_lists[n0] and n0 in adjacency_lists[n1]})
else:
    def bron_kerbosch(curr_clique, potential, excluded, graph):  # bron kerbosch algorithm for all cliques possible
        if not potential and not excluded:
            yield curr_clique  # current clique is best possible from offered potential
        while potential:
            v = potential.pop()
            yield from bron_kerbosch(
                curr_clique.union({v}), potential.intersection(graph[v]), excluded.intersection(graph[v]), graph)
            excluded.add(v)

    all_cliques = list(bron_kerbosch(set(), set(adjacency_lists.keys()), set(), adjacency_lists))
    max_size = 0
    for clique in all_cliques:
        if len(clique) > max_size:
            result = ','.join(sorted(clique))
            max_size = len(clique)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
