// day 21 of advent of code 2021
// author: rachael judy
// date: 21 dec 2021
// deterministic dice and probabilistic functions

use std::cmp;

// for the deterministic 100 sided dice
fn next_roll(roll : &mut usize) -> usize {
    if *roll < 100 { *roll += 1; } else { *roll = 1; }
    *roll
}

// part 2's scoring
fn count_wins(seed : usize) -> Vec<Vec<u64>> {
    // probability of any single sum occurring with the three die - independent of position
    const PROBABILITY : [(usize, usize); 7] = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)];
    // index with [step][score][board position] = count at that position -> initial has 1 at seed
    let mut score : Vec<Vec<Vec<u64>>> = vec![vec![vec![0; 10]; 22]; 12];
    score[0][0][seed] = 1;
    // do 11 steps of shifting and multiplying prob - sufficient for getting all poss to 21
    for step in 1..score.len() {
        for s in 0..21 { // s = score being used to update future - keep only the new values for 21
            for pos in 0..10 { // position the numbers are at within score
                for (ad, freq) in PROBABILITY {
                    score[step][if s+1+(pos+ad)%10 < 21 { s+1+(pos+ad)%10 } else {21}][(pos+ad)%10]
                        += score[step-1][s][pos] * freq as u64;
                }
            }
        }
    }

    // consolidate to 21 and !21 for ease of use later
    let mut result = vec![vec![0; 22]; 11];
    for step in 0..result.len() {
        for s in 0..score[step].len() { result[step][s] += score[step][s].iter().sum::<u64>(); }
        result[step][0] = result[step].iter().sum::<u64>() - result[step][21];
        result[step][1] = result[step][21];
    }
    result
}

pub fn calculate(inp : Vec<String>) -> std::io::Result<()> {
    let mut players : Vec<usize> = Vec::new();
    players.push(inp[0].split_whitespace().collect::<Vec<&str>>()[4].parse::<usize>().unwrap() -1);
    players.push(inp[1].split_whitespace().collect::<Vec<&str>>()[4].parse::<usize>().unwrap() -1);

    let mut positions = players.clone();
    let mut scores : Vec<usize> = vec![0;2];
    let (mut roll, mut count) = (0, 0);
    while scores[0] < 1000 && scores[1] < 1000 {
        positions[count % 2] = (positions[count % 2] + next_roll(&mut roll) + next_roll(&mut roll) + next_roll(&mut roll)) % 10;
        scores[count % 2] += (positions[(count) % 2] + 1);
        count += 3;
    }
    println!("part 1 (losing score * rolls): {}", cmp::min(scores[0], scores[1]) * count);

    let p1_scores = count_wins(players[0]);
    let p2_scores = count_wins(players[1]);
    let mut wins = vec![0; 2];
    for i in 1..p1_scores.len() { // compare to same index for p1
        wins[0] += &p1_scores[i][1] * &p2_scores[i-1][0];
        wins[1] += &p2_scores[i][1] * &p1_scores[i][0];
    }
    println!("part 2 (dirac die wins ad infinitum): {}", cmp::max(wins[0], wins[1]));

    Ok(())
}
