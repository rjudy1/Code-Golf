# Advent of Code 2018 - Day 9

# Author:   Rachael Judy
# Date:     12/23/2020
# Purpose:  Play game with rotating circle of marbles, place every other except on multiples of 23, then get points

from collections import deque


def play_game(max_players, last_marble):
    scores = [0 for i in range(max_players)]
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores) if scores else 0


inp = '416 players; last marble is worth 71617 points'
num_plyrs, max_pts = int(inp.split()[0]), int(inp.split()[6])

print("part 1: ", play_game(num_plyrs, max_pts))
print("part 2: ", play_game(num_plyrs, max_pts*100))