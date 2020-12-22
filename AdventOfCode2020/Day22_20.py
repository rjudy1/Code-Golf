# Advent of Code 2020 - Day 22

# Author:   Rachael Judy
# Date:     12/22/2020
# Purpose:  Play card game like war (part 1) and recursive version that involves subgame with smaller deck (part 2)

import copy
import os
import sys
import queue

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

hands = parseMod.readCSV_row('data/22decks.csv', '\n')


# basic War
def part_1(player_queues):
    while not player_queues[0].empty() and not player_queues[1].empty():
        play = [player_queues[0].get(), player_queues[1].get()]
        winner = play[1] > play[0]
        player_queues[winner].put(play[winner])
        player_queues[winner].put(play[1-winner])

    return winner


# recursive War
def part_2(player_lists):
    memory = set()
    while len(player_lists[0]) and len(player_lists[1]):
        # recursion exit, first player wins
        if tuple([tuple(player_lists[0]), tuple(player_lists[1])]) in memory:
            return 0
        else:
            memory.add(tuple([tuple(player_lists[0]), tuple(player_lists[1])]))

        play = [player_lists[0].pop(0), player_lists[1].pop(0)]
        # check if can recurse
        if play[0] <= len(player_lists[0]) and play[1] <= len(player_lists[1]):
            list0_copy = copy.deepcopy(player_lists[0][:play[0]])
            list1_copy = copy.deepcopy(player_lists[1][:play[1]])
            winner = part_2([list0_copy, list1_copy])
        else:  # else winner is determined by old version
            winner = play[1] > play[0]

        player_lists[winner].append(play[winner])
        player_lists[winner].append(play[1-winner])

    return winner


# get input - queues for part one, lists for splicing part 2
player_queues = [queue.SimpleQueue(), queue.SimpleQueue()]
player_lists = [[], []]
for i in hands[1:int(len(hands)/2)]:
    player_queues[0].put(int(i))
    player_lists[0].append(int(i))
for j in hands[int(len(hands)/2+1):]:
    player_queues[1].put(int(j))
    player_lists[1].append(int(j))

score = 0
winner = part_1(player_queues)
for i in range(50, 0, -1):
    score += i * player_queues[winner].get()
print("part 1: ", score)

score = 0
winner = part_2(player_lists)
for i in range(len(player_lists[winner]), 0, -1):
    score += i * player_lists[winner][len(player_lists[winner])-i]
print("part 2: ", score)
