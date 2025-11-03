# Advent of Code 2017 Day 6
# Author:   Rachael Judy
# Purpose:  find memory reallocation loop

import parseMod

ready = True
day = 6
stage = 'a'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSVInts("data/" + str(day).zfill(2) + "data.csv", delim='\t')


def redistribute(data):
    banks = data[:]
    maxi, maxm = max(enumerate(banks), key=lambda x: x[1])
    banks[maxi] = 0
    for j in range(1, len(banks) + 1):
        idx = (maxi + j) % len(banks)
        banks[idx] += (maxm//len(banks)) + (1 if j <= maxm%len(banks) else 0)
    return banks

# brent's optimized tortoise/hare
power = lam = 1
tortoise, hare = data, redistribute(data)
while tortoise != hare:
    if power == lam:
        tortoise, power, lam = hare, power * 2, 0
    hare = redistribute(hare)
    lam += 1

mu = 0
tortoise = hare = data
for _ in range(lam):
    hare = redistribute(hare)
while tortoise != hare:
    tortoise, hare, mu = redistribute(tortoise), redistribute(hare), mu + 1

result = lam + mu if stage=='a' else lam

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
