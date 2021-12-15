// day 12 of advent of code 2021
// author: rachael judy
// date: 12 dec 2021
// count paths through graphs

use std::vec::Vec;
use std::collections::HashMap;

fn count_paths(u : &str, dest : &str, visited : HashMap<&str, i32>, adj : &Vec<(&str, &str)>, path_count :  &mut i32) {
    if u == dest { // path to end found
        *path_count += 1;
    }
    else {
        let mut visited = visited.clone(); // copy of the visited map
        // recurse for all adjacent to the current
        *visited.get_mut(u).unwrap() -= 1; // will reduce visited to zero
        for i in 0..adj.len() {
            if adj[i].0 == u && (visited[adj[i].1] != 0
                || adj[i].1.chars().nth(0).unwrap().is_ascii_uppercase()) {
                count_paths(adj[i].1, dest, visited.clone(), adj, path_count);
            } else if adj[i].1 == u && (visited[adj[i].0] != 0
                || adj[i].0.chars().nth(0).unwrap().is_ascii_uppercase()) {
                count_paths(adj[i].0, dest, visited.clone(), adj, path_count);
            }
        }
    }
}

pub fn calculate(inp : Vec<String>) -> std::io::Result<()> {
    // store adjacencies of graph, visited map, and points in input
    let mut points : Vec<&str> = Vec::new();
    let mut adj : Vec<(&str, &str)> = Vec::new();
    let mut visited_n: HashMap<&str, i32> = HashMap::new();
    for i in 0..inp.len() {
        let split_line : Vec<&str> = inp[i].split("-").collect();
        adj.push((split_line[0], split_line[1])); // adjacency
        visited_n.insert(split_line[0], 1); // if not present, insert nodes in visited
        visited_n.insert(split_line[1], 1);
        if !points.contains(&split_line[0]) { // insert unique points
            points.push(split_line[0]);
        }
        if !points.contains(&split_line[1]) {
            points.push(split_line[1]);
        }
    }

    // part 1 - count paths through graph with lower only visited once
    let mut path_count = 0;
    count_paths("start", "end", visited_n.clone(), &adj, &mut path_count);
    println!("Part 1: {} paths", path_count);

    // part 2 - count paths with a single lower being able to be visited twice
    let mut full_path_count = path_count; // will sum all the possible paths to here
    for i in 0..points.len() { // go through each point and use if a lowercase one
        let mut new_count = 0;
        let mut visitedi = visited_n.clone();
        if points[i].chars().nth(0).unwrap().is_ascii_lowercase()
            && points[i] != "start" && points[i] != "end" {
            *visitedi.get_mut(points[i]).unwrap() = 2; // give the single one two chances
        }
        count_paths("start", "end", visitedi.clone(), &adj, &mut new_count);
        full_path_count += new_count-path_count;
    }
    println!("Part 2: {} paths", full_path_count);
    Ok(())
}
