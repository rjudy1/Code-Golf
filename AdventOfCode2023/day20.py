# Advent of Code 2023 Day 20
# Author:   Rachael Judy
# Date:     12/20/23
# Purpose:  conjunctions and flip flops to settle for 1000 button presses, then until rx gets 1 (boring cycles again)

from collections import deque
from copy import deepcopy
from itertools import count
from math import lcm
import parseMod

ready = True
day = 20
stage = 'b'
year = 2023

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")


def propagate_pulse(graph, flops, conjs, sender, receiver, pulse):
    if receiver in flops:
        if pulse:
            return  # low active only
        next_pulse = flops[receiver] = not flops[receiver]
    elif receiver in conjs:
        conjs[receiver][sender] = pulse
        next_pulse = not all(conjs[receiver].values())
    elif receiver in graph:
        next_pulse = pulse
    else:
        return

    for new_receiver in graph[receiver]:
        yield receiver, new_receiver, next_pulse


def run(graph, flops, conjs):
    q = deque([('button', 'broadcaster', False)])
    nlo = nhi = 0
    while q:  # full iteration until unchanging
        sender, receiver, pulse = q.popleft()
        nhi += pulse
        nlo += not pulse
        q.extend(propagate_pulse(graph, flops, conjs, sender, receiver, pulse))
    return nlo, nhi


def find_cycles(graph, flops, conjs, rx_source):
    useful = set()
    for source, dests in graph.items():
        if rx_source in dests:
            useful.add(source)

    for iteration in count(1):
        q = deque([('button', 'broadcaster', False)])
        while q:
            sender, receiver, pulse = q.popleft()
            if not pulse:
                if receiver in useful:
                    yield iteration
                    useful.discard(receiver)
                    if not useful:
                        return
            q.extend(propagate_pulse(graph, flops, conjs, sender, receiver, pulse))


flops, conjs, graph = {}, {}, {}
for line in data:
    source, dests = line.split('->')
    source = source.strip()
    dests = list(map(str.strip, dests.split(',')))
    if 'rx' in dests:
        rx_source = source[1:]

    if source[0] == '%':
        flops[source[1:]] = False
    elif source[0] == '&':
        conjs[source[1:]] = {}
    else:
        source = '.'+source
    graph[source[1:]] = dests

for source, dests in graph.items():
    for dest in filter(conjs.__contains__, dests):
        conjs[dest][source] = False

orig_flops = deepcopy(flops)
orig_conjs = deepcopy(conjs)

tothi = totlo = 0
for _ in range(1000):
    nhi, nlo = run(graph, flops, conjs)
    tothi += nhi
    totlo += nlo

if stage=='a':
    result = totlo * tothi
else:
    result = lcm(*find_cycles(graph, orig_flops, orig_conjs, rx_source))

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
