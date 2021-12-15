// day 11 of advent of code 2021
// author: rachael judy
// date: 11 dec 2021
// expand flashes when over 10 per step

use std::vec::Vec;

// recursive expansion of flashes
fn flash_expand( grid : &mut Vec<Vec<(u32, bool)>>, x : usize, y : usize) -> i64 {
    let mut flashes = 0;
    if  x < grid[0].len() && y < grid.len() {
        grid[x][y].0 += 1;
        // expand if greater than 9 and not already flashed
        if grid[x][y].0 > 9 && !grid[x][y].1 {
            flashes += 1; // will flash
            grid[x][y].1 = true;

            // expand if will stay in bounds
            flashes += flash_expand(grid, x + 1, y);
            flashes += flash_expand(grid, x + 1, y + 1);
            flashes += flash_expand(grid, x, y + 1);
            if x > 0 { // have to have because of usize type
                flashes += flash_expand(grid, x - 1, y + 1);
                flashes += flash_expand(grid, x - 1, y);
            }
            if y > 0 {
                flashes += flash_expand(grid, x, y - 1);
                flashes += flash_expand(grid, x + 1, y - 1);
            }
            if x > 0 && y > 0 {
                flashes += flash_expand(grid, x - 1, y - 1);
            }
        }
    }
    return flashes;
}

pub fn calculate(inp : Vec<String>, stage : i32) -> std::io::Result<()> {
    println!("Stage {}", stage);
    // each digit goes to a spot
    let mut grid: Vec<Vec<(u32, bool)>> = vec![vec![(0, false); inp[0].len()]; inp.len()];
    for i in 0..inp.len() {
        let line : Vec::<u32> = inp[i].chars().map(|c| c.to_digit(10).unwrap()).collect();
        for j in 0..inp[0].len() { grid[i][j] = (line[j], false); }
    }

    // iterate through days until day 1 and 2 conditions are met
    let mut flashes : i64 = 0;
    for day in 0..500 { // big enough to catch where all line up
        for i in 0..grid.len() { // iterate through expansions
            for j in 0..grid[0].len() {
                grid[i][j].0 +=1;
                if grid[i][j].0 > 9 { flashes += flash_expand(&mut grid, i, j); }
            }
        }
        // reset at end of steps if greater
        let mut count = 0;
        for i in 0..grid.len() {
            for j in 0..grid[0].len() {
                if grid[i][j].0 > 9 { grid[i][j].0 = 0; } // reset greater than 9
                count += grid[i][j].1 as i32;
                grid[i][j].1 = false;
            }
        }
        if day == 99 { println!("Flashes after 100 days: {}", flashes); }
        if count == (grid.len() * grid[0].len()) as i32 {
            println!("Day at all flash: {}", day +1);
            break;
        };
    }

    Ok(())
}
