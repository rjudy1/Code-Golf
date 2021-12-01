// Advent of Code 2021 Solutions
// author: Rachael Judy
// date: December 1, 2021


mod day01;

use std::io;
use std::io::prelude::*;
use std::fs::File;
use std::io::BufReader;
use std::env;
use std::vec::Vec;
use std::path::Path;

// number input - note needs to add whitespace at end of file
fn get_input_num_col(filename: &str, size:usize) ->Vec<i32> {
    let path = Path::new(filename);
    let f = match File::open(&filename) {
        Err(why) => panic!("couldn't open {}: {}", path.display(), why),
        Ok(file) => file,
    };
    // let mut f = File::open("Day01.txt")?;
    let mut reader = BufReader::new(f);
    let mut buffer : Vec<String> = vec![String::new(); size];

    for i in 0..size {
        let mut temp= String::new();
        reader.read_line(&mut temp);
        buffer[i] = temp;
    }

    let mut numbers : Vec<i32> = vec![0; size];
    for i in 0..size {
        numbers[i] = buffer[i][0..(buffer[i].len()-2)].parse::<i32>().unwrap();
    }
    return numbers
}


fn main() -> std::io::Result<()> {
    println!("Hello, world!");

    //***************
    // set these
    let day = 1;
    let stage = 1;
    // **************

    if day == 1 {
        day01::calculate(get_input_num_col("Day01.txt", 2000), stage);
    } else if day == 2 {

    } else if day == 3 {

    } else if day == 4 {

    } else if day == 5 {

    } else if day == 6 {

    }

    Ok(())
}
