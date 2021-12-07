// day 6 of advent of code 2021
// author: rachael judy
// date: 6 dec 2021
// count fish at day n

use std::io::prelude::*;
use std::vec::Vec;
use std::cmp;

fn get_fish_at_day(inp : Vec<i32>, day : i32) -> Vec<i32>{
    let mut fish = inp.clone();
    for i in 0..day {
        for j in 0..fish.len() {
            if fish[j] == 0 {
                fish.push(8);
            }

            if fish[j] == 0 { fish[j] = 6;
            } else {          fish[j] -= 1; }
        }
    }
    return fish
}

fn get_count_at_days_256() -> Vec<i64> {
    let mut multiplicities: Vec<i32> = vec![0; 9];
    let mut fish : Vec<Vec<i32>> = vec![vec![0; 1]; 9];
    for i in 0..9 {
        fish[i] = get_fish_at_day(vec![i as i32;1], 128);
        multiplicities[i as usize] = fish[i].len() as i32;
    }

    let mut sum : Vec<i64> = vec![0; 9];
    for i in 0..fish.len() {
        for j in 0..fish[i].len() {
            sum[i] += multiplicities[fish[i][j] as usize] as i64;
        }
    }
    return sum
}

pub fn calculate(fish : Vec<i32>, stage : i32) -> std::io::Result<()> {
    println!("Stage {}", stage);

    // let mut fish = inp.clone();
    if stage == 1 {
        let fish80 = get_fish_at_day(fish, 80);
        println!("Fish at day 80: {}", fish80.len());
    } else {
        // gets fish count based on having a single fish with numbers 1-9
        let mut x = get_count_at_days_256();
        let mut sum = 0;
        for i in 0..fish.len() {
            sum += x[fish[i] as usize];
        }
        println!("Fish at day 128: {}", sum);
    }
    Ok(())
}
