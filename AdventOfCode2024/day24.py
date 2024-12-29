# Advent of Code 2024 Day 24
# Author:   Rachael Judy
# Purpose:  simulate wires, correct errors in the ripple carry adder (alphabetize what, graphviz for initial solve)

import collections
import csv
import graphviz
import parseMod

ready = True
day = 24
stage = 'b'  # 55920211035878, (btb,cmv,mwp,rdg,rmj,z17,z23,z30)  # pairs are (cmv,z17), (rmj,z23), (rdg,z30), (mwp,btb)
year = 2024

parseMod.createDataFile(year=year, day=day)
gates, gate_list, graph = dict(), list(), graphviz.Digraph()
top_z = 0
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    to_populate = collections.deque([])
    for i, row in enumerate(csv.reader(file)):
        if row:
            if ':' in row[0]:  # input
                gates[row[0][:3]] = int(row[0][-1])
            elif '->' in row[0]:  # gate
                x0, op, x1, _, out = row[0].split()
                to_populate.append((x0, op, x1, out))
                gate_list.append((x0, op, x1, out))
                if out[0] == 'z':  # keep index of highest bit in result
                    top_z = max(top_z, int(out[1:]))
                graph.edge(x0, out, label=op)
                graph.edge(x1, out, label=op)

graph.render('temp/adder-graph.gv', view=True)  # render graph - review to find adder errors at lsb wrong iteratively

# solve a by populating the z edges as provided
while to_populate:
    x0, op, x1, out = to_populate.popleft()
    if x0 in gates and x1 in gates:  # ready to assess this value
        gates[out] = gates[x0] & gates[x1] if op == 'AND' else gates[x0] | gates[x1] if op == 'OR' else gates[x0] ^ gates[x1]
    else:  # postpone until inputs resolve
        to_populate.append((x0, op, x1, out))

# swapped gates in adder (invalid inputs/outputs/feedforwards; only broken within adder, otherwise loops would occur)
wrong_gates = set()
for x0, op, x1, out in gate_list:
    if (out[0] == 'z' and op != "XOR" and out != f'z{top_z:02d}'
            or op == 'XOR' and not ((x0[0] in ['x', 'y'] and x1[0] in ['x', 'y']) or out[0] == 'z')):
        wrong_gates.add(out)
    for sub0, subgate, sub1, out0 in gate_list:  # could hash by input but it's not that slow
        if (op == 'AND' and 'x00' not in [x0, x1] and (sub0 == out or sub1 == out) and subgate != 'OR' or
                op == 'XOR' and (sub0 == out or sub1 == out) and subgate == 'OR'):
            wrong_gates.add(out)
result = sum(2**i * gates[f'z{i:02d}'] for i in range(top_z, -1, -1)) if stage == 'a' else ','.join(sorted(wrong_gates))

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
