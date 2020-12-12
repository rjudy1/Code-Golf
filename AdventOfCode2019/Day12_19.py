# Advent of Code 2019 - Day 12

# Author:   Rachael Judy
# Date:     12/5/2020
# Purpose:  Calculate energies of moons around Jupiter - O(step * iterations^2) - part 1
#           Find when the positions repeat - part 2
#               takes about 7s - could be more efficient


import copy


# set velocities with gravity
def Generate_Gravity(moons_position, moons_velocity, dim):
    # hand in (w,x,y,z) for positions and velocity
    # simulate gravity by finding position relative to all moons and adjusting velocity accordingly
    for moon in range(len(moons_position)):
        for other in range(len(moons_position)):
            if moons_position[other][dim] > moons_position[moon][dim]:
                moons_velocity[moon][dim] += 1
            elif moons_position[other][dim] < moons_position[moon][dim]:
                moons_velocity[moon][dim] -= 1


# execute the velocities
def Step(moons_position, moons_velocity, dim):
    # execute the velocity
    for moon in range(len(moons_position)):
        moons_position[moon][dim] += moons_velocity[moon][dim]


def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm


""" Start Positions - hard coded
<x=-2, y=9, z=-5>
<x=16, y=19, z=9>
<x=0, y=3, z=6>
<x=11, y=0, z=11>
"""
moons_position = [[-2, 9, -5], [16, 19, 9], [0, 3, 6], [11, 0, 11]]
moons_velocity = [[0, 0, 0] for i in range(4)]
moons_position_initial = copy.deepcopy(moons_position)
moons_velocity_initial = copy.deepcopy(moons_velocity)


# step through - part 1
step_limit = 1000
moons_energy = [0, 0, 0, 0]
for step in range(step_limit):
    # simulate gravity by finding position relative to all moons and adjusting velocity accordingly
    for dim in range(3):
        Generate_Gravity(moons_position, moons_velocity, dim)
        Step(moons_position, moons_velocity, dim)

# determine energy at end - part 1
total_energy = 0
for m in range(len(moons_position)):
    total_energy += (abs(moons_position[m][0]) + abs(moons_position[m][1]) + abs(moons_position[m][2])) \
                   * (abs(moons_velocity[m][0]) + abs(moons_velocity[m][1]) + abs(moons_velocity[m][2]))

print("Energy:", total_energy)


# find time when cycle starts and repeats - part 2
# find LCM of periods for each dimension
# reset initial conditions to find match
moons_position = copy.deepcopy(moons_position_initial)
moons_velocity = copy.deepcopy(moons_velocity_initial)
xyz_repeat_time = [0, 0, 0]
for dim in range(3):
    while True:  # iterate until conditions are found again, tracking steps
        Generate_Gravity(moons_position, moons_velocity, dim)
        Step(moons_position, moons_velocity, dim)
        xyz_repeat_time[dim] += 1

        # see if match found
        match = True
        for i in range(4):  # check all four moons in the current dimension
            if moons_position[i][dim] != moons_position_initial[i][dim] \
                or moons_velocity[i][dim] != moons_velocity_initial[i][dim]:
                match = False
                break

        if match:
            break

# find LCM of steps to repetition
lcm = compute_lcm(xyz_repeat_time[0], xyz_repeat_time[1])
lcm = compute_lcm(lcm, xyz_repeat_time[2])
print("Steps at Repeat: ", lcm)
