// day 7 of advent of code 2021
// author: rachael judy
// date: 7 dec 2021
// calculate minimum distance point between all points

use std::io::prelude::*;
use std::vec::Vec;
use std::cmp;

pub fn calculate(inp : Vec<i32>, stage : i32) -> std::io::Result<()> {
    println!("Stage {}", stage);

    let mut mini :i64 = 10000000000; // find min in distances
    for i in 0..inp.iter().max().unwrap()+1 { // possible distances
        let mut distance = 0;
        for j in 0..inp.len() {
            if stage == 1 { // one move costs one fuel, also equal to univariate median
                distance += (i-inp[j]).abs() as i64;
            } else {        // each move costs one more fuel than previous
                distance += (((i-inp[j]).abs() + 1) * (i-inp[j]).abs() / 2) as i64;
            }
        }
        mini = cmp::min(distance, mini); // store smallest distance
    }
    println!("Fuel Burned: {}", mini);
    Ok(())
}
