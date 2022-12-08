# Advent of Code 2022 Day 8
# Author:   Rachael Judy
# Date:     12/8/22
# Purpose:  check visibility from outside and inside grove of trees (dumb n^2 n^3 approach)

import parseMod

stage = 'b'
day = 8
year = 2022
parseMod.createDataFile(year=year, day=day)
trees = [[*map(int, row)] for row in parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")]


def transpose(matrix):
    transposed = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed[j][i] = matrix[i][j]
    return transposed


def mark_visible_horizontal(grid, visibility_matrix):
    for i in range(0, len(grid)):
        max_height = grid[i][0] - 1
        for j in range(0, len(grid[i])):
            visibility_matrix[i][j] = 1 if grid[i][j] > max_height else visibility_matrix[i][j]
            max_height = max(max_height, grid[i][j])

        max_height = grid[i][len(grid[i])-1] - 1
        for j in range(len(grid[i])-1, -1, -1):
            visibility_matrix[i][j] = 1 if grid[i][j] > max_height else visibility_matrix[i][j]
            max_height = max(max_height, grid[i][j])

    return visibility_matrix


def mark_sights_horizontal(grid, score):
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            count = 1
            for k in range(j-1, 0, -1):
                count += int(grid[i][k] < grid[i][j])
                if grid[i][k] >= grid[i][j]: break
            score[i][j] *= count

            count = 1
            for k in range(j+1, len(grid[i])-1):
                count += int(grid[i][k] < grid[i][j])
                if grid[i][k] >= grid[i][j]: break
            score[i][j] *= count

    return score


if stage == 'a':
    visible = [[0 for j in range(len(trees[0]))] for i in range(len(trees))]
    visible = mark_visible_horizontal(trees, visible)
    visible = mark_visible_horizontal(transpose(trees), transpose(visible))

    result = sum(sum(row) for row in visible)

else:
    # outer edges will always be zero, but leaving them one should be fine
    scene_score = [[1 for j in range(len(trees[0]))] for i in range(len(trees))]
    scene_score = mark_sights_horizontal(trees, scene_score)
    scene_score = mark_sights_horizontal(transpose(trees), transpose(scene_score))

    result = max(max(row) for row in scene_score)

print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
