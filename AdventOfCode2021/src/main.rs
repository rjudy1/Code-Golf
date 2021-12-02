// Advent of Code 2021 Solutions
// author: Rachael Judy
// date: December 1, 2021
// usage: change flagged day and stage to match current day; add whitespace to end of columns

use std::env;
use std::io;
use std::io::prelude::*;
use std::vec::Vec;

mod parser;
mod day01;
mod day02;
mod day03;

fn main() -> std::io::Result<()> {
    println!("Hello, world!");

    //************************************
    // set these
    let mut day = 3;
    let mut stage = 1;
    // ***********************************


    let args: Vec<String> = env::args().collect();
    if args.len() == 3 {
        day = args[1].parse::<i32>().unwrap();
        stage = args[2].parse::<i32>().unwrap();
    }

    if day == 1 {
        day01::calculate(parser::get_input_num_col("Day01.txt", 2000), stage);
    } else if day == 2 {
        day02::calculate(parser::get_input_string_col("Day02.txt", 1000), stage);
    } else if day == 3 {
        day03::calculate(parser::get_input_comma_sep("Day03.txt", 1000), stage);
    } else if day == 4 {

    } else if day == 5 {

    } else if day == 6 {

    } else if day == 7 {

    } else if day == 8 {

    } else if day == 9 {

    } else if day == 10 {

    } else if day == 11 {

    } else if day == 12 {

    } else if day == 13 {

    } else if day == 14 {

    } else if day == 15 {

    } else if day == 16 {

    } else if day == 17 {

    } else if day == 18 {

    }

    Ok(())
}
