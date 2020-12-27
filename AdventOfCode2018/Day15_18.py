# Advent of Code 2018 - Day 15

# Author:   Rachael Judy
# Date:     12/25/2020
# Purpose:  Play movement game where units move in reading order

import copy
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


def print_board(inp):
    for row in inp:
        for char in row:
            if isinstance(char,tuple):
                print(char[0], end='')
            else:
                print(char, end='')
        print()


def move_character(inp, from_row, from_col, to_row, to_col, char):
    # Move character on grid, and increment the i value
    inp[from_row][from_col] = "."
    inp[to_row][to_col] = (char[0],char[1],True)
    return inp


# Attack weakest adjacent enemy, if one is there
# If multiple weakest enemies, attack in reading order
def attack(inp, row, col, enemy, damage=3):
    if not adjacent_enemy(inp, row, col, enemy):  # no adjacencies, no attack
        return inp, False

    # Create a dict of {coordinates: hp} for each adjacent enemy
    enemies = {}
    for coords in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:  # adj
        if inp[coords[0]][coords[1]][0] == enemy:
            # enemy (char_type, hp, already_moved_bool)
            enemies[coords] = inp[coords[0]][coords[1]][1]

    # keep min hitpoint enemy
    min_hp = min(enemies.values())
    enemies = [x for x in enemies if enemies[x]==min_hp]

    # sort list of coordinates to get reading order, then take the first to get our enemy
    enemies.sort()
    coords = enemies[0]

    enemy = inp[coords[0]][coords[1]]
    enemy_pts = enemy[1] - damage
    enemy_tup = (enemy[0], enemy_pts, enemy[2])

    # Check for kill
    if enemy_pts <= 0:
        inp[coords[0]][coords[1]] = "."
        return inp, True
    else:
        inp[coords[0]][coords[1]] = enemy_tup
        return inp, False


# Check for enemy in adjacent square
def adjacent_enemy(inp, rowI, colI, enemy):
    if any(x[0]==enemy for x in [inp[rowI+1][colI], inp[rowI-1][colI], inp[rowI][colI+1], inp[rowI][colI-1]]):
        return True
    return False


# takes list of possible best moves (first, number of moves, coordinates) and chooses based on conditions
def get_best_move(best_moves):
    if not best_moves:
        return None

    # fewest number of moves away
    min_steps = min([x[1] for x in best_moves])
    best_moves = [x for x in best_moves if x[1]==min_steps]

    # if tie, choose the first tile in reading order
    best_moves.sort(key=lambda x:x[2])
    best_moves = [x for x in best_moves if x[2]==best_moves[0][2]]

    # if tie, take the first step in reading order
    best_moves.sort(key = lambda x:x[0])
    best_moves = [x for x in best_moves if x[0]==best_moves[0][0]]

    return best_moves[0][0]


# count remaining
def count_characters(inp):
    seen = {"G":0, "E":0, ".":0, "#":0}
    for row in inp:
        for col in row:
            seen[col[0]]+=1
    return seen


# breadth first search on adjacent tile to make sorting easy
def bfs_move(inp, rowI, colI, hero, enemy):
    if adjacent_enemy(inp, rowI, colI, enemy):  # no move if adjacent
        return None

    first_moves = [(rowI+1, colI), (rowI-1, colI), (rowI, colI-1), (rowI, colI+1)]
    first_moves = [x for x in first_moves if inp[x[0]][x[1]]=="."]  # valid move on '.'

    # keep nearest tiles found in (first_move, num_moves, coordinates)
    best_moves = []
    for move in first_moves:
        r, c = move

        if adjacent_enemy(inp, r, c, enemy):
            best_moves.append((move, 1, move))
            continue

        # track seen tiles and new accessible tiles fo this one
        seen_coordinates = {(rowI,colI),(r,c)}
        stack = [(r+1,c),(r-1,c),(r,c-1),(r,c+1)]
        stack = [x for x in stack if inp[x[0]][x[1]]=="." and (x[0],x[1]) not in seen_coordinates]

        # bfs
        i = 1  #  Already have moved one tile at this point
        run = True
        while run:
            i += 1
            new_stack = []  # Keep track of the new tiles here
            for tile in stack:
                if tile in seen_coordinates:
                    continue

                seen_coordinates.add(tile)
                r, c = tile
                if adjacent_enemy(inp, r, c, enemy):
                    best_moves.append((move,i,(r,c)))
                    # got to keep checking in case other equivalent moves
                    run = False
                    continue

                # Add all newly accessible tiles to queue
                new_tiles = [(r+1,c),(r-1,c),(r,c-1),(r,c+1)]
                new_stack += [x for x in new_tiles if inp[x[0]][x[1]]=="." and (x[0],x[1]) not in seen_coordinates]

            stack = list(set(new_stack))
            if not stack:  # finished exploring
                run = False

    # Take our list of the best_moves from each starting point that we generated, and find the one move we'll take
    return get_best_move(best_moves)


def score_game(inp, rounds):
    pts = 0
    for rowI, row in enumerate(inp):
        for colI, col in enumerate(row):
            pts += col[1] if col[0] in ['G', 'E'] else 0
    return rounds*pts


def reset_moved_bools(inp):
    for rowI,row in enumerate(inp):
        for colI,col in enumerate(row):
            if col[0] in ["G","E"]:
                inp[rowI][colI] = (col[0], col[1], False)
    return inp


def problem1(grid, print_=False):
    rounds = 0
    while True:  # keep track of the number of each type
        counts = count_characters(grid)

        for rowI, row in enumerate(grid):
            for colI, col in enumerate(row):
                char = grid[rowI][colI]
                if isinstance(char, tuple):
                    if char[2]:  # already moved
                        continue

                    r,c = rowI,colI  # Keep track of our current coordinates in case we move
                    hero = char[0]
                    enemy = "G" if hero=="E" else "E"
                    counts[hero]-=1

                    move_to = bfs_move(grid, rowI, colI, hero, enemy)  # do a bfs of moves
                    if move_to:
                        r,c = move_to  # update coordinates
                        grid = move_character(grid, rowI, colI, r, c, char)

                    grid, death = attack(grid, r, c, enemy)
                    if death:
                        current_counts = count_characters(grid)  # is game over?
                        game_over = any(x==0 for x in current_counts.values())
                        if game_over:  # is round complete?
                            if counts[hero]>0:  # round incomplete
                                final_score = score_game(grid, rounds)
                            else:  # round over
                                rounds+=1
                                final_score = score_game(grid, rounds)
                            if print_:
                                print("GAME OVER", rounds)
                                print_board(grid)

                            return final_score

        grid = reset_moved_bools(grid)
        rounds += 1

        if print_:  # display each round if true
            print(rounds)
            print_board(grid)


# nearly identical to problem 1 with repetition
def problem2_loop(grid, damage_dict, print_=False):
    rounds = 0

    while True:  # similar to round 1
        counts = count_characters(grid)

        for rowI,row in enumerate(grid):
            for colI,col in enumerate(row):
                char = grid[rowI][colI]
                if isinstance(char, tuple):
                    if char[2]:
                        continue

                    r,c = rowI,colI  # track current coordinates in case we move
                    hero = char[0]
                    enemy = "G" if hero=="E" else "E"
                    counts[hero]-=1

                    move_to = bfs_move(grid, rowI, colI, hero, enemy)
                    if move_to:
                        r,c = move_to
                        grid = move_character(grid, rowI, colI, r, c, char)

                    damage = damage_dict[hero]
                    grid, death = attack(grid, r, c, enemy, damage)
                    if death and enemy=="E":  # lost an elf, this won't do
                        return False
                    elif death:
                        current_counts = count_characters(grid)  # check end
                        game_over = any(x==0 for x in current_counts.values())

                        if game_over:
                            if counts[hero]>0:
                                final_score = score_game(grid, rounds)
                            else:
                                rounds+=1
                                final_score = score_game(grid, rounds)
                            if print_:
                                print("GAME ENDED", rounds)
                                print_board(grid)

                            return final_score

        grid = reset_moved_bools(grid)
        rounds += 1

        if print_:
            print(rounds)
            print_board(grid)


def problem2(inp, print_=False):
    score = False
    damage_dict = {"G":3, "E":3}
    while not score:  # advance elf damage until a win is returned
        damage_dict["E"] += 1
        score = problem2_loop(copy.deepcopy(inp), damage_dict, print_)
    return score


board = parseMod.readCSV_row('data/15game.csv', '\n')
for j, row in enumerate(board):
    print(row)
    board[j] = list(board[j])
    for i, c in enumerate(board[j]):
        if c in ['G', 'E']:
            board[j][i] = (c, 200, False)

print("part 1: ", problem1(copy.deepcopy(board)))
print("part 2: ", problem2(board))
