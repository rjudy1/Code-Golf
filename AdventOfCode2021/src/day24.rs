// day 24 of advent of code 2021
// author: rachael judy
// date: 24 dec 2021
// find max and min 14 digit number (no zero digits) that outputs zero from the alu code (128s runtime)
// useful notes: repeats in 14 blocks of 18, changes only on lines 4,5,and 15, can eliminate if
//                  division causes an expansion, can store one prefix (max/min) per z instead of all

use std::cmp;
use std::collections::HashMap;

// reverse engineered the repeated blocks of code to divide, conditional multiply, cond add
fn calc_stage(w: i64, dz : i64, ax : i64, ay : i64, z : i64) -> i64 {
    z / dz * (25 * (((z % 26) + ax) != w) as i64 + 1) + (w + ay) * (((z % 26) + ax) != w) as i64
}

// tree descent to expand prefixes that work
fn search(dzs : &Vec<i64>, axs : &Vec<i64>, ays : &Vec<i64>, mut working : HashMap<i64, String>, maximize: bool) -> HashMap<i64, String> {
    let mut hasher : HashMap<i64, String> = HashMap::new();
    for d in (1..=9).rev() {
        for (z, prefix) in &working {
            // hit end of digits/aka bottom of tree to check on previous call
            if prefix.len() == 14 { return working }

            // calculate new z from previous z and digit to add, add max/min extend prefix
            // to array at z if not a divide that causes an expansion
            let new_z = calc_stage(d, dzs[prefix.len()], axs[prefix.len()], ays[prefix.len()], *z);
            if dzs[prefix.len()] == 1 || dzs[prefix.len()] == 26 && new_z < *z {
                let new_prefix = prefix.to_string() + &d.to_string();
                if !hasher.contains_key(&new_z) {
                    hasher.insert(new_z, new_prefix);
                } else {
                    if maximize {
                        hasher.insert(new_z, cmp::max(hasher[&new_z].parse::<i64>().unwrap(),
                                                      new_prefix.parse::<i64>().unwrap()).to_string());
                    } else {
                        hasher.insert(new_z, cmp::min(hasher[&new_z].parse::<i64>().unwrap(),
                                                      new_prefix.parse::<i64>().unwrap()).to_string());
                    }
                }
            }
        }
    }

//    println!("z's len: {}", hasher.len());  // if want to see incremental progress
    return search(dzs, axs, ays, hasher, maximize);
}

pub fn calculate(inp : Vec<String>) -> std::io::Result<()> {
    // lines 4, 5 and 15 have the relevant changing data
    let mut dzs = Vec::new();
    let mut axs = Vec::new();
    let mut ays = Vec::new();
    for i in 0..14 {
        let zline = &inp[18*i + 4].split_whitespace().collect::<Vec<&str>>();
        dzs.push(zline[2].parse::<i64>().unwrap());
        let xline = &inp[18*i + 5].split_whitespace().collect::<Vec<&str>>();
        axs.push(xline[2].parse::<i64>().unwrap());
        let yline = &inp[18*i + 15].split_whitespace().collect::<Vec<&str>>();
        ays.push(yline[2].parse::<i64>().unwrap());
    }

    // do search, keep max and min prefix
    let mut matches : HashMap<i64, String> = HashMap::new();
    matches.insert(0, String::new());
    println!("Maximum key: {}", search(&dzs, &axs, &ays, matches.clone(), true)[&0]);

    let mut matches : HashMap<i64, String> = HashMap::new();
    matches.insert(0, String::new());
    println!("Maximum key: {}", search(&dzs, &axs, &ays, matches.clone(), false)[&0]);
    Ok(())
}
