// day 4 of advent of code 2021
// author: rachael judy
// date: 4 dec 2021
// play bingo

use std::io::prelude::*;
use std::vec::Vec;

fn score_board(boards : Vec<Vec<Vec<i32>>>, num : usize) -> i32 {
    let mut sum = 0;
    for j in 0..5 {
        for k in 0..5 {
            if boards[num][j][k] != -1 {
                sum += boards[num][j][k];
            }
        }
    }
    return sum
}

fn check_win_2(boards : Vec<Vec<Vec<i32>>>) -> (Vec<usize>) {
    let mut winners: Vec<usize> = vec![0; 0];
    let mut sum1 = 0;
    let mut sum2 = 0;

    for i in 0..boards.len() {
        for j in 0..5 {
            sum1 = 0;
            sum2 = 0;
            for k in 0..5 {
                sum1 += boards[i][k][j];
                sum2 += boards[i][j][k];
            }
            if sum1 == -5 || sum2 == -5 {
                if !winners.contains(&i) {
                    winners.push(i);
                }

            }
        }
    }
    return winners
}

pub fn calculate(inp : Vec<String>, stage : i32) -> std::io::Result<()> {
    println!("Stage {}", stage);
    // array of comma separated inputs
    let mut inp0 : Vec<&str> = (&inp[0]).split(',').collect();
    let mut num_sel : Vec<i32> = vec![0; 100];

    // drop the /r/n
    let mut temp = inp0[inp0.len()-1];
    temp = &temp[0..temp.len()-2];
    let t = inp0.len();
    inp0[t-1] = temp;

    // convert to ints
    for i in 0..inp0.len() {
        num_sel[i] = inp0[i].parse::<i32>().unwrap();
    }

    let mut boards = vec![vec![vec![0; 5]; 5]; 100];
    let mut board_num = 0;

    // set up board array
    for row in 2..inp.len() {
        let mut row_nums : Vec<&str> = inp[row].split_whitespace().collect();
        if row_nums.len() == 0 {//on blank line, start new board
            board_num+=1;
            continue;
        }
        for i in 0..5 {
            boards[board_num][(row-2)%6][i] = row_nums[i].parse::<i32>().unwrap();
        }
    }

    let mut loser = 200;
    for number in num_sel {
        // mark the boards
        for i in 0..boards.len() {
            for j in 0..5 {
                for k in 0..5 {
                    if boards[i][j][k] == number {
                        boards[i][j][k] = -1;
                    }
                }
            }
        }

        // different win checks
        if stage == 1 {
            let num = check_win_2(boards.clone());
            if num.len()==1 {
                // for num in 0..nums {
                let mut sum = score_board(boards, num[0]);
                println!("{} wins; score: {}", num[0], sum * number);
                break;
            }

        // stage 2
        } else {
            let wins = check_win_2(boards.clone());
            for i in 0..wins.len() {
                if wins[i] == loser { // loser set when only one remains to finish
                    let mut sum = score_board(boards.clone(), i);
                    println!("{} wins; score: {}", loser, number * sum);
                    return Ok(())
                }
                if wins.len() == boards.len()-1 {
                    for i in 0..boards.len() {
                        if !wins.contains(&i) {loser=i;}
                    }
                }
            }
        }
    }
    Ok(())
}
