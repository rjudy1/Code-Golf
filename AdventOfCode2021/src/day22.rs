// day 22 of advent of code 2021
// author: rachael judy
// date: 22 dec 2021
// turn on and off cubes in a large 3D space; track border cuboids/rectangular prisms

use std::cmp;
use std::collections::HashSet;

#[derive(Debug, Clone, Copy, Eq, PartialEq, Ord, PartialOrd, Hash)]
struct Cuboid {
    x : (i32, i32),
    y : (i32, i32),
    z : (i32, i32)
}
impl Cuboid {
    fn volume(&self) -> i64 {
        (self.x.1-self.x.0 + 1) as i64 * (self.y.1-self.y.0 + 1) as i64 * (self.z.1-self.z.0 + 1) as i64
    }
}

// keep on cuboids in the cubes hashmap, breaking down as necessary
fn switch(cubes : &mut HashSet<Cuboid>, cuba : Cuboid, on : bool) {
    // go through all cubes, splitting around intersection of cuboids to remove overlap and add subcuboids
    let mut cubes_to_add : Vec<Cuboid> = Vec::new();
    let mut cubes_to_remove : HashSet<Cuboid> = HashSet::new();
    for c in cubes.iter() {
        // if no intersection, no need to split this cuboid
        if cuba.x.0 > c.x.1 || cuba.x.1 < c.x.0 || cuba.y.0 > c.y.1 || cuba.y.1 < c.y.0 || cuba.z.0 > c.z.1 || cuba.z.1 < c.z.0 {
            continue;
        }
        // will remove the cube that has overlaps and replace with smaller
        cubes_to_remove.insert(c.clone());

        // make top and bottom prisms
        cubes_to_add.push(Cuboid{x:c.x, y:c.y, z:(cuba.z.1+1,c.z.1)});
        cubes_to_add.push(Cuboid{x:c.x, y:c.y, z:(c.z.0,cuba.z.0-1)});
        // left and right prisms - must account for possibilities of above and below
        cubes_to_add.push(Cuboid{x:(c.x.0,cuba.x.0-1), y:c.y,
            z:(cmp::max(cuba.z.0, c.z.0), cmp::min(cuba.z.1,c.z.1))});
        cubes_to_add.push(Cuboid{x:(cuba.x.1+1,c.x.1), y:c.y,
            z:(cmp::max(cuba.z.0, c.z.0), cmp::min(cuba.z.1,c.z.1))});
        // back and front prisms - same z as left/right, new constraints on xy
        cubes_to_add.push(Cuboid{
            x:(cmp::max(cuba.x.0, c.x.0), cmp::min(cuba.x.1,c.x.1)),
            y:(c.y.0,cuba.y.0-1),
            z:(cmp::max(cuba.z.0, c.z.0), cmp::min(cuba.z.1,c.z.1))});
        cubes_to_add.push(Cuboid{
            x:(cmp::max(cuba.x.0, c.x.0), cmp::min(cuba.x.1,c.x.1)),
            y:(cuba.y.1+1,c.y.1),
            z:(cmp::max(cuba.z.0, c.z.0), cmp::min(cuba.z.1,c.z.1))});
    }
    // add the sub cubes that are kept and remove the og cubes
    for cube in cubes_to_add {
        // only add cuboids that were actually part of the original cube and not negative space
        if cube.x.0 <= cube.x.1 && cube.y.0 <= cube.y.1 && cube.z.0 <= cube.z.1 {
            cubes.insert(cube);
        }
    }
    for cube in cubes_to_remove {
        cubes.remove(&cube);
    }

    // insert cubes if told to be on
    if on { cubes.insert(cuba); }
}

// compute total volume in the cuboids
fn total_volume(cubes : & HashSet<Cuboid>) -> i64 {
    let mut vol = 0;
    for cube in cubes {
        vol += cube.volume();
    }
    return vol
}

pub fn calculate(inp : Vec<String>) -> std::io::Result<()> {
    let mut instructions : Vec<(Cuboid, bool)> = Vec::new();
    for line in inp {
        let split_line = line.split(',').collect::<Vec<&str>>();
        let on = if line.chars().nth(1) == Some('n') {true} else {false};
        let x = split_line[0].split('=').collect::<Vec<&str>>()[1].split('.').collect::<Vec<&str>>();
        let (x1, x2) = (x[0].parse::<i32>().unwrap(), x[2].parse::<i32>().unwrap());
        let y = split_line[1].split('=').collect::<Vec<&str>>()[1].split('.').collect::<Vec<&str>>();
        let (y1, y2) = (y[0].parse::<i32>().unwrap(), y[2].parse::<i32>().unwrap());
        let z = split_line[2].split('=').collect::<Vec<&str>>()[1].split('.').collect::<Vec<&str>>();
        let (z1, z2) = (z[0].parse::<i32>().unwrap(), z[2].parse::<i32>().unwrap());
        instructions.push((Cuboid{x:(x1,x2), y:(y1,y2), z:(z1,z2)}, on));
    }

    let mut cubes : HashSet<Cuboid> = HashSet::new();
    for i in 0..instructions.len() {
        switch(&mut cubes, instructions[i].0,instructions[i].1);
        if i == 19 {println!("part 1: initialization count = {}", total_volume(&cubes)); }
    }
    println!("part 2: total volume = {}", total_volume(&cubes));
    Ok(())
}
