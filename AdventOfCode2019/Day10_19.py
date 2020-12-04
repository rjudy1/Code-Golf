# Advent of Code 2019 - Day 10

# Author:   Rachael Judy
# Date:
# Purpose:  Find best asteroid to put base on that can see most others - go based on slope


import parseMod

astMap = parseMod.readCSV_row('10asteroids.csv')
# matrix is [row][column] (y,x)
# use slope somehow