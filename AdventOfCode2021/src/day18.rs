// day 18 of advent of code 2021
// author: rachael judy
// date: 18 dec 2021
// two versions - short tree flatten and long string parse
// gamble on it never being bigger than 2 digits; 1 min runtime for string parse

use std::vec::Vec;
use std::cmp;

fn reduce_alt(pairs : &mut Vec<(i32, i32)>) {
    // explode
    let mut i = 0;
    while i < pairs.len()-1 {
        if pairs[i].1 == 5 {
            if i == 0 { // first pair
                pairs[i+2].0 += pairs[i+1].0;
            } else if i == pairs.len()-2 { // last pair
                pairs[i-1].0 += pairs[i].0;
            } else { // all other pairs
                pairs[i-1].0 += pairs[i].0;
                pairs[i+2].0 += pairs[i+1].0;
            }
            // replace pair
            pairs.insert(i, (0, pairs[i].1-1));
            pairs.remove(i+1);
            pairs.remove(i+1);
        }
        i+=1;
    }
    // split
    for i in 0..pairs.len() {
        if pairs[i].0 > 9 {
            pairs.insert(i+1, ((pairs[i].0 + 1)/2, pairs[i].1+1));
            pairs.insert(i+1, (pairs[i].0 / 2, pairs[i].1+1));
            pairs.remove(i);
            reduce_alt(pairs);  // recursive repeat of explosion checking
            break;
        }
    }
}

fn insert_pair(pairs : &mut Vec<(i32, i32)>, line : String, drop : i32) {
    let mut depth = 1+drop;
    for j in 0..line.len() {
        depth += (&(&line)[j..j + 1] == "[") as i32 - (&(&line)[j..j + 1] == "]") as i32;
        if (&line)[j..j + 1].parse::<i32>().is_ok() {
            pairs.push((line[j..j + 1].parse::<i32>().unwrap(), depth));
        }
    }
}

// find magnitude of the pairs
fn sum_clean(stack : &mut Vec<(i32, i32)>) -> i32 {
    let mut depth = 4;
    while depth != 0 {
        let mut i = 0;
        while i < stack.len() {
            if stack[i].1 == depth {
                let x = stack.remove(i);
                let y = stack.remove(i);
                stack.insert(i, (3*x.0 + 2*y.0, x.1-1));
                i = if i > 0 {i-1} else {0};
            }
            i+=1;
        }
        depth -= 1;
    }
    return stack.pop().unwrap().0  // return magnitude
}

pub fn calculate_clean(inp : Vec<String>) -> std::io::Result<()> {
    // initialize array for mega
    let mut pairs : Vec<(i32, i32)> = Vec::new(); // expand main pairs for first part
    insert_pair(&mut pairs, inp[0].clone(), -1);
    for i in 1..inp.len() {
        // increase current depth
        for j in 0..pairs.len() {
            pairs[j].1 += 1;
        }
        // add next set of deeper values
        insert_pair(& mut pairs, inp[i].clone(), 0);
        reduce_alt(&mut pairs);
    }
    println!("sum: {}", sum_clean(&mut pairs));

    let mut maxi = 0;
    for i in 0..inp.len() {
        for k in 0..inp.len() {
            let mut pairs : Vec<(i32, i32)> = Vec::new();
            if i != k {
                insert_pair(& mut pairs, inp[i].clone(), 0);
                insert_pair(& mut pairs, inp[k].clone(), 0);
                reduce_alt(&mut pairs);
                maxi = cmp::max(maxi, sum_clean(&mut pairs));
            }
        }
    }
    println!("max: {}", maxi);
    Ok(())
}

//// ---------------------------------------------------------------------//////
//// end actual clean solution
//// ---------------------------------------------------------------------//////

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
    // smart way
    calculate_clean(inp.clone());

    let mut mega : String = inp[0].clone(); // mega pair
    for i in 1..inp.len() {
        mega = "[".to_string() + &mega + &",".to_string() + &inp[i].clone() + &"]".to_string();
        mega = reduce(mega.clone()); // reduce every time pair is expanded
    }

    println!("Countdown to slow but same results...");
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
