# Advent of Code 2025 Day 10
# Author:   Rachael Judy
# Purpose:  solve for x such that Vx = target or joltage with operation either toggle or increment

from collections import deque
import numpy as np
from pulp import LpProblem, LpMinimize, LpVariable, LpInteger, lpSum, PULP_CBC_CMD, LpStatus

import aocd
from mycookie import cookie

ready = True
day = 10
stage = 'b'

data = [[el.strip('(){}[]') for el in ln.split(' ')] for ln in aocd.get_data(cookie, day, 2025).split('\n')]
result = 0
for tstr, *btstrs, jstr in data:
    if stage == 'a':
        target = sum(1 << len(tstr) - i - 1 for i in range(len(tstr)) if tstr[i] == '#')
        buttons = [sum(1 << (len(tstr) - 1 - int(num)) for num in b.split(',')) for b in btstrs]

        q, vis = deque([(0, 0)]), {0}
        while q:
            lights, step = q.popleft()
            if lights == target:
                result += step
                break
            for b in buttons:
                if lights ^ b not in vis:
                    q.append((lights ^ b, step+1))
                    vis.add(lights ^ b)
    else:
        joltage = tuple(int(jt) for jt in jstr.split(','))
        buttons = [[((1 << (len(joltage) - 1 - i)) & sum(1 << (len(joltage) - 1 - int(n)) for n in b.split(','))) != 0 for i in range(len(joltage))] for b in btstrs]

        V, t = np.array(buttons).T, np.array(joltage)  # V x = t
        N, M = V.shape
        prob = LpProblem("MinButtonSum", LpMinimize)
        x_vars = [LpVariable(f"x{i}", lowBound=0, cat=LpInteger) for i in range(M)]
        prob += lpSum(x_vars)
        for i in range(N):
            prob += lpSum(V[i, j] * x_vars[j] for j in range(M)) == t[i]
        status = prob.solve(PULP_CBC_CMD(msg=False))
        result += sum(int(x_vars[i].varValue) for i in range(M))

print(f'stage {stage} result (ready={ready}): \n{result}')
if ready:
    aocd.submit(result, part=stage, day=day, year=2025, session=cookie)
