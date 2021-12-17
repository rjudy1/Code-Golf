// day 17 of advent of code 2021
// author: rachael judy
// date: 17 dec 2021
// parabola trajectory with drag (brute force) - ASSUMING general input is to the right and down

use std::vec::Vec;
use std::cmp;

pub fn calculate(inp : Vec<String>) -> std::io::Result<()> {
    // target area: x=175..227, y=-134..-79 - down to the right on std coordinate sys
    let line : Vec<&str> = inp[0].split_whitespace().collect();
    let xs : Vec<&str> = line[2].split('=').collect::<Vec<&str>>()[1].split('.').collect();
    let (x1, x2) = (xs[0].to_string().parse::<i32>().unwrap(), xs[2][..xs[2].len()-1].to_string().parse::<i32>().unwrap());
    let ys : Vec<&str> = line[3].split('=').collect::<Vec<&str>>()[1].split('.').collect();
    let (y1, y2) = (ys[0].to_string().parse::<i32>().unwrap(), ys[2].to_string().parse::<i32>().unwrap());

    let mut maxy = 0;       // overall max height
    let mut count = 0;      // count of shots that work
    // iterate over combinations of x from the minimum possible to reach to largest to not overshoot
    for i in ((cmp::min(x1, x2)*2) as f64).sqrt() as i32 - 1..cmp::max(x1, x2)+1 {
        // iterate over shooting down at the target to shooting up and falling past
        for j in cmp::min(y1, y2)-1..cmp::max(y1.abs(), y2.abs())+1 {
            let (mut x, mut y, mut temp_max) = (0, 0, 0);
            let (mut vx, mut vy) = (i, j);
            for _k in 0..400 { // try some steps
                x += vx; // move x
                y += vy; // move y
                vx -= match vx {0=>0, _=>(vx)/(vx.abs())}; // drag (sign matters)
                vy -= 1; // gravity
                temp_max = cmp::max(temp_max, y); // max height of this shot
                if x <= x2 && x >= x1 && y >= y1 && y <= y2 {   // hit
                    maxy = cmp::max(maxy, temp_max);
                    count +=1;
                    break;
                } else if x > x2 || y < y1 {break;}     // stepped out of range
            }
        }
    }
    println!("Max y:\t\t\t{}\nTrajectories:\t{}", maxy, count);
    Ok(())
}
