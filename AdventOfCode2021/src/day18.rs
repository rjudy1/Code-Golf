// day 18 of advent of code 2021
// author: rachael judy
// date: 18 dec 2021
// gamble on it never being bigger than 2 digits; 1 min runtime

use std::vec::Vec;
use std::cmp;

fn reduce(pair : String) -> String {
    // explode and split internally
    let mut depth = 0;
    let mut x : &str = &pair;
    let mut result = pair.clone();
    let mut i = 0;
    while i < result.len() -1 {  // while space to check
        // check depth
        if result.chars().nth(i).unwrap() == '[' {
            depth+=1;
        } else if result.chars().nth(i).unwrap() == ']' {
            depth-=1;
        }

        // explode if we are deeper than allowed and found the number to explode on
        if depth > 4 && x[i..i+1].parse::<i32>().is_ok() && result.chars().nth(i+1).unwrap() == ',' {
            // initialize searchers outside deepest and numbers
            let mut j = i-2;
            let mut k = i+4;
            let mut num1 = x[i..i+1].parse::<i32>().unwrap();
            if x[i-1..i+1].parse::<i32>().is_ok() { num1 = x[i-1..i+1].parse::<i32>().unwrap(); }
            let mut num2 = x[i+2..i+3].parse::<i32>().unwrap();
            if x[i+2..i+4].parse::<i32>().is_ok() { num2 = x[i+2..i+4].parse::<i32>().unwrap(); }
            // find closest numbers
            while  j != 0 {
                if x[j..j+1].parse::<i32>().is_ok() { break; }
                j-=1;
            }
            while  k < result.len() {
                if x[k..k+1].parse::<i32>().is_ok() { break; }
                k+=1;
            }

            // add the back numbers
            let mut new_x = x.to_string().clone();
            if k != result.len() {
                let mut num3 = x[k..k+1].parse::<i32>().unwrap();
                if x[k..k+2].parse::<i32>().is_ok() { num3 = x[k..k+2].parse::<i32>().unwrap(); }
                new_x = (&x[..k]).to_owned();
                new_x.push_str(&(num3 + num2).to_string());
                new_x.push_str(&(&x[k+1+((num3>9) as usize)..]).to_owned());
                x = &new_x;
            }
            // add the front number
            let xstring = new_x.clone();
            x = &xstring;
            new_x = x.to_string().clone();
            if j != 0 {
                let mut num3 = x[j..j+1].parse::<i32>().unwrap();
                if x[j-1..j+1].parse::<i32>().is_ok() { num3 = x[j - 1..j + 1].parse::<i32>().unwrap(); }
                new_x = (&x[..j-((num3 > 9) as usize)]).to_owned();
                new_x.push_str(&(num3 + num1).to_string());
                new_x.push_str(&(&x[j+1..]).to_owned());
                x = &new_x;
            }

            // find edges to replace with zero
            let mut left = i;
            let mut right = i;
            while &x[left..left+1] != "[" { left-=1; }
            while &x[right..right+1] != "]" { right += 1; }
            result = x[..left].to_owned() + &"0".to_string() + &x[right+1..];
            x = &result;

            // rerun through part of array with new knowledge of depth
            i = left;
            depth -= 1;
        }
        i+=1;
    }

    // do split (has to return to checking depth if fails
    for _i in 0..x.len()-1 {
        if x[_i.._i +1].parse::<i32>().is_ok() && x[_i +1.._i +2].parse::<i32>().is_ok() { // split on >9
            let x1 = &x[_i.._i +2].parse::<i32>().unwrap() / 2;
            let x2 = &(x[_i.._i +2].parse::<i32>().unwrap() + 1) / 2;
            let mut new_x = x[.._i].to_string().clone() + &"[".to_owned() + &x1.to_string()
                + &",".to_owned() + &x2.to_string() + &"]".to_owned()+ &x[_i +2..];
            return reduce(new_x.clone())
        }
    }
    return result
}

fn sum(pair : String) -> i32 {
    let mut stack : Vec<i32> = Vec::new();
    for i in 0..pair.len() {
        if (&pair)[i..i+1].parse::<i32>().is_ok() {
            stack.push((&pair)[i..i+1].parse::<i32>().unwrap());
        } else if &(&pair)[i..i+1] == "]" {
            let x = stack.pop().unwrap();
            let y = stack.pop().unwrap();
            stack.push(2*x+3*y);
        }
    }
    return stack.pop().unwrap()
}

pub fn calculate(inp : Vec<String>) -> std::io::Result<()> {
    let mut mega : String = inp[0].clone(); // mega pair
    for i in 1..inp.len() {
        mega = "[".to_string() + &mega + &",".to_string() + &inp[i].clone() + &"]".to_string();
        mega = reduce(mega.clone()); // reduce every time pair is expanded
    }

    println!("Countdown to results...");
    let mut maxi = 0;
    for i in 0..inp.len() {
        for j in 0..inp.len() {
            if i != j {
                maxi = cmp::max(maxi, sum(reduce("[".to_string() + &inp[i].clone()
                    + &",".to_string() + &inp[j].clone() + &"]".to_string())));
            }
        }
        println!("{}", 99-i);
    }

    println!("Page sum:  {}", sum(mega.clone()));
    println!("Maximum:   {}", maxi);
    Ok(())
}
