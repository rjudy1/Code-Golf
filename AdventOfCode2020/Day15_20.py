# Advent of Code 2020 - Day 15

# Author:   Rachael Judy
# Date:     12/15/2020
# Purpose:  Play elves' memory game - if number has appeared before, say difference between turns, if not, say 0

turn_to_end = 30_000_000  # 2020  # for phase 1 (2020) and 2 (30 mil) - part 2 takes around 20 seconds

# use usage dict that stores last turn and seed which holds value last spoken
# input is:
# 13,16,0,12,15,1
usage_dict = {13:0, 16:1, 0:2, 12:3, 15:4}
seed = 1

# execute game
for i in range(len(usage_dict)+1, turn_to_end):
    if seed in usage_dict.keys():  # if already spoken, subtract turns spoken for next seed
        temp = usage_dict[seed]
        usage_dict[seed] = i - 1
        seed = i - temp - 1
    else:  # if not spoken, 0
        usage_dict[seed] = i - 1
        seed = 0

print(f"Number at turn {turn_to_end}: {seed}")