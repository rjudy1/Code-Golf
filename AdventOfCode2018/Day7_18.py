# Advent of Code 2020 - Day 23

# Author:   Rachael Judy
# Date:     12/23/2020
# Purpose:  Find order of tasks with prerequisites to be done singly or with help

import os
import sys
import networkx as nx

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


class Elf:
    def __init__(self):
        self.available = 0  # time can do a new task
        self.working_on = ''  # time


def work(phase, relationships):
    # line[1] is the predecessor of line[7] - add edges to graph of predecessor to successor
    G = nx.DiGraph()
    for line in relationships:
        G.add_edge(line.split()[1], line.split()[7])

    order = ''
    num_workers = pow(5, phase-1)
    workers = [Elf() for i in range(num_workers)]
    in_progress = []

    for t in range(2000):  # 2000 time steps should cover the time needed
        # collect the finished work before polling for new - necessary to avoid lag of a step
        for w in workers:
            if w.available <= t:
                order += w.working_on
                w.working_on = ''
                in_progress.remove(w.working_on) if w.working_on in in_progress else 0
                G.remove_node(w.working_on) if w.working_on in G.nodes else 0

        # check if more work is available
        for w in workers:
            if w.available <= t:
                for x in sorted(G.nodes):  # remaining nodes
                    ready = True
                    for c in list(G.predecessors(x)):
                        if c not in order:
                            ready = False
                            break

                    if ready and x not in in_progress:  # worker found work
                        w.available = t + 61 + ord(x) - ord('A')  # t to be available again
                        w.working_on = x  # task to work on
                        in_progress.append(w.working_on)
                        break

        if len(order) == 26:  # have full string
            break

    print(f"part {phase}")
    print("order:   ", order)
    print("time:    ", t)
    print()


# input
lines = parseMod.readCSV_row('data/7steps.csv', '\n')
work(1, lines)  # execute phase 1
work(2, lines)  # execute phase 2
