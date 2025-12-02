# Advent of Code 2025 Day 2
# Author:   Rachael Judy
# Purpose:  sum invalid ids that are composed of repeating sequences of digits

import aocd
from mycookie import cookie

ready = True
day = 2
stage = 'b'

data = aocd.get_data(cookie, day, 2025).split(',')
result = sum(i for r in data for lo, up in [map(int, r.split('-'))] for i in range(lo, up + 1)
             if stage=='a' and len(s:=str(i))%2==0 and s[:len(s)//2]==s[len(s)//2:] or stage=='b' and (s:=str(i)) in (s+s)[1:-1])

print(f'stage {stage} result (ready={ready}): \n{result}')
if ready:
    aocd.submit(result, part=stage, day=day, year=2025, session=cookie)
