// day 19 of advent of code 2021
// author: rachael judy
// date: 19 dec 2021
//

use std::time::{Duration, SystemTime};
use std::ops::Add;
use std::ops::Sub;

// point struct has implemented methods, derive from standard
#[derive(Debug, Clone, Copy, Eq, PartialEq, Ord, PartialOrd, Hash)]
struct Point {
    x: i32,
    y: i32,
    z: i32,
}
impl Add for Point {
    type Output = Point;
    fn add(self, other: Point) -> Point {
        Point { x: self.x + other.x, y: self.y + other.y, z: self.z + other.z, }
    }
}
impl Sub for Point {
    type Output = Point;
    fn sub(self, other: Point) -> Point {
        Point { x: self.x - other.x, y: self.y - other.y, z: self.z - other.z, }
    }
}

// return rotation of a point based on the index chosen
fn get_rotation(v: Point, index: usize) -> Point {
    return match index {
        0 => Point { x: v.z, y: v.y, z: -v.x, }, 1 => Point { x: -v.z, y: -v.y, z: -v.x, },
        2 => Point { x: -v.z, y: -v.x, z: v.y, }, 3 => Point { x: -v.z, y: v.x, z: -v.y, },
        4 => Point { x: -v.z, y: v.y, z: v.x, }, 5 => Point { x: -v.y, y: -v.z, z: v.x, },
        6 => Point { x: -v.y, y: -v.x, z: -v.z, }, 7 => Point { x: -v.y, y: v.x, z: v.z, },
        8 => Point { x: -v.y, y: v.z, z: -v.x, }, 9 => Point { x: -v.x, y: -v.z, z: -v.y, },
        10 => Point { x: -v.x, y: -v.y, z: v.z, }, 11 => Point { x: -v.x, y: v.y, z: -v.z, },
        12 => Point { x: -v.x, y: v.z, z: v.y, }, 13 => Point { x: v.x, y: -v.z, z: v.y, },
        14 => Point { x: v.x, y: -v.y, z: -v.z, }, 15 => Point { x: v.x, y: v.y, z: v.z, },
        16 => Point { x: v.x, y: v.z, z: -v.y, }, 17 => Point { x: v.y, y: -v.z, z: -v.x, },
        18 => Point { x: v.y, y: -v.x, z: v.z, }, 19 => Point { x: v.y, y: v.x, z: -v.z, },
        20 => Point { x: v.y, y: v.z, z: v.x, }, 21 => Point { x: v.z, y: -v.y, z: v.x, },
        22 => Point { x: v.z, y: -v.x, z: -v.y, }, 23 => Point { x: v.z, y: v.x, z: v.y, },
        _ => Point { x: 0, y: 0, z: 0 },
    };
}

// check if points map so can be overlapped/look at rotation matches
fn overlaps(a: &Vec<Point>, b: &Vec<Point>, offset: Point, orientation: usize) -> bool {
    let mut matches = 0;
    for point_a in a {
        for point_b in b {
            let b_adjusted = offset + get_rotation(*point_b, orientation);
            if *point_a == b_adjusted {
                matches += 1;
                if matches >= 12 { return true; }
                break;
            }
        }
    }
    return false;
}

// return the overlap if found
fn find_overlaps(a: &Vec<Point>, b: &Vec<Point>) -> Option<(Point, usize)> {
    for i in 0..a.len() {
        let point_a = a[i];
        for j in 0..b.len() {
            let point_b = b[j];
            for orientation in 0..24 {
                let offset = point_a - get_rotation(point_b, orientation);
                if overlaps(a, b, offset, orientation) {
                    return Some((offset, orientation));
                }
            }
        }
    }
    return None;
}

// rotate to proper position
fn orient_points(points: &Vec<Point>, orientation: usize, offset: Point) -> Vec<Point> {
    let mut result = Vec::new();
    for p in points {
        result.push(offset + get_rotation(*p, orientation));
    }
    return result;
}

fn orient_beacons(scanners: Vec<Vec<Point>>) -> (usize, Vec<Point>) {
    let mut scanners = scanners.clone();
    let mut offsets = vec![Point{x:0,y:0,z:0}; scanners.len()];
    let mut is_oriented = vec![false; scanners.len()];
    is_oriented[0] = true;

    // find overlaps and set up
    loop {
        let mut done = true;
        for i in 0..scanners.len() - 1 {
            for j in i + 1..scanners.len() {
                if is_oriented[i] == is_oriented[j] {
                    continue;
                }
                done = false;
                let idx_a = if is_oriented[i] { i } else { j };
                let idx_b = if is_oriented[i] { j } else { i };
                let overlaps = find_overlaps(&scanners[idx_a], &scanners[idx_b]);

                if overlaps.is_some() {
                    let (offset, orientation) = overlaps.unwrap();
                    offsets[idx_b] = offset;
                    scanners[idx_b] = orient_points(&scanners[idx_b], orientation, offset);
                    is_oriented[idx_b] = true;
                }
            }
        }
        if done {
            break;
        }
    }
    // get actual beacons, kill duplicates
    let mut beacons = Vec::new();
    for scanner in scanners {
        for point in scanner {
            beacons.push(point);
        }
    }
    beacons.sort();
    beacons.dedup();
    return (beacons.len(), offsets);
}

pub fn calculate(inp : Vec<String>) -> std::io::Result<()> {
    let now = SystemTime::now();
    let mut scanmaps : Vec<Vec<Point>> = Vec::new();
    let mut scanner = -1;
    for row in 0..inp.len() {
        if inp[row].len() == 0 {
            continue;
        } else if &(&inp[row])[0..2] == "--" {
            scanmaps.push(Vec::new());
            scanner += 1;
        } else {
            let values = inp[row].split(',').collect::<Vec<&str>>();
            scanmaps[scanner as usize].push(Point { x: values[0].parse::<i32>().unwrap(),
                y: values[1].parse::<i32>().unwrap(), z: values[2].parse::<i32>().unwrap() });
        }
    }

    // orient the beacons
    let (num_beacons, positions) = orient_beacons(scanmaps);

    // part 2 manhatten distance
    let mut max = 0;
    for i in 0..positions.len() {
        let p0 = positions[i];
        for j in i + 1..positions.len() {
            let p1 = positions[j];
            let mag = (p0.x - p1.x).abs() + (p0.y - p1.y).abs() + (p0.z - p1.z).abs();
            max = std::cmp::max(max, mag);
        }
    }

    println!("Time: {} s", now.elapsed().unwrap().as_millis() as f32 / 1000 as f32);
    println!("Part one: {}", num_beacons);
    println!("Part two: {}", max);
    Ok(())
}


