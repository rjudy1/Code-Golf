// day 15 of advent of code 2021
// author: rachael judy
// date: 15 dec 2021
// djikstra's algorithm to find least risky path between the upper left and bottom right
//      could be improved with a priority queue; runtime is kind of terrible (6 min)

use std::vec::Vec;
use std::collections::HashMap;
use std::cmp;
use std::time::{Duration, SystemTime};

fn update_neighbor(map : Vec<Vec<usize>>, src : (usize, usize), nbr : &mut Vec<(usize, usize)>,
                   cost : &mut HashMap<(usize,usize), i32>,
                   visited : &mut HashMap<(usize, usize), bool>, edge : usize) {
    if src.0 > 0 && !*visited.get_mut(&(src.0-1, src.1)).unwrap() {
        nbr.push((src.0-1, src.1));
        *cost.get_mut(&(src.0 - 1, src.1)).unwrap()
            = cmp::min(cost[&src] + map[src.0 - 1][src.1] as i32, cost[&(src.0 - 1, src.1)]);
    }
    if src.0 < edge-1 && !*visited.get_mut(&(src.0+1, src.1)).unwrap() {
        nbr.push((src.0+1, src.1));
        *cost.get_mut(&(src.0 + 1, src.1)).unwrap()
            = cmp::min(cost[&src] + map[src.0 + 1][src.1] as i32, cost[&(src.0 + 1, src.1)]);
    }
    if src.1 > 0 && !*visited.get_mut(&(src.0, src.1-1)).unwrap() {
        nbr.push((src.0, src.1-1));
        *cost.get_mut(&(src.0, src.1 - 1)).unwrap()
            = cmp::min(cost[&src] + map[src.0][src.1 - 1] as i32, cost[&(src.0, src.1 - 1)]);
    }
    if src.1 < edge-1 && !*visited.get_mut(&(src.0, src.1+1)).unwrap() {
        nbr.push((src.0, src.1+1));
        *cost.get_mut(&(src.0, src.1 + 1)).unwrap()
            = cmp::min(cost[&src] + map[src.0][src.1 + 1] as i32, cost[&(src.0, src.1 + 1)]);
    }
}

fn djikstra(map : Vec<Vec<usize>>, src : (usize, usize), cost : &mut HashMap<(usize, usize), i32>) {
    // set source, create neighbors and visited collections
    let mut src = src;
    let mut neighbors : Vec<(usize, usize)> = Vec::new();
    let mut visited : HashMap<(usize, usize), bool> = HashMap::new();
    for i in 0..map.len() {
        for j in 0..map[0].len() {
            visited.insert((i, j), false);
        }
    }

    // loop until source is matched - shortcut out if in middle
    for i in 0..map.len()*map.len() { // big enough for all points
        neighbors.retain(|&x| x != src); // remove source node from the neighbors
        *visited.get_mut(&src).unwrap() = true;  // mark source node visited

        // update neighbors of visited nodes and find next source (minimum distance node)
        update_neighbor(map.clone(), src, &mut neighbors, cost, &mut visited, map.len());
        let mut mini = 100000;
        for loc in neighbors.clone() {
            if cost[&loc] < mini {
                mini = cost[&loc];
                src = loc.clone();
            }
        }

        if i % 10000 == 0 { println!("on iteration {}", i); }
        if neighbors.len() == 0 || src == (map.len()-1, map[0].len()-1) { break; }
    }
}

pub fn calculate(inp : Vec<String>, stage : i32) -> std::io::Result<()> {
    let now = SystemTime::now(); // for timer
    let mut map = vec![vec![1000 as usize; inp[0].len()]; inp.len()];
    for i in 0..inp.len() {
        map[i] = inp[i].chars().map(|c| c.to_digit(10).unwrap() as usize).collect();
    }

    // stage 2 expands map
    if stage == 2 {
        // while map is missing rows up to 5*size of og grid, add rows and columns
        while map.len() != inp.len()*5 { map.push(Vec::new()); }
        for i in 0..inp.len()*5 {
            while map[i].len() != inp[0].len()*5 { map[i].push(1000); }
        }
        for i in inp.len()..inp.len()*5 {  // go down the rows, incrementing by one by grid
            for m in 0..100 { // do full table
                map[i][m] = match map[i-100][m] {9 => 1, _ => map[i-100][m]+1};
            }
        }
        for i in 0..inp.len()*5 {  // go over columns
            for j in inp[0].len()..inp[0].len()*5 {
                map[i][j] = match map[i][j-100] {9 => 1, _ => map[i][j-100]+1};
            }
        }
    }

    let mut cost : HashMap<(usize, usize), i32> = HashMap::new();
    for i in 0..map.len() {
        for j in 0..map[0].len() {
            cost.insert((i, j), 1000000);
        }
    }

    *cost.get_mut(&(0, 0)).unwrap() = 0;
    djikstra(map.clone(), (0, 0), &mut cost);
    println!("Time: {} s", now.elapsed().unwrap().as_millis() as f32 / 1000 as f32);
    println!("Stage {} cost: {}", stage, cost[&(map.len()-1, map.len()-1)]);
    Ok(())
}