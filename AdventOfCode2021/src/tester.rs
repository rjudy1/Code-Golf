// day 19 of advent of code 2021
// author: rachael judy
// date: 19 dec 2021
// gamble on it never being bigger than 2 digits; should have probably flattened the tree/depth flag

use std::vec::Vec;
use std::cmp;

fn reduce_alt(pairs : &mut Vec<(i32, i32)>) {
    let mut i = 0;
    while i != pairs.len()-2 {
        if pairs[i].1 == 5 {
            if i == 0 {
                pairs[i+2].0 += pairs[i+1].1;
                pairs.insert(i, (0, pairs[i].1-1));
                pairs.remove(i+1);
                pairs.remove(i+1);
            } else if i == pairs.len()-1 {
                pairs[i-1].0 += pairs[i].0;
                pairs.insert(i, (0, pairs[i].1-1));
                pairs.remove(i+1);
                pairs.remove(i+1);
            } else {
                pairs[i-1].0 += pairs[i].0;
                pairs[i+2].0 += pairs[i+1].1;
                pairs.insert(i, (0, pairs[i].1-1));
                pairs.remove(i+1);
                pairs.remove(i+1);
            }
            i = 0;
        }
        i+=1;
    }

    for i in 0..pairs.len() {
        if pairs[i].0 > 1 {
            pairs.insert(i+1, ((pairs[0].0 + 1)/2, pairs[i].1+1));
            pairs.insert(i+1, (pairs[0].0/2, pairs[i].1+1));
            pairs.remove(i);
            reduce_alt(pairs);
            break;
        }
    }
}

fn sum(pairs : Vec<(i32, i32)>) -> i32 {
    let mut stack : Vec<i32> = Vec::new();
    for i in 0..pairs.len() {
        if pairs[i].1 == 4 {
            let x = stack.pop().unwrap();
            let y = stack.pop().unwrap();
            stack.push(x*y);
        } else {
            stack.push(pairs[i].0);
        }
    }
    return stack.pop().unwrap()
}


pub fn calculate(inp : Vec<String>) -> std::io::Result<()> {
    let mut depth = 0;
    let mut pairs : Vec<(i32, i32)> = Vec::new();
    for i in 0..inp.len() {
        for j in 0..pairs.len() {
            pairs[j].1 += 1;
        }
        for j in 0..inp[i].len() {
            depth += (&(&inp[i])[j..j+1] == "[") as i32 - (&(&inp[i])[j..j+1]=="]") as i32;
            if (&inp[i])[j..j+1].parse::<i32>().is_ok() {
                pairs.push( ((&inp)[i][j..j+1].parse::<i32>().unwrap(), depth));
            }
        }
        reduce_alt(&mut pairs);
    }
    println!("{}", sum(pairs));

    Ok(())
}


