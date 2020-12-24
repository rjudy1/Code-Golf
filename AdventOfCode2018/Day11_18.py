# Advent of Code 2018 - Day 11

# Author:   Rachael Judy
# Date:     12/24/2020
# Purpose:  based on power changing based on coordinate and serial number, find the max power grid with changing grid x
#           part 2 is kind of slow force

import math

serial_num = 1308  # set this
grid = [[0 for i in range(300)] for j in range(300)]  # 300 by 300 grid (coordinates all have to be incremented by one)
for y in range(1, len(grid) + 1):  # get each spot's power
    for x in range(1, len(grid[0]) + 1):
        grid[y - 1][x - 1] = math.floor((((x+10) * y + serial_num) * (x+10) % 1000) / 100) - 5


def get_max(min_size, max_size):
    max_power = (0, 0, 0, 0)
    for size in range(min_size, max_size+1):
        for y in range(0, len(grid)-size+1):
            for x in range(0, len(grid[0])-size+1):
                power = sum(grid[j][i] for i in [xi for xi in range(x, x+size)] for j in [yi for yi in range(y, y+size)])
                if power > max_power[3]:
                    max_power = (x+1, y+1, size, power)
    return max_power


print("part 1", get_max(3, 3))
print("part 2", get_max(5, 30))  # might have to adjust this window
