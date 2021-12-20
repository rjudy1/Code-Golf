// day 20 of advent of code 2021
// author: rachael judy
// date: 20 dec 2021
// map of pixels enhanced by key (note flash possible with infinite so infinite on odds)

fn enhance(map : &Vec<Vec<usize>>, key : & Vec<usize>, iter : i32) -> Vec<Vec<usize>> {
    let mut output : Vec<Vec<usize>> = map.clone();
    for k in 0..iter {
        // add border round of 2
        let mut expanded_map = output.clone();
        for i in 0..2 {
            for j in i..output.len()+i {
                expanded_map[j].insert(0, if k%2==1 {key[0]} else {0});
                expanded_map[j].push(if k%2==1 {key[0]} else {0});
            }
            expanded_map.insert(0, vec![if k%2==1 {key[0]} else {0}; output[0].len() + 4]);
            expanded_map.push(vec![if k%2==1 {key[0]} else {0}; output[0].len() + 4]);
        }

        // enhance
        output = vec![Vec::new(); expanded_map.len()-2];
        for i in 1..expanded_map.len() - 1 {
            for j in 1..expanded_map[0].len() - 1 {
                let index = expanded_map[i-1][j-1]*256 + expanded_map[i-1][j]*128 + expanded_map[i-1][j+1]*64
                          + expanded_map[i][j-1]*32 + expanded_map[i][j]*16 + expanded_map[i][j+1]*8
                          + expanded_map[i+1][j-1]*4 + expanded_map[i+1][j]*2 + expanded_map[i+1][j+1];
                output[i-1].push(key[index]);
            }
        }
    }
    output
}

fn count(enh : Vec<Vec<usize>>) -> usize {
    let mut count = 0;
    for x in enh { count += x.iter().sum::<usize>(); }
    count
}

pub fn calculate(inp : Vec<String>) -> std::io::Result<()> {
    // get key and map
    let mut key: Vec<usize> = Vec::new();
    for i in inp[0].chars().collect::<Vec<char>>() {key.push(match i {'#'=>1, _=>0}); }
    let mut map : Vec<Vec<usize>> = vec![vec![0;0]; inp.len()-2];
    for i in 2..inp.len() {
        for c in inp[i].chars().collect::<Vec<char>>() {
            map[i-2].push(match c { '#'=>1, _=>0});
        }
    }

    // enhance x number of times
    println!("Lights after 2 days: {}", count(enhance(&map, &key, 2)));
    println!("Lights after 50 days: {}", count(enhance(&map, &key, 50)));
    Ok(())
}
