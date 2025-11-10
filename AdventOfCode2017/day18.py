# Advent of Code 2017 Day 18
# Author:   Rachael Judy
# Purpose:  mini assembly coroutines

from collections import defaultdict

import parseMod

ready = True
day = 18
stage = 'a'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv", ' ')


def run_program(pid=0):
    global data, q, counts, stage  # shared across all programs
    pc, r = 0, defaultdict(int, p=pid)  # program counter, registers
    v = lambda x: int(x) if x.lstrip('-').isdigit() else r[x]  # get value
    def snd(a):
        r['lp'] = v(a)
        q[1 - pid].append(v(a))
        counts[pid] += 1
    def set_(a, b): r[a] = v(b)
    def add(a, b):  r[a] += v(b)
    def mul(a, b):  r[a] *= v(b)
    def mod(a, b):  r[a] %= v(b)
    def rcv(a):
        if stage == 'a':
            if v(a) != 0:
                yield r['lp']
        else:
            while not q[pid]: yield
            r[a] = q[pid].pop(0)
    def jgz(a, b):
        nonlocal pc
        if v(a) > 0:
            pc += v(b) - 1

    ops = {'snd': snd, 'set': set_, 'add': add, 'mul': mul, 'mod': mod, 'rcv': rcv, 'jgz': jgz}

    while 0 <= pc < len(data):
        ins, *args = data[pc]
        res = ops[ins](*args)
        if res is not None:
            yield from res
        pc += 1


q, counts = [list(), list()], [0, 0]
p0, p1 = run_program(0), run_program(1)
if stage == 'a':
    result = next(p0)
else:
    while True:
        next(p0, None)
        next(p1, None)
        if not q[0] and not q[1]:  # queues are empty and programs deadlocked
            result = counts[1]
            break

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
