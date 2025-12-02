# Advent of Code 2015 Day 22
# Author:   Rachael Judy
# Purpose:  wizard battle min win with different spells (dijkstra)

from collections import defaultdict, namedtuple
import heapq
import math

import parseMod

ready = False
day = 22
stage = 'a'
year = 2015

parseMod.createDataFile(year=year, day=day)
bh, bd = (int(x[-1]) for x in parseMod.readCSV_rowEl(f'data/{day:02d}data.csv', ' '))

# cost, damage, heal, shield enable timer, poison enable, recharge enable
Spell = namedtuple("Spell", ["c", "d", "h", "se", "pe", "re"])
SPELLS = [Spell(53, 4, 0, 0, 0, 0), Spell(73, 2, 2, 0, 0, 0), Spell(113, 0, 0, 6, 0, 0), Spell(173, 0, 0, 0, 6, 0), Spell(229, 0, 0, 0, 0, 5)]

# state = (mana spent, php, bhp, mana, shield timer, poison timer, recharge timer, boss turn
heap, vis = [state := (0, 50, bh, 500, 0, 0, 0, 0)], defaultdict(lambda: math.inf, {state[1:]: state[0]})
while heap:
    result, php, bhp, mana, st, pt, rt, bt = cn = heapq.heappop(heap)

    php -= 1 * (stage == 'b' and not bt)
    mana += 101 * (rt != 0)
    bhp -= 3 * (pt != 0)

    if bhp <= 0:  # cost to get to node is min
        break
    if php <= 0:
        continue

    if not bt:
        for sp in SPELLS:
            if (not (mana < sp.c or sp.re and rt > 1 or sp.pe and pt > 1 or sp.se and st > 1) and
                    vis[n := (php+sp.h, bhp-sp.d, mana-sp.c, max(sp.se, st-1, 0), max(sp.pe, pt-1, 0), max(sp.re, rt-1, 0), 1)] > vis[cn[1:]] + sp.c):
                vis[n] = vis[cn[1:]] + sp.c
                heapq.heappush(heap, (vis[n], *n))
    else:  # boss turn
        vis[n := (php - max(1, bd - 7*(st!=0)), bhp, mana, max(st-1, 0), max(pt-1, 0), max(rt-1, 0), 0)] = result
        heapq.heappush(heap, (result, *n))

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
