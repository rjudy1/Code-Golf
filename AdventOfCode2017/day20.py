# Advent of Code 2017 Day 20
# Author:   Rachael Judy
# Purpose:  3D particle dynamics (acc dominates for a) and elimination by collision in space (b)

import re
from collections import namedtuple, Counter

import parseMod

ready = True
day = 20
stage = 'b'
year = 2017

data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv", )

Particle = namedtuple('Particle', ['pos', 'vel', 'acc'])
particles = [Particle(tuple(map(int, m[:3])), tuple(map(int, m[3:6])), tuple(map(int, m[6:9]))) for line in data
             for m in [re.findall(r'-?\d+', line)] ]
if stage == 'a':
    # particle with smallest acceleration, with ties broken by velocity, with ties broken by position
    result = min(range(len(particles)), key=lambda i: (sum(map(abs, particles[i].acc)), sum(map(abs, particles[i].vel)), sum(map(abs, particles[i].pos))))
else:
    def move_particle(particle):
        new_v = tuple(v + a for v, a in zip(particle.vel, particle.acc))
        return Particle(tuple(p + v for p, v in zip(particle.pos, new_v)), new_v, particle.acc)
    for _ in range(100):  # assume this is enough, could find the equations pairwise but must account for time of hit
        counts = Counter(p.pos for p in particles)
        particles = [move_particle(p) for p in particles if counts[p.pos] == 1]
    result = len(particles)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
