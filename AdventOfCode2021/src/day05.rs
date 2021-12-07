// day 5 of advent of code 2021
// author: rachael judy
// date: 5 dec 2021
// find overlaps in map

use std::io::prelude::*;
use std::vec::Vec;
use std::cmp;

pub fn calculate(inp : Vec<String>, stage : i32) -> std::io::Result<()> {
    println!("Stage {}", stage);

    // read coords
    let mut coords = vec![vec![0; 4]; inp.len()]; // 500 rows, 4 col
    for i in 0..inp.len() {
        let parts : Vec<&str> = (&inp[i]).split_whitespace().collect();
        let p1 : Vec<&str>= parts[0].split(',').collect();
        let p2 : Vec<&str> = parts[2].split(',').collect();
        coords[i][0] = p1[0].parse::<i32>().unwrap();
        coords[i][1] = p1[1].parse::<i32>().unwrap();
        coords[i][2] = p2[0].parse::<i32>().unwrap();
        coords[i][3] = p2[1].parse::<i32>().unwrap();
    }

    // make map
    let mut map = vec![vec![0; 1000]; 1000]; // should be large enough as only 3 digit
    for i in 0..coords.len() {
        if coords[i][0] == coords[i][2] {
            for j in cmp::min(coords[i][1], coords[i][3])..=cmp::max(coords[i][1], coords[i][3]) {
                map[coords[i][0] as usize][j as usize] += 1;
            }
        } else if coords[i][1] == coords[i][3] {
            for j in cmp::min(coords[i][0], coords[i][2])..=cmp::max(coords[i][0], coords[i][2]) {
                map[j as usize][coords[i][1] as usize] += 1;
            }
        } else if stage == 2 { // filter in diagonal lines also
            let mut inc = 1;
            let mut y = cmp::min(coords[i as usize][1], coords[i as usize][3]);
            if (coords[i][1]-coords[i][3]) / (coords[i][0] - coords[i][2]) < 0 {
                inc = -1;
                y = cmp::max(coords[i as usize][1], coords[i as usize][3]);
            }
            for k in cmp::min(coords[i][0], coords[i][2])..=cmp::max(coords[i][0], coords[i][2]) {
                map[k as usize][y as usize] += 1;
                y += inc;
            }
        }
    }

    // count overlaps
    let mut count_overlaps = 0;
    for i in  0..map.len() {
        for j in 0..map[0].len() {
            if map[i][j] > 1 { count_overlaps +=1; }
        }
    }

    println!("{} overlaps", count_overlaps);
    Ok(())
}
