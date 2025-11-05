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

        # initialize edge relationships
        self.edges = [self.tile_pattern[0], [], self.tile_pattern[-1], []]  # top, right, bottom, left edges
        for i in range(len(self.tile_pattern)):
            self.edges[3].append(self.tile_pattern[i][0])
            self.edges[1].append(self.tile_pattern[i][-1])
        self.joins = [0, 0, 0, 0]  # Top Right Bottom Left joins

    # horizontal flip - switches top and bottom order and left and right sides
    def flip_h(self):
        for row in self.tile_pattern:
            row.reverse()
        self.joins[1], self.joins[3] = self.joins[3], self.joins[1]

    # vertical flip does opposite of horizontal
    def flip_v(self):
        self.tile_pattern.reverse()
        self.joins[0], self.joins[2] = self.joins[2], self.joins[0]

    # rotate at whatever the requested angle is
    def rotate(self, angle):
        # rotates the angle given
        for _ in range(int(angle/90)):
            self.tile_pattern = list(zip(*self.tile_pattern[::-1]))
            for r in range(len(self.tile_pattern)):  # fix a tuple thing
                self.tile_pattern[r] = list(self.tile_pattern[r])

            self.joins[0], self.joins[1], self.joins[2], self.joins[3] \
                = self.joins[3], self.joins[0], self.joins[1], self.joins[2]


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
        # for each edge in t, check if t_match has a match and if so, store the edge it's at in the join matrix
        if t_match != t:
            for i in range(4):  # edges are TOP, RIGHT, BOTTOM, LEFT, parallel with joins
                for j in range(4):
                    if (tile_dict[t].edges[i] == tile_dict[t_match].edges[j]
                        or tile_dict[t].edges[i] == list(reversed(tile_dict[t_match].edges[j]))) \
                        and tile_dict[t].joins[i] == 0:
                        tile_dict[t].joins[i] = t_match
                        tile_dict[t_match].joins[j] = t

# find the unmatched corners
corners = []
for t_id in tile_dict:
    count_unmatched = (not tile_dict[t_id].joins[0]) + (not tile_dict[t_id].joins[3])\
                      + (not tile_dict[t_id].joins[2]) + (not tile_dict[t_id].joins[1])
    if count_unmatched == 2:
        corners.append(t_id)

print("Part 1 - corner ids product: ", math.prod(corners))

# part 2
for corner in corners:  # start with corner with top and left missing match
    if not tile_dict[corner].joins[0] and not tile_dict[corner].joins[3]:  break

# find board width in tiles (12 for actual problem), assemble picture
board_width_tiles = int(math.sqrt(len(tile_dict)))  # assuming x by x grid
picture_wedges = [[0 for j in range(board_width_tiles)] for i in range(board_width_tiles)]

# populate first column to allow the rows to be generated
picture_wedges[0][0] = tile_dict[corner]  # set initial upper left
for j in range(1, board_width_tiles):
    pic_down_id = picture_wedges[j - 1][0].joins[2]  # id of the picture below, matches the bottom join
    if tile_dict[pic_down_id].joins[1] == picture_wedges[j - 1][0].id_num:  # tile right side match
        if tile_dict[pic_down_id].joins[0] == 0:  # compare to one above it bottom join
            tile_dict[pic_down_id].rotate(270)
        else:
            tile_dict[pic_down_id].flip_h()
            tile_dict[pic_down_id].rotate(90)
    elif tile_dict[pic_down_id].joins[0] == picture_wedges[j - 1][0].id_num:  # tile top side match
        if tile_dict[pic_down_id].joins[1] == 0:
            tile_dict[pic_down_id].flip_h()
    elif tile_dict[pic_down_id].joins[3] == picture_wedges[j - 1][0].id_num:  # left side match
        if tile_dict[pic_down_id].joins[0] == 0:
            tile_dict[pic_down_id].flip_v()
        tile_dict[pic_down_id].rotate(90)
    elif tile_dict[pic_down_id].joins[2] == picture_wedges[j - 1][0].id_num:  # bottom match
        if tile_dict[pic_down_id].joins[3] == 0:
            tile_dict[pic_down_id].flip_v()
        else:
            tile_dict[pic_down_id].rotate(180)

    picture_wedges[j][0] = tile_dict[pic_down_id]

for j in range(0, board_width_tiles):  # do each row
    for x in range(1, board_width_tiles):  # do each element in row
        piece_id = picture_wedges[j][x - 1].joins[1]  # match right join
        above_piece_id = 0 if j == 0 else picture_wedges[j - 1][x].id_num  # either the piece above or top of map
        if tile_dict[piece_id].joins[1] == picture_wedges[j][x - 1].id_num:  # tile right side match
            if tile_dict[piece_id].joins[0] == above_piece_id:  # compare to one above it bottom join
                tile_dict[piece_id].flip_h()
            else:
                tile_dict[piece_id].rotate(180)
        elif tile_dict[piece_id].joins[0] == picture_wedges[j][x - 1].id_num:  # tile top side match
            if tile_dict[piece_id].joins[3] == above_piece_id:
                tile_dict[piece_id].rotate(90)
                tile_dict[piece_id].flip_h()
            else:
                tile_dict[piece_id].rotate(270)
        elif tile_dict[piece_id].joins[3] == picture_wedges[j][x - 1].id_num:  # left side match
            if tile_dict[piece_id].joins[2] == above_piece_id:
                tile_dict[piece_id].flip_v()
        elif tile_dict[piece_id].joins[2] == picture_wedges[j][x - 1].id_num:  # bottom match
            if tile_dict[piece_id].joins[1] == above_piece_id:
                tile_dict[piece_id].flip_h()
            tile_dict[piece_id].rotate(90)

        picture_wedges[j][x] = tile_dict[piece_id]

# now to assemble the true map
ocean_map = [[] for i in range(board_width_tiles*8)]
for t_y in range(board_width_tiles):
    for t_x in range(board_width_tiles):
        pattern = picture_wedges[t_y][t_x].tile_pattern  # alias
        # remove the borders
        for row in pattern:
            row.pop(0)
            row.pop()
        pattern.pop(0)
        pattern.pop()

        # populate map with each element in the current_i tile
        for y in range(len(picture_wedges[t_y][t_x].tile_pattern)):
            for x in range(len(picture_wedges[t_y][t_x].tile_pattern[0])):
                ocean_map[t_y*8 + y].append(picture_wedges[t_y][t_x].tile_pattern[y][x])

''' --representation of the sea monster hashtag positions and number of hashtags belonging to him--
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
'''
sea_monster = [(18, 0), (0, 1), (5, 1), (6, 1), (11, 1), (12, 1), (17, 1), (18, 1), (19, 1),
               (1, 2), (4, 2), (7, 2), (10, 2), (13, 2), (16, 2)]
sea_monster_hashtags = len(sea_monster)

# find possible maps by flipping the map and rotating - 8 maps
possible_maps = [ocean_map, list(reversed(ocean_map))]
for o_map in copy.deepcopy(possible_maps):
    for i in range(3):  # rotate 90, 180, 270
        o_map = list(zip(*o_map[::-1]))
        possible_maps.append(o_map)

# count the number of sea monsters
sea_monster_count = 0
for ocean_map in possible_maps:  # check each possible map for sea monsters
    for y in range(len(ocean_map)-2):  # check every position
        for x in range(len(ocean_map[0])-19):
            match = True  # assume true until otherwise found
            for coordinates in sea_monster:  # check every coordinate for a possible monster
                if ocean_map[coordinates[1]+y][coordinates[0]+x] != '#':
                    match = False
                    break
            sea_monster_count += 1 if match else 0
    if sea_monster_count != 0:  # if monsters found on this map, exit
        for row in ocean_map:
            print(''.join(row))
        break
total_hashtags = sum(row.count('#') for row in ocean_map)

print("Part 2 - non sea monster #s: ", total_hashtags - sea_monster_count * sea_monster_hashtags)
