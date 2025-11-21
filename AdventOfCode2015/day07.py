# Advent of Code 2015 Day 7
# Author:   Rachael Judy
# Purpose:  trace through circuit

from collections import namedtuple, defaultdict

import parseMod

ready = False
day = 7
stage = 'a'
year = 2015

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl('data/' + str(day).zfill(2) + 'data.csv', ' ')

Instr = namedtuple("Instr", "op ops")
commands = {}
for *expr, _, target in data:
    if len(expr) == 1:
        op, ops = "SET", [expr[0]]
    elif len(expr) == 2:        # NOT x
        op, ops = expr[0], [expr[1]]
    else:                       # any two operand
        op, ops = expr[1], [expr[0], expr[2]]
    commands[target] = Instr(op, ops)

OPS = {"SET": lambda a, b=None: a, "NOT":    lambda a, b=None: 65535 ^ a,
       "AND":    lambda a, b: a & b, "OR":     lambda a, b: a | b,
       "LSHIFT": lambda a, b: a << b, "RSHIFT": lambda a, b: a >> b}
cache = {}

def eval_wire(w):
    if w.isdigit():
        return int(w)
    if w in cache:
        return cache[w]
    ops = [eval_wire(x) for x in commands[w].ops]
    cache[w] = OPS[commands[w].op](*ops)
    return cache[w]

result = eval_wire('a')
if stage == 'b':
    cache = {}
    commands['b'] = Instr('SET', [str(result)])
    result = eval_wire('a')

if not ready:
    print(f'result: \n{result}')
elif ready:
    print('SUBMITTING RESULT: ', result)
    parseMod.submit(result, part=stage, day=day, year=year)
