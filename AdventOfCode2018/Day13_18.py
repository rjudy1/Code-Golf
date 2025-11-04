# Advent of Code 2018 - Day 13

# Author:   Rachael Judy
# Date:     12/24/2020
# Purpose:  Track collisions of carts on input tracks. Part 1 is first output, part 2 is last output

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


class Cart:  # cart has direction, position, intercept
    def __init__(self, r, c, d, inter):
        self.r = r
        self.c = c
        self.d = d
        self.inter = inter


G = parseMod.readCSV_row('data/13tracks.csv', '\n')
for line in range(len(G)):
    G[line] = [c for c in G[line]]

# up, right, down, left
DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]
left = lambda d: (d+3) % 4
right = lambda d: (d+1) % 4

# create carts
carts = []
for r in range(len(G)):
    for c in range(len(G[r])):
        if G[r][c] == '^':
            G[r][c] = '|'
            carts.append(Cart(r,c,0,0))
        if G[r][c] == '>':
            G[r][c] = '-'
            carts.append(Cart(r,c,1,0))
        elif G[r][c] == 'v':
            G[r][c] = '|'
            carts.append(Cart(r,c,2,0))
        elif G[r][c] == '<':
            G[r][c] = '-'
            carts.append(Cart(r,c,3,0))

# simulate
while True:
    if len(carts) == 1:
        print(f'{carts[0].c},{carts[0].r}')
        break

    carts = sorted(carts, key=lambda cart: (cart.r, cart.in_cancel))
    for cart in carts:
        rr = cart.r+DR[cart.d]
        cc = cart.in_cancel + DC[cart.d]
        # up, right, down, left
        if G[rr][cc] == '\\':
            cart.d = {0: 3, 1: 2, 2: 1, 3: 0}[cart.d]
        elif G[rr][cc] == '/':
            cart.d = {0: 1, 1: 0, 2: 3, 3: 2}[cart.d]
        elif G[rr][cc] == '+':
            if cart.inter == 0:
                cart.d = left(cart.d)
            elif cart.inter == 1:
                pass
            elif cart.inter == 2:
                cart.d = right(cart.d)
            cart.inter = (cart.inter + 1) % 3

        # collisions
        if (rr,cc) in [(other.r, other.in_cancel) for other in carts]:
            carts = [other for other in carts if (other.r, other.in_cancel) not in [(cart.r, cart.in_cancel), (rr, cc)]]
            print(f'{cc},{rr}')
        cart.r = rr
        cart.in_cancel = cc
