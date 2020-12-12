# Advent of Code 2019 - Day 22

# Author:   Rachael Judy
# Date:     12/12/2020
# Purpose:  Implement shuffles on massive deck

import os
import sys

import copy

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

dealing = parseMod.readCSV_rowEl('data/22dealer.csv')

# part 1 - kind of brute force
# create deck
deck = [i for i in range(10007)]
for instruction in dealing:
    if instruction[-2] == 'increment':
        new_deck = [0 for i in range(len(deck))]
        index = 0
        for card in deck:
            new_deck[index % len(deck)] = card
            index += int(instruction[-1])
        deck = copy.deepcopy(new_deck)
    elif instruction[-2] == 'cut':
        deck = deck[int(instruction[-1]):len(deck)] + deck[0:int(instruction[-1])]
    elif instruction[-2] == 'new':
        deck.reverse()

print("Part 1: ", deck.index(2019))


# part 2
m = 119315717514047  # deck size, modulo
iterations = 101741582076661
pos = 2020
shuffles = { 'increment': lambda x,m,a,b: (a*x % m, b*x % m),  # increment affects both the same
         'new': lambda _,m,a,b: (-a % m, (m-1-b) % m),  # new deal mirrors
         'cut': lambda x,m,a,b: (a, (b-x) % m) }  # cut maintains a, moves b

a, b = 1,0
for shuffle in dealing:  # perform the linearity on each instruction
    for name, fn in shuffles.items():  # find match
        if shuffle[-2] == name:
            arg = int(shuffle[-1]) if name != 'new' else 0
            a, b = fn(arg, m, a, b)
            break

r = (b * pow(1-a, m-2, m)) % m  # manipulation on fermat's little theorem
print(f"Part 2: card at #{pos}: {((pos - r) * pow(a, iterations * (m - 2), m) + r) % m}")  # manipulation of exp
