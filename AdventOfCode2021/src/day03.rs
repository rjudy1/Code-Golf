// day 3 of advent of code 2021
// author: rachael judy
// date: 3 dec 2021
// count bits and find matches to the bit pattern

use std::vec::Vec;

fn count_ones_and_zeros(inp : Vec<String>) -> (Vec<i32>, Vec<i32>){
    let mut zeros : Vec<i32> = vec![0; inp[0].len()-2];// = vec![String::from('f'); size];
    let mut ones : Vec<i32> = vec![0; inp[0].len()-2];// = vec![String::from('f'); size];
    for i in 0..inp.len() {
        for j in 0..inp[i].len()-2 {
            if inp[i].chars().nth(j).unwrap() == '0' {
                zeros[j] += 1;
            } else {
                ones[j] += 1;
            }
        }
    }

    return (zeros, ones)
}


pub fn calculate(inp : Vec<String>, stage : i32) -> std::io::Result<()> {
    // stage one is simply storing greater and less in epsilon and gamma
    if stage == 1 {
        let (zeros, ones) = count_ones_and_zeros(inp);
        let mut gamma = String::new();
        let mut epsilon = String::new();

        for k in 0..zeros.len() {
            if zeros[k] >= ones[k] {
                gamma.push('0');
                epsilon.push('1');
            } else {
                gamma.push('1');
                epsilon.push('0');
            }
        }
        let gammaint = isize::from_str_radix(&gamma, 2).unwrap();
        let epsilonint = isize::from_str_radix(&epsilon, 2).unwrap();

        println!("gamma, epsilon, {}, {}", gammaint, epsilonint);
        println!("product: {}", gammaint * epsilonint);

    } else {
        // arrays will come down to only element that matches
        let mut oxyinter: Vec<String> = inp.clone();
        let mut co2inter: Vec<String> = inp.clone();

        // index through bits
        let mut ok = 0;
        let mut ck = 0;
        // continue until only one match
        while oxyinter.len() != 1 {
            let (zeros, ones) = count_ones_and_zeros(oxyinter.clone());
            let mut i = 0;
            while i < oxyinter.len() {
                if ones[ok] >= zeros[ok] && oxyinter[i].chars().nth(ok).unwrap() != '1'
                    ||  ones[ok] < zeros[ok] && oxyinter[i].chars().nth(ok).unwrap() != '0'{
                    oxyinter.remove(i);
                } else { i += 1; }
            }
            ok += 1;
        }
        oxyinter[0].pop();
        oxyinter[0].pop();

        while co2inter.len() != 1 {
            let (zeros, ones) = count_ones_and_zeros(co2inter.clone());
            let mut i = 0;
            while i < co2inter.len() {
                if ones[ck] >= zeros[ck] && co2inter[i].chars().nth(ck).unwrap() != '0'
                    || ones[ck] < zeros[ck] && co2inter[i].chars().nth(ck).unwrap() != '1' {
                    co2inter.remove(i);
                } else { i+=1 }
            }
            ck += 1;
        }

        co2inter[0].pop();
        co2inter[0].pop();

        let oxy = isize::from_str_radix(&oxyinter[0], 2).unwrap();
        let co2 = isize::from_str_radix(&co2inter[0], 2).unwrap();

        println!("oxy, co2: {}, {}", oxy, co2);
        println!("product: {}", oxy * co2);
    }
    Ok(())
}
