# Advent of Code 2016 Day 17
# Author:   Rachael Judy
# Purpose:  navigate dynamic maze based on md5 hash of instruction sequence

from collections import deque
import hashlib

import parseMod

ready = True
day = 17
stage = 'b'
year = 2016

parseMod.createDataFile(year=year, day=day)
code = parseMod.readCSV_row('data/' + str(day).zfill(2) + 'data.csv')[0]

q, vis, rseq = deque([(0, '')]), {(0, '')}, ''
while q:
    p, seq = q.popleft()
    if p == 3+3j:
        rseq = max(seq, rseq, key=len)
        if stage == 'a':
            break
        continue

    for door, (dir, dx) in enumerate([('U', -1), ('D', 1), ('L', -1j), ('R', 1j)]):
        if (n:=(p+dx, seq+dir)) not in vis and 0 <= n[0].real < 4 and 0 <= n[0].imag < 4 \
                and hashlib.md5((code+seq).encode()).hexdigest()[door] in {'b','c','d','e','f'}:
            q.append(n)
            vis.add(n)

result = rseq if stage == 'a' else len(rseq)
print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
