// day 25 of advent of code 2021
// author: rachael judy
// date: 25 dec 2021
// east-moving wraparound followed by south-moving wraparound until no moves

pub fn calculate(inp : Vec<String>) -> std::io::Result<()> {
    let mut map : Vec<Vec<char>> = Vec::new();
    for line in inp {
        map.push(line.chars().collect::<Vec<char>>());
    }

    for step in 1..1000 {
        // east moves - check if open
        let mut east_moves = 0;
        let mut east_mmap = map.clone();
        for x in 0..map.len() {
            for y in 0..map[0].len() {
                if map[x][y] == '>' && map[x][(y+1) % map[0].len()] == '.' {// && y == map[0].len()-1 && map[x][0] == '.' {
                    east_mmap[x][(y+1) % map[0].len()] = map[x][y];
                    east_mmap[x][y] = '.';
                    east_moves+=1;
                }
            }
        }

        // south moves - moves after east
        let mut south_moves = 0;
        let mut new_map2 = east_mmap.clone();
        for x in 0..east_mmap.len() {
            for y in 0..east_mmap[0].len() {
                if east_mmap[x][y] == 'v' && east_mmap[(x+1) % east_mmap.len()][y] == '.' {
                        new_map2[(x+1) % east_mmap.len()][y] = east_mmap[x][y];
                        new_map2[x][y] = '.';
                        south_moves+=1;
                }
            }
        }

        // copy map for next round/check end of movement
        map = new_map2.clone();
        if south_moves + east_moves == 0 {
            println!("On step {}, there are no moves available", step);
            break;
        }
    }
    Ok(())
}
