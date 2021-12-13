// Advent of Code 2021 Solutions
// author: Rachael Judy
// date: December 13, 2021
// usage:   change flagged day and stage to match current day
//          add size being given to parser line
//      !!! make sure to add whitespace to last row if not a one liner csv

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
mod day08;
mod day09;
mod day10;
mod day11;
mod day12;
mod day13;
mod day14;

fn main() -> std::io::Result<()> {
    //************************************
    // set these
    let mut day = 14;
    let mut stage = 1;
    // ***********************************

    println!("Hello, world! It's day {}!", day);

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
        day07::calculate(parser::get_input_comma_sep("Day07.txt", 1000), stage);
    } else if day == 8 {
        day08::calculate(parser::get_input_cols("Day08.txt", 200), stage);
    } else if day == 9 {
        day09::calculate(parser::get_input_cols("Day09.txt", 100), stage);
    } else if day == 10 {
        day10::calculate(parser::get_input_cols("Day10.txt", 110), stage);
    } else if day == 11 {
        day11::calculate(parser::get_input_cols("Day11.txt", 10), stage);
    } else if day == 12 {
        day12::calculate(parser::get_input_cols("Day12.txt", 21));
    } else if day == 13 {
        day13::calculate(parser::get_input_cols("Day13.txt", 896));
    } else if day == 14 {
        day14::calculate(parser::get_input_cols("Day14.txt", 1000));
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
