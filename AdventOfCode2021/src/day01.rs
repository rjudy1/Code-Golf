// day 1 of advent of code 2021
// author: rachael judy
// date: 1 dec 2021
// count occurrences of increases

use std::vec::Vec;

pub fn calculate(numbers : Vec<i32>, stage : i32) -> std::io::Result<()> {
    // set stage to 1 or 2
    let mut diff=1;
    if stage==2 {
        diff=3;
    }

    let mut count = 0;
    for i in diff..2000 {
        if numbers[i] > numbers[i-diff] {
            count+=1;
        }
    }

    println!("{}", count);

    Ok(())
}
