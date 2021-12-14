// day 14 of advent of code 2021
// author: rachael judy
// date: 14 dec 2021
// expand polymer internally by rules

use std::io::prelude::*;
use std::vec::Vec;
use std::collections::HashMap;
use std::cmp;

// count character based on numbers of pairs
fn count(char_count : HashMap<char, i64>, pairs : HashMap<String, i64>) -> i64 {
    let mut char_count = char_count.clone();
    for (k, v) in pairs {
        *char_count.get_mut(&k.chars().nth(0).unwrap()).unwrap() += v;
        *char_count.get_mut(&k.chars().nth(1).unwrap()).unwrap() += v;
    }

    let mut min_val : i64 = 1000000000000000;
    let mut max_val : i64 = 0;
    for (k, v) in char_count {
        min_val = cmp::min(min_val, v);
        max_val = cmp::max(max_val, v);
    }
    return (max_val-min_val)/2 // double counted so divide by two at end
}

pub fn calculate(inp : Vec<String>) -> std::io::Result<()> {
    // set rules
    let mut starter : String = inp[0].clone();
    let mut rules : HashMap<String, char> = HashMap::new();
    for i in 2..inp.len() {
        let line : Vec<&str> = inp[i].split_whitespace().collect();
        rules.insert(line[0].to_string(), line[2].chars().nth(0).unwrap());
    }

    // count pairs in initial polymer and initialize char_count
    let mut pairs : HashMap<String, i64> = HashMap::new(); // combinations of letters
    let mut char_count : HashMap<char, i64> = HashMap::new();
    for (k, v) in rules.clone() {
        if starter.contains(&k) { pairs.insert(k, 1); }
        else { pairs.insert(k, 0); }
        char_count.insert(v, 0);
    }
    // set first and last count as they are the only not double counted
    char_count.insert(starter.chars().nth(0).unwrap(), 1);
    char_count.insert(starter.chars().nth(starter.len()-1).unwrap(), 1);

    // go through days
    for day in 0..40 {
        let mut new_pairs = pairs.clone(); // keep copy for end of day
        for (k, v) in pairs {
            // create key with pushing on chars
            let mut k1 = k.chars().nth(0).unwrap().to_string();
            k1.push(rules[&k].clone());
            let mut k2 = rules[&k].to_string(); // create second key
            k2.push(k.chars().nth(1).unwrap());

            // new pairs are created and the v old pairs are removed
            *new_pairs.get_mut(&k1).unwrap() += v;
            *new_pairs.get_mut(&k2).unwrap() += v;
            *new_pairs.get_mut(&k).unwrap() -= v;
        }
        pairs = new_pairs.clone();
        if day==9 { println!("Stage 1: {}", count(char_count.clone(), pairs.clone())); }
    }

    println!("Stage 2: {}", count(char_count.clone(), pairs.clone()));
    Ok(())
}