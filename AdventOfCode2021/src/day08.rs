// day 8 of advent of code 2021
// author: rachael judy
// date: 8 dec 2021
// decode the broken seven segs

use std::io::prelude::*;
use std::vec::Vec;

fn equals(a : Vec<char>, b : Vec<char>) -> bool {
    if a.len() != b.len() { return false }
    for i in 0..a.len() { if a[i]!=b[i] { return false } }
    return true
}

pub fn calculate(inp : Vec<String>, stage : i32) -> std::io::Result<()> {
    println!("Stage {}", stage);
    // iterate through all messed up seven segs, and decode each row
    let mut count_special = 0;
    let mut sum = 0;
    for i in 0..inp.len() { // iterate over every row
        let parts : Vec<&str> = (&inp[i]).split_whitespace().collect();
        let mut options:Vec<Vec<char>> = vec![vec!['a'; 0]; 10];

        // match numbers by contents
        // find the one, four, seven, eight seg
        for j in 0..parts.len()-5 {
            let mut x : Vec<char> = parts[j].chars().collect();
            x.sort();
            if parts[j].len() == 2 {options[1] = x.clone();}
            if parts[j].len() == 3 {options[7] = x.clone();}
            if parts[j].len() == 4 {options[4] = x.clone();}
            if parts[j].len() == 7 {options[8] = x.clone();}
        }

        // find the three which is the only five digit with the one
        // find the six which is the only six digit without the full one
        for j in 0..parts.len()-5 {
            let mut x : Vec<char> = parts[j].chars().collect();
            x.sort();

            if parts[j].len() == 5
                && parts[j].contains(options[1][0]) && parts[j].contains(options[1][1]) {
                options[3] = x.clone();
            }
            if parts[j].len() == 6
                && (parts[j].contains(options[1][0])  && !parts[j].contains(options[1][1])
                || !parts[j].contains(options[1][0]) && parts[j].contains(options[1][1])) {
                options[6] = x.clone();
            }
        }

        // find the nine which is three plus an additional spot
        // find the five which is the six missing one seg
        for j in 0..parts.len()-5 {
            let mut x : Vec<char> = parts[j].chars().collect();
            x.sort();

            if parts[j].len() == 6 && parts[j].contains(options[3][0])
                && parts[j].contains(options[3][1]) && parts[j].contains(options[3][2])
                && parts[j].contains(options[3][3]) && parts[j].contains(options[3][4]) {
                options[9] = x.clone();
            }
            if parts[j].len() == 5 && options[6].contains(&x[0])
                && options[6].contains(&x[1]) && options[6].contains(&x[2])
                && options[6].contains(&x[3]) && options[6].contains(&x[4]) {
                options[5] = x.clone();
            }
        }

        // match the zero and two, basically what's left of that length
        for j in 0..parts.len()-5 {
            let mut x : Vec<char> = parts[j].chars().collect();
            x.sort();

            if parts[j].len() == 6 && !equals(x.clone(), options[6].clone())
                && !equals(x.clone(), options[9].clone()) {
                options[0] = x.clone();
            }
            if parts[j].len() == 5 && !equals(x.clone(),options[3].clone())
                && !equals(x.clone(), options[5].clone()) {
                options[2] = x.clone();
            }
        }

        // result time
        for j in parts.len()-4..parts.len() {
            // stage 1 - count occurrences of 1, 4, 7, 8
            count_special += match parts[j].len() {
                2 | 3 | 4 | 7 => 1,
                _ => 0
            };

            // match each found number to its encoded form
            let mut x : Vec<char> = parts[j].chars().collect();
            x.sort();
            for k in 0..options.len() {
                if equals(options[k].clone(), x.clone()) {
                    sum += k as i32 * 10i32.pow((parts.len()-j-1) as u32);
                    break;
                }
            }
        }
    }

    println!("Specials: {}", count_special);
    println!("Sum: {}", sum);
    Ok(())
}
