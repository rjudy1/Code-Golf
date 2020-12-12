# Advent of Code 2019 Day 8

# Author:   Rachael Judy
# Date:     12/3/2020
# Purpose:  Image pixel layers - requires some squinting


import numpy as np

import parseMod


# occupied_count occurrences of zeros, ones, twos
def countTypes(numbers):
    zeros = 0
    ones = 0
    twos = 0
    for n in numbers:
        if n == '0':
            zeros += 1
        elif n == '1':
            ones += 1
        elif n == '2':
            twos += 1

    return zeros, ones, twos


# display the image based on 1 being white and 0 being black (message white on black)
# squint at the letters in awe
def printImage(image):
    for x in range(6):
        for y in range(25):
            if image[x, y] == '1':
                print('}{', end='')
            else:
                print('  ', end='')
        print()


# read each char as own item
pixels = parseMod.readCSV_single('data/8pixels.csv')
phase = 2
height = 6
width = 25
layers = [pixels[150 * i:150 * (i + 1)] for i in range(int(len(pixels) / 150))]

#  phase one product of number of ones and twos in minimum number of zeros layer
if phase == 1:
    minNum = 1000
    prod = 0
    for layer in layers:
        counts = countTypes(layer)
        if counts[0] < minNum:
            minNum = counts[0]
            prod = int(counts[1]) * int(counts[2])
    print("Product in Layer with Min Zeroes: ", prod)

# interpose with lowest numbered layer being top, 2'shuffle being transparent
elif phase == 2:
    msg = ['2' for i in range(width*height)]
    for layer in layers:
        for i in range(len(layer)):
            if layer[i] != '2' and msg[i] == '2':
                msg[i] = layer[i]

    # reshape list to two dimensional array and display
    photo = np.array(msg)
    photo = np.reshape(photo, (6, 25))
    printImage(photo)
