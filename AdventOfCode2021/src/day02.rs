// day 2 of advent of code 2021
// author: rachael judy
// date: 2 dec 2021

use std::io;
use std::io::prelude::*;
use std::vec::Vec;

pub fn calculate(numbers : Vec<String>, stage : i32) -> std::io::Result<()> {
    // set stage to 1 or 2
    let mut diff=1;
    if stage==2 {
        diff=3;
    }

    let mut forw = 0;
    let mut depth = 0;
    let mut aim = 0;
    println!("{}", numbers[4]);

    for i in 0..numbers.len() {
        println!("{} {}", numbers[i], numbers[i].len());
        let change  = (numbers[i].chars().nth(numbers[i].len()-3).unwrap()).to_digit(10).unwrap();
        if numbers[i].chars().nth(0).unwrap() == 'f' {
            if stage == 1 {
                forw += change;
            } else {
                depth += aim * change;
                forw += change;
            }
        } else if numbers[i].chars().nth(0).unwrap() == 'u' {
            if stage == 1 {
                depth -= change;
            } else {
                aim -= change;
            }
        } else if numbers[i].chars().nth(0).unwrap() == 'd' {
            if stage == 1 {
               depth += change;
            } else {
                aim += change;
            }

        }
    }

    println!("PART {}:", stage);
    println!("Position: {}, {}", forw, depth);
    println!("Product: {}", depth*forw);

    Ok(())
}
