# Advent of Code 2023 Day 24
# Author:   Rachael Judy
# Date:     12/24/23
# Purpose:  Find hailstone paths that collide and create hailstone to collide with all

from sympy import symbols, solve
import parseMod

ready = False
day = 24
stage = 'b'
year = 2023

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")

hails = []
for line in data:
    pos, vel = line.strip().split(" @ ")
    px, py, pz = pos.split(", ")
    vx, vy, vz = vel.split(", ")
    hails.append((int(px), int(py), int(pz), int(vx), int(vy), int(vz)))

# make lines y=mx+b, check intersection from slopes and itnercepts
if stage == 'a':
    result = 0
    for adx in range(len(hails) - 1):
        shard_a = hails[adx]
        ma = shard_a[4] / shard_a[3]
        ba = shard_a[1] - ma * shard_a[0]
        for bdx in range(adx + 1, len(hails)):
            shard_b = hails[bdx]
            mb = shard_b[4] / shard_b[3]
            bb = shard_b[1] - mb * shard_b[0]
            if ma == mb and ba != bb:  # parallel lines, would create divide-by-zero on the next step, and won't intersection
                continue
            ix = (bb - ba) / (ma - mb)
            iy = ma * ix + ba
            ta = (ix - shard_a[0]) / shard_a[3]
            tb = (ix - shard_b[0]) / shard_b[3]

            if ta >= 0 and tb >= 0 and ix >= 200000000000000 and ix <= 400000000000000 and iy >= 200000000000000 and iy <= 400000000000000:
                result += 1
else:
    # can use any three
    x1, y1, z1, vx1, vy1, vz1 = hails[0]
    x2, y2, z2, vx2, vy2, vz2 = hails[1]
    x3, y3, z3, vx3, vy3, vz3 = hails[2]

    x, y, z = symbols('x'), symbols('y'), symbols('z')
    vx, vy, vz = symbols('vx'), symbols('vy'), symbols('vz')

    # equations for the cross products being the null vector
    equations = [
        # first hail
        (y1 - y) * (vz1 - vz) - (z1 - z) * (vy1 - vy),
        (z1 - z) * (vx1 - vx) - (x1 - x) * (vz1 - vz),
        (x1 - x) * (vy1 - vy) - (y1 - y) * (vx1 - vx),

        # second hail
        (y2 - y) * (vz2 - vz) - (z2 - z) * (vy2 - vy),
        (z2 - z) * (vx2 - vx) - (x2 - x) * (vz2 - vz),
        (x2 - x) * (vy2 - vy) - (y2 - y) * (vx2 - vx),

        # third hail
        (y3 - y) * (vz3 - vz) - (z3 - z) * (vy3 - vy),
        (z3 - z) * (vx3 - vx) - (x3 - x) * (vz3 - vz),
        (x3 - x) * (vy3 - vy) - (y3 - y) * (vx3 - vx)
    ]

    solution = solve(equations, [x, y, z, vx, vy, vz], dict=True)[0]
    result = solution[x] + solution[y] + solution[z]

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
