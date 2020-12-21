# Advent of Code 2020 - Day 20

# Author:   Rachael Judy
# Date:     12/20/2020
# Purpose:  Take the rotated/reflected images put in and match the borders to form a seamless image
#           then identify sea monsters

import copy
import os
import sys
import math

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


# each tile input will have pattern, id number, and other useful attributes
class Tile:
    def __init__(self, pattern, id_num):
        self.tile_pattern = pattern
        self.id_num = id_num

        # initialize edges
        self.top = pattern[0]
        self.bottom = pattern[-1]
        self.left = []
        self.right = []
        self.set_edges(pattern)

        self.top_join = 0
        self.bottom_join = 0
        self.right_join = 0
        self.left_join = 0

    def set_edges(self, pattern):
        self.top = pattern[0]
        self.bottom = pattern[-1]
        self.left = []
        self.right = []
        for i in range(len(pattern)):
            self.left.append(pattern[i][0])
            self.right.append(pattern[i][-1])

    # horizontal flip - switches top and bottom order and left and right sides
    def flip_h(self):
        for row in self.tile_pattern:
            row.reverse()
        self.set_edges(self.tile_pattern)
        self.right_join, self.left_join = self.left_join, self.right_join

    # vertical flip does opposite of horizontal
    def flip_v(self):
        self.tile_pattern.reverse()
        self.set_edges(self.tile_pattern)
        self.top_join, self.bottom_join = self.bottom_join, self.top_join

    # rotate at whatever the requested angle is
    def rotate(self, angle):
        # rotates the angle given
        for _ in range(int(angle/90)):
            self.tile_pattern = list(zip(*self.tile_pattern[::-1]))
            for r in range(len(self.tile_pattern)):  # fix a tuple thing
                self.tile_pattern[r] = list(self.tile_pattern[r])

            self.set_edges(self.tile_pattern)
            self.top_join, self.right_join, self.bottom_join, self.left_join \
                = self.left_join, self.top_join, self.right_join, self.bottom_join


input_tiles = parseMod.readCSV_row('data/20tiles.csv', '\n')

# tile dictionary will be id to Tile object
tile_dict = {}
tile = []
for row in input_tiles:
    row_on_tile = []
    if row.startswith('Tile'):  # save id
        id = int((row.split())[-1].strip(':'))
    else:  # is a row of the tile
        for letter in row:  # build row and tile
            row_on_tile.append(letter)
        tile.append(row_on_tile)

    if len(tile) == len(row):  # end when tile is square
        tile_dict[id] = Tile(tile, id)
        tile = []

# pair the sides - disgusting quantity of if statements
for t in tile_dict:  # go through each tile
    for t_match in tile_dict:
        if t_match != t:
            # top join
            if (tile_dict[t].top == tile_dict[t_match].top or tile_dict[t].top == list(reversed(tile_dict[t_match].top)))\
                    and tile_dict[t].top_join == 0:  # not matched yet
                tile_dict[t].top_join = t_match
                tile_dict[t_match].top_join = t
            elif (tile_dict[t].top == tile_dict[t_match].right or tile_dict[t].top == list(reversed(tile_dict[t_match].right)))\
                    and tile_dict[t].top_join == 0:
                tile_dict[t].top_join = t_match
                tile_dict[t_match].right_join = t
            elif (tile_dict[t].top == tile_dict[t_match].bottom or tile_dict[t].top == list(reversed(tile_dict[t_match].bottom)))\
                    and tile_dict[t].top_join == 0:
                tile_dict[t].top_join = t_match
                tile_dict[t_match].bottom_join = t
            elif (tile_dict[t].top == tile_dict[t_match].left or tile_dict[t].top == list(reversed(tile_dict[t_match].left)) )\
                    and tile_dict[t].top_join == 0:
                tile_dict[t].top_join = t_match
                tile_dict[t_match].left_join = t

            # right
            if (tile_dict[t].right == tile_dict[t_match].top or tile_dict[t].right == list(reversed(tile_dict[t_match].top)))\
                    and tile_dict[t].right_join == 0:
                tile_dict[t].right_join = t_match
                tile_dict[t_match].top_join = t
            elif (tile_dict[t].right == tile_dict[t_match].right or tile_dict[t].right == list(reversed(tile_dict[t_match].right)))\
                    and tile_dict[t].right_join == 0:
                tile_dict[t].right_join = t_match
                tile_dict[t_match].right_join = t
            elif (tile_dict[t].right == tile_dict[t_match].bottom or tile_dict[t].right == list(reversed(tile_dict[t_match].bottom)))\
                    and tile_dict[t].right_join == 0:
                tile_dict[t].right_join = t_match
                tile_dict[t_match].bottom_join = t
            elif (tile_dict[t].right == tile_dict[t_match].left or tile_dict[t].right == list(reversed(tile_dict[t_match].left)))\
                    and tile_dict[t].right_join == 0:
                tile_dict[t].right_join = t_match
                tile_dict[t_match].left_join = t

            # bottom
            if (tile_dict[t].bottom == tile_dict[t_match].top or tile_dict[t].bottom == list(reversed(tile_dict[t_match].top)))\
                    and tile_dict[t].bottom_join == 0:
                tile_dict[t].bottom_join = t_match
                tile_dict[t_match].top_join = t
            elif (tile_dict[t].bottom == tile_dict[t_match].right or tile_dict[t].bottom == list(reversed(tile_dict[t_match].right)))\
                    and tile_dict[t].bottom_join == 0:
                tile_dict[t].bottom_join = t_match
                tile_dict[t_match].right_join = t
            elif (tile_dict[t].bottom == tile_dict[t_match].bottom or tile_dict[t].bottom == list(reversed(tile_dict[t_match].bottom)))\
                    and tile_dict[t].bottom_join == 0:
                tile_dict[t].bottom_join = t_match
                tile_dict[t_match].bottom_join = t
            elif (tile_dict[t].bottom == tile_dict[t_match].left or tile_dict[t].bottom == list(reversed(tile_dict[t_match].left)))\
                    and tile_dict[t].bottom_join == 0:
                tile_dict[t].bottom_join = t_match
                tile_dict[t_match].left_join = t

            # left
            if (tile_dict[t].left == tile_dict[t_match].top or tile_dict[t].left == list(reversed(tile_dict[t_match].top)))\
                    and tile_dict[t].left_join == 0:
                tile_dict[t].left_join = t_match
                tile_dict[t_match].top_join = t
            elif (tile_dict[t].left == tile_dict[t_match].right or tile_dict[t].left == list(reversed(tile_dict[t_match].right)))\
                    and tile_dict[t].left_join == 0:
                tile_dict[t].left_join = t_match
                tile_dict[t_match].right_join = t
            elif (tile_dict[t].left == tile_dict[t_match].bottom or tile_dict[t].left == list(reversed(tile_dict[t_match].bottom)))\
                    and tile_dict[t].left_join == 0:
                tile_dict[t].left_join = t_match
                tile_dict[t_match].bottom_join = t
            elif (tile_dict[t].left == tile_dict[t_match].left or tile_dict[t].left == list(reversed(tile_dict[t_match].left))) \
                    and tile_dict[t].left_join == 0:
                tile_dict[t].left_join = t_match
                tile_dict[t_match].left_join = t

# find the unmatched corners
corners = []
for t_id in tile_dict:
    count_unmatched = (not tile_dict[t_id].top_join) + (not tile_dict[t_id].left_join)\
                      + (not tile_dict[t_id].bottom_join) + (not tile_dict[t_id].right_join)
    if count_unmatched == 2:
        corners.append(t_id)

print("Part 1 - corner ids product: ", math.prod(corners))

# part 2
# lets start with corner that has left and top missing right now
for corner in corners:
    if not tile_dict[corner].top_join and not tile_dict[corner].left_join:  break

# find board width in tiles (12 for actual problem), assemble picture
board_width_tiles = int(math.sqrt(len(tile_dict)))
picture_cut = [[0 for j in range(board_width_tiles)] for i in range(board_width_tiles)]

# first column to allow the rows to be generated
picture_cut[0][0] = tile_dict[corner]  # set initial upper left
for j in range(1, board_width_tiles):
    pic_down_id = picture_cut[j-1][0].bottom_join

    if tile_dict[pic_down_id].right_join == picture_cut[j-1][0].id_num:  # tile right side match
        if tile_dict[pic_down_id].top_join == 0:  # compare to one above it bottom join
            tile_dict[pic_down_id].rotate(270)
        else:
            tile_dict[pic_down_id].flip_h()
            tile_dict[pic_down_id].rotate(90)
    elif tile_dict[pic_down_id].top_join == picture_cut[j-1][0].id_num:  # tile top side match
        if tile_dict[pic_down_id].left_join == 0:
            pass
        else:
            tile_dict[pic_down_id].flip_h()
    elif tile_dict[pic_down_id].left_join == picture_cut[j-1][0].id_num:  # left side match
        if tile_dict[pic_down_id].top_join == 0:
            tile_dict[pic_down_id].flip_v()
            tile_dict[pic_down_id].rotate(90)
        else:
            tile_dict[pic_down_id].rotate(90)
    elif tile_dict[pic_down_id].bottom_join == picture_cut[j-1][0].id_num:  # bottom match
        if tile_dict[pic_down_id].left_join == 0:
            tile_dict[pic_down_id].flip_v()
        else:
            tile_dict[pic_down_id].rotate(180)

    picture_cut[j][0] = tile_dict[pic_down_id]

for j in range(0, board_width_tiles):  # do each row
    for x in range(1, board_width_tiles):  # do each element in row
        piece_id = picture_cut[j][x - 1].right_join
        above_piece_id = 0 if j == 0 else picture_cut[j-1][x].id_num  # either the piece above or top of map

        if tile_dict[piece_id].right_join == picture_cut[j][x - 1].id_num:  # tile right side match
            if tile_dict[piece_id].top_join == above_piece_id:  # compare to one above it bottom join
                tile_dict[piece_id].flip_h()
            else:
                tile_dict[piece_id].rotate(180)
        elif tile_dict[piece_id].top_join == picture_cut[j][x - 1].id_num:  # tile top side match
            if tile_dict[piece_id].left_join == above_piece_id:
                tile_dict[piece_id].rotate(90)
                tile_dict[piece_id].flip_h()
            else:
                tile_dict[piece_id].rotate(270)
        elif tile_dict[piece_id].left_join == picture_cut[j][x - 1].id_num:  # left side match
            if tile_dict[piece_id].top_join == above_piece_id:
                pass
            else:
                tile_dict[piece_id].flip_v()
        elif tile_dict[piece_id].bottom_join == picture_cut[j][x - 1].id_num:  # bottom match
            if tile_dict[piece_id].left_join == above_piece_id:
                tile_dict[piece_id].rotate(90)
            else:
                tile_dict[piece_id].flip_h()
                tile_dict[piece_id].rotate(90)

        picture_cut[j][x] = tile_dict[piece_id]

# now to assemble the true map
ocean_map = [[] for i in range(board_width_tiles*8)]
for t_y in range(board_width_tiles):
    for t_x in range(board_width_tiles):
        pattern = picture_cut[t_y][t_x].tile_pattern  # alias
        # remove the borders
        for row in pattern:
            row.pop(0)
            row.pop()
        pattern.pop(0)
        pattern.pop()

        # populate map with each element in the current tile
        for y in range(len(picture_cut[t_y][t_x].tile_pattern)):
            for x in range(len(picture_cut[t_y][t_x].tile_pattern[0])):
                ocean_map[t_y*8 + y].append(picture_cut[t_y][t_x].tile_pattern[y][x])

'''
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
'''
# representation of the sea monster and number of hashtags belonging to him
sea_monster = [(18, 0), (0, 1), (5, 1), (6, 1), (11, 1), (12, 1), (17, 1), (18, 1), (19, 1),
               (1, 2), (4, 2), (7, 2), (10, 2), (13, 2), (16, 2)]
sea_monster_hashtags = len(sea_monster)

# find possible maps by flipping the map and rotating - 8 maps
possible_maps = [ocean_map, list(reversed(ocean_map))]
for o_map in copy.deepcopy(possible_maps):
    temp = copy.deepcopy(o_map)
    for i in range(3):  # rotate 90, 180, 270
        temp = list(zip(*temp[::-1]))
        possible_maps.append(temp)

# count the number of sea monsters
count = 0
for ocean_map in possible_maps:  # check each possible map for sea monsters
    for y in range(len(ocean_map)-2):  # check every position
        for x in range(len(ocean_map[0])-19):
            match = True  # assume true until otherwise found
            for coordinates in sea_monster:  # check every coordinate for a possible monster
                if ocean_map[coordinates[1]+y][coordinates[0]+x] != '#':
                    match = False
                    break
            if match:  # if found a sea monster, count it
                count += 1
    if count != 0:  # if monsters found on this map, exit
        break
total_hashtags = sum(row.count('#') for row in ocean_map)

print("Part 2 - non sea monster #s: ", total_hashtags - count * sea_monster_hashtags)
