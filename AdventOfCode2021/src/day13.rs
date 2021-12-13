// day 13 of advent of code 2021
// author: rachael judy
// date: 13 dec 2021
// find display code after folds

use std::io::prelude::*;
use std::vec::Vec;

pub fn calculate(inp : Vec<String>) -> std::io::Result<()> {
    let mut instr_section = false;
    let mut coords = vec![(0, 0); 0];
    let mut instr = vec![('x', 0); 0];
    for i in 0..inp.len() {
        if inp[i].len() == 0 { instr_section=true; }
        else if !instr_section {    // coordinates here
            let split_line : Vec<&str> = inp[i].split(",").collect();
            coords.push((split_line[0].to_string().parse::<i32>().unwrap(),
                           split_line[1].to_string().parse::<i32>().unwrap()));
        } else {                    // instructions to fold here
            let split_line : Vec<&str> = inp[i].split_whitespace().collect();
            let fold : Vec<&str> = split_line[split_line.len()-1].split("=").collect();
            instr.push((fold[0].chars().nth(0).unwrap(), fold[1].to_string().parse::<i32>().unwrap()));
        }
    }

    // go through executing the folds
    for fold in instr {
        for i in 0..coords.len() {  // if coords apply, do the fold of 2*line - pos
            if fold.0 == 'x' && coords[i].0 > fold.1 { // fold is about x
                coords[i].0 = 2 * fold.1 - coords[i].0;
            } else if fold.0 == 'y' && coords[i].1 > fold.1 { // fold is about y
                coords[i].1 = 2 * fold.1 - coords[i].1;
            }
        }
        coords.sort();
        coords.dedup(); // remove duplicates
        println!("After fold, {} coordinates", coords.len());
    }

    // display final solution
    println!("\nCode: ");
    for y in 0..8 {
        for x in 0..50 {
            if coords.contains(&(x, y)) { print!("#"); }        // coord matched
            else { print!(" "); }                                  // untouched coord
        }
        println!(); // next row
    }
    Ok(())
}