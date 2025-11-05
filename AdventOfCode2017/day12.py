# Advent of Code 2017 Day 12
# Author:   Rachael Judy
# Purpose:  connected components size and count

import networkx as nx

import parseMod

ready = False
day = 12
stage = 'a'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv")

graph = nx.Graph(((a, b.strip(',')) for a, _, *rest in data for b in rest))
result = len(nx.node_connected_component(graph, '0')) if stage == 'a' else nx.number_connected_components(graph)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
