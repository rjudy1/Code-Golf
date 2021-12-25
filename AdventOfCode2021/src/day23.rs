// day 23 of advent of code 2021
// author: rachael judy
// date: 23 dec 2021
// hand solve with trial and error using tool - doesn't enforce rules except border - probably np hard
// nice tool somebody posted: https://aochelper2021.blob.core.windows.net/day23/index.html

use std::io;

fn display(map : Vec<Vec<char>>) {
    println!("xy>\t0000000000111");
    println!("V\t0123456789012");
    let mut i = 0;
    for i in 0..map.len() {
        print!("{}\t", i);
        for c in &map[i] {
            print!("{}", c);
        }
        println!();
    }
}

pub fn calculate(inp : Vec<String>) -> std::io::Result<()> {
    let mut map : Vec<Vec<char>> = Vec::new();
    for line in inp.iter() {
        map.push(line.chars().collect::<Vec<char>>());
    }

    // for part 2, between the two rows, insert
    //   #D#C#B#A#
    //   #D#B#A#C#
    map.insert(3, vec![' ', ' ', '#', 'D', '#', 'C', '#', 'B', '#', 'A', '#']);
    map.insert(4, vec![' ', ' ', '#', 'D', '#', 'B', '#', 'A', '#', 'C', '#']);

    // need to sort ABCD with cost 1, 10, 100, 1000 - cannot block hallway
    let mut score = 0;
    let mut board_copy = map.clone();
    println!("Enter 'r' or 'x' at the first prompt to reset or exit, otherwise enter coords");
    display(map.clone());
    loop {
        println!("Enter letter and order (ex. A2) in reading order across board : ");
        let mut input = String::new();
        io::stdin().read_line(&mut input);
        // reset to starting position
        if input.chars().nth(0).unwrap() == 'r' {
            board_copy = map.clone();
            score = 0;
            display(map.clone());
            continue;
        } else if input.chars().nth(0).unwrap() == 'x' {
            break;
        }
        // get source coordinates
        let letter = input.chars().nth(0).unwrap();
        let count = input.chars().nth(1).unwrap().to_digit(10).unwrap();
        let mut copies = 0;
        let (mut x0, mut y0) = (0, 0);
        for i in 0..board_copy.len() {
            for j in 0..board_copy[i].len() {
                if board_copy[i][j] == letter {
                    copies += 1;
                    if copies == count {
                        x0 = i;
                        y0 = j;
                        break;
                    }
                }
            }
        }

        // get destination coordinates
        println!("Enter where to move (zero indexed). ex. 5,10 : ");
        let mut input = String::new();
        io::stdin().read_line(&mut input);
        let mut line = input.split(',').collect::<Vec<&str>>();
        let x1 = line[0].parse::<usize>().unwrap();
        line[1] = &line[1][..line[1].len()-1];
        let y1 = line[1].parse::<usize>().unwrap();
        if x1 >= board_copy.len() || y1 >= board_copy[x1].len() || board_copy[x1][y1] != '.' {continue;}
        else {
            let increase = match board_copy[x0][y0] { 'A'=>1, 'B'=>10, 'C'=>100, 'D'=>1000, _=>0 };
            score += ((x0-1) as i32 + (x1-1) as i32 +  (y1 as i32 - y0 as i32).abs()) as usize * increase;
            board_copy[x1][y1] = board_copy[x0][y0];
            board_copy[x0][y0] = '.';
        }
        display(board_copy.clone());
        println!("Score: {}", score);
    }
    display(map);
    println!("Score: {}", score);

    Ok(())
}
