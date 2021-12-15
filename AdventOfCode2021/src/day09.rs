// day 9 of advent of code 2021
// author: rachael judy
// date: 9 dec 2021
// find the local minima and their basin sizes

use std::vec::Vec;

fn branch(map : Vec<Vec<u32>>, x : usize, y : usize, chk: &mut Vec<(usize, usize)>) -> i32{
    let mut basin = 1; // count the one we're on now
    if map[x][y] < map[x][y+1] && map[x][y+1] < 9 && !chk.contains(&(x, y+1)){ // check down
        chk.push((x, y+1));
        basin+=branch(map.clone(), x, y+1, chk); }
    if map[x][y] < map[x][y-1] && map[x][y-1] < 9 && !chk.contains(&(x, y-1)){
        chk.push((x, y-1));
        basin+=branch(map.clone(), x, y-1, chk); }
    if map[x][y] < map[x+1][y] && map[x+1][y] < 9 && !chk.contains(&(x+1, y)){
        chk.push((x+1, y));
        basin+=branch(map.clone(), x+1, y, chk); }
    if map[x][y] < map[x-1][y] && map[x-1][y] < 9 && !chk.contains(&(x-1, y)){
        chk.push((x-1, y));
        basin+=branch(map.clone(), x-1, y, chk); }
    return basin;
}

pub fn calculate(inp : Vec<String>) -> std::io::Result<()> {
    let mut map = vec![vec![10; inp[0].len()+2]; inp.len()+2];
    for i in 0..inp.len() {
        map[i+1] = inp[i].chars().map(|c| c.to_digit(10).unwrap()).collect();
        map[i+1].push(10); // pad front and back so can just check all four corners
        map[i+1].insert(0, 10);
    }

    let mut risk = 0;
    let mut basins : Vec<i32> = Vec::new();
    for i in 1..map.len()-1 {
        for j in 1..map[0].len()-1 {
            if map[i][j] < map[i-1][j] && map[i][j] < map[i+1][j]
                && map[i][j] < map[i][j-1] && map[i][j] < map[i][j+1] {
                risk += map[i][j]+1; // risk is value + 1 at minima
                basins.push(branch(map.clone(), i, j, &mut vec![(i, j)]));
            }
        }
    }
    println!("Stage 1: Risk: {}", risk);
    basins.sort();
    println!("Stage 2: Basin max product: {}", basins[basins.len()-1]*basins[basins.len()-2]*basins[basins.len()-3]);
    Ok(())
}