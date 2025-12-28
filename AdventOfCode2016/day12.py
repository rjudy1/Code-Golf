# Advent of Code 2016 Day 12
# Author:   Rachael Judy
# Purpose:  basic assembly

import parseMod

ready = False
day = 12
stage = 'a'
year = 2016

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl('data/' + str(day).zfill(2) + 'data.csv', ' ')

pc, reg = 0, {'a': 0, 'b': 0, 'c': stage=='b', 'd': 0}
get_val = lambda x: reg[x] if x.isalpha() else int(x)
while 0 <= pc < len(data):
    match data[pc][0]:
        case 'cpy': reg[data[pc][2]] = get_val(data[pc][1])
        case 'inc': reg[data[pc][1]] += 1
        case 'dec': reg[data[pc][1]] -= 1
        case 'jnz': pc += (get_val(data[pc][2])-1) * (get_val(data[pc][1])!=0)
    pc += 1
result = reg['a']

# equivalent to the assembly
# a, b = 1, 1
# for i in range(33 if stage == 'b' else 26):  # dth fibonacci
#     a, b = b + a, a
# result = a + int(data[16][1]) * int(data[17][1])

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
