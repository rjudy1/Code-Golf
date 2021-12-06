// Advent of Code 2021 Solutions
// author: Rachael Judy
// date: December 1, 2021
// usage: change flagged day and stage to match current day; add whitespace to end of columns;
//          add size being given to parser

use std::env;
use std::io;
use std::io::prelude::*;
use std::vec::Vec;

mod parser;
mod day01;
mod day02;
mod day03;
mod day04;
mod day05;
mod day06;
mod day07;

fn main() -> std::io::Result<()> {
    println!("Hello, world!");

    //************************************
    // set these
    let mut day = 7;
    let mut stage = 1;
    // ***********************************

    let args: Vec<String> = env::args().collect();
    if args.len() == 4 {
        day = args[1].parse::<i32>().unwrap();
        stage = args[2].parse::<i32>().unwrap();
    }

    if day == 1 {
        day01::calculate(parser::get_input_num_col("Day01.txt", 2000), stage);
    } else if day == 2 {
        day02::calculate(parser::get_input_string_col("Day02.txt", 1000), stage);
    } else if day == 3 {
        day03::calculate(parser::get_input_string_col("Day03.txt", 1000), stage);
    } else if day == 4 {
        day04::calculate(parser::get_input_string_col("Day04.txt", 601), stage);
    } else if day == 5 {
        day05::calculate(parser::get_input_cols("Day05.txt", 500), stage);
    } else if day == 6 {
        day06::calculate(parser::get_input_comma_sep("Day06.txt", 1000), stage);
    } else if day == 7 {
        day07::calculate(parser::get_input_cols("Day07.txt", 1000), stage);
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

    } else if day == 19 {

    } else if day == 20 {

    } else if day == 21 {

    } else if day == 22 {

    } else if day == 23 {

    } else if day == 24 {

    } else if day == 25 {

    }

    Ok(())
}
