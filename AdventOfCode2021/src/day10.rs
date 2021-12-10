// day 10 of advent of code 2021
// author: rachael judy
// date: 10 dec 2021
// read characters on the stack and match open and close of <>, {}, [], ()

use std::io::prelude::*;
use std::vec::Vec;

pub fn calculate(inp : Vec<String>, stage : i32) -> std::io::Result<()> {
    let mut scores2 : Vec<i64> = vec![0;0];
    let mut close : Vec<char> = vec!['a';0];
    for i in 0..inp.len() { // iterate through input lines
        let mut stack : Vec<char> = Vec::new(); // check each line's validity
        let line : Vec<char> = inp[i].chars().collect();
        let mut errorline = false; // for part 2 to get incomplete lines
        for el in 0..line.len() { // iterate through elements, pushing on stack
            if stack.len() != 0 &&
                (stack[stack.len()-1] == '{' && line[el] == '}' || stack[stack.len()-1] == '(' && line[el] == ')'
                || stack[stack.len()-1] == '[' && line[el] == ']' || stack[stack.len()-1] == '<' && line[el] == '>') {
                stack.pop();                        // pop element off if closure
            } else if line[el] == '[' ||  line[el] == '{' || line[el] == '(' || line[el] == '<' {
                stack.push(line[el]);         // push element on if opener
            } else {
                close.push(line[el]);         // note closure error if mismatch
                errorline = true;                   // mark error for part 2
                break;
            }
        }
        // for part 2 - if no error, score the line
        if !errorline {
            let mut s : i64 = 0;
            while stack.len() != 0 {
                s = 5*s + match stack.pop().unwrap() {'('=>1, '['=>2, '{'=>3, '<'=>4, other=>0};
            }
            scores2.push(s);
        }
    }
    // score part 1 (sum value of first error characters)
    let mut sum = close.iter().filter(|&n| *n == ')').count() * 3
                      + close.iter().filter(|&n| *n == ']').count() * 57
                      + close.iter().filter(|&n| *n == '}').count() * 1197
                      + close.iter().filter(|&n| *n == '>').count() * 25137;
    println!("Score (stage 1): {}", sum);

    // find middle score for part 2
    scores2.sort();
    println!("Score (stage 2): {}", scores2[((scores2.len()-1)/2)]);
    Ok(())
}
