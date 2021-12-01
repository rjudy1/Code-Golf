// advent of code 2021 rust parser
// author: rachael judy
// date: 12/1/2021

use std::io::BufReader;
use std::path::Path;
use std::fs::File;
use std::io::prelude::*;

// number input - note needs to add whitespace at end of file
pub fn get_input_num_col(filename: &str, size:usize) ->Vec<i32> {
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

// number input - note needs to add whitespace at end of file
pub fn get_input_comma_sep(filename: &str, size:usize) ->Vec<i32> {
    let path = Path::new(filename);
    let f = match File::open(&filename) {
        Err(why) => panic!("couldn't open {}: {}", path.display(), why),
        Ok(file) => file,
    };
    // let mut f = File::open("Day01.txt")?;
    let mut reader = BufReader::new(f);
    // let mut buffer : Vec<String> = vec![String::new(); size];

    let mut temp= String::new();
    reader.read_line(&mut temp);

    let v: Vec<&str> = temp.split(',').collect();

    let mut numbers : Vec<i32> = vec![0; v.len()];
    for i in 0..v.len() {
        numbers[i] = v[i].parse::<i32>().unwrap();
    }
    return numbers
}