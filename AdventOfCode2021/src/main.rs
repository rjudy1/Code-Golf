// Advent of Code 2021 Solutions
// author: Rachael Judy
// date: December 15, 2021
// usage:   change flagged day and stage to match current day
//          add size being given to parser line
//      !!! make sure to add whitespace to last row if not a one liner csv

use std::env;
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
mod day15;
mod day16;
mod day17;
mod day18;
mod day19;
mod day20;
mod day21;
mod day22;
mod day23;
mod day24;
mod day25;
mod tester;

fn main() -> std::io::Result<()> {
    //************************************
    // set these
    let mut day = 24;
    let mut stage = 1;
    // ***********************************

    println!("Hello, world! It's day {}!", day);

    let args: Vec<String> = env::args().collect();
    if args.len() == 4 {
        day = args[1].parse::<i32>().unwrap();
        stage = args[2].parse::<i32>().unwrap();
    }

    let mut r: std::io::Result<()> = Ok(());
    if day==0 {
        r = day10::calculate(parser::get_input_cols("test_input.txt", 2000));
    }else if day == 1 {
        r = day01::calculate(parser::get_input_num_col("Day01.txt", 2000), stage);
    } else if day == 2 {
        r = day02::calculate(parser::get_input_string_col("Day02.txt", 1000), stage);
    } else if day == 3 {
        r = day03::calculate(parser::get_input_string_col("Day03.txt", 1000), stage);
    } else if day == 4 {
        r = day04::calculate(parser::get_input_string_col("Day04.txt", 601), stage);
    } else if day == 5 {
        r = day05::calculate(parser::get_input_cols("Day05.txt", 500), stage);
    } else if day == 6 {
        r = day06::calculate(parser::get_input_comma_sep("Day06.txt"), stage);
    } else if day == 7 {
        r = day07::calculate(parser::get_input_comma_sep("Day07.txt"), stage);
    } else if day == 8 {
        r = day08::calculate(parser::get_input_cols("Day08.txt", 200), stage);
    } else if day == 9 {
        r = day09::calculate(parser::get_input_cols("Day09.txt", 100));
    } else if day == 10 {
        r = day10::calculate(parser::get_input_cols("Day10.txt", 110));
    } else if day == 11 {
        r = day11::calculate(parser::get_input_cols("Day11.txt", 10), stage);
    } else if day == 12 {
        r = day12::calculate(parser::get_input_cols("Day12.txt", 21));
    } else if day == 13 {
        r = day13::calculate(parser::get_input_cols("Day13.txt", 896));
    } else if day == 14 {
        r = day14::calculate(parser::get_input_cols("Day14.txt", 102));
    } else if day == 15 {
        r = day15::calculate(parser::get_input_cols("Day15.txt", 100), stage);
    } else if day == 16 {
        r = day16::calculate(parser::get_input_cols("Day16.txt", 1));
    } else if day == 17 {
        r = day17::calculate(parser::get_input_cols("Day17.txt", 1));
    } else if day == 18 {
        r = day18::calculate(parser::get_input_cols("Day18.txt", 100));
    } else if day == 19 {
        r = day19::calculate(parser::get_input_cols("Day19.txt", 868));
    } else if day == 20 {
        r = day20::calculate(parser::get_input_cols("Day20.txt", 102));
    } else if day == 21 {
        r = day21::calculate(parser::get_input_cols("Day21.txt", 2));
    } else if day == 22 {
        r = day22::calculate(parser::get_input_cols("Day22.txt", 420));
    } else if day == 23 {
        r = day23::calculate(parser::get_input_cols("Day23.txt", 5));
    } else if day == 24 {
        r = day24::calculate(parser::get_input_cols("Day24.txt", 100));
    } else if day == 25 {
        r = day25::calculate(parser::get_input_cols("Day25.txt", 100));
    }

    // tester
    r = tester::calculate(parser::get_input_cols("test_input.txt", 100));

    match r {
        Ok(()) => print!(""),
        Err(..) => print!("Run failed")
    }

    Ok(())
}
