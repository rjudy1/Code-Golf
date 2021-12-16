// day 16 of advent of code 2021
// author: rachael judy
// date: 16 dec 2021
// parse nested packets

use std::vec::Vec;
use std::cmp;

struct Packet {
    version : i32,
    type_id : i32,
    literal : i64,
    packets : Vec<Packet>
}

// returns the packet and next index to look at of the packet parsed
fn break_packet(s : &str) -> (Packet, usize) {
    let mut p : Packet = Packet {
        version : i32::from_str_radix(&s[0..3], 2).unwrap(),
        type_id : i32::from_str_radix(&s[3..6], 2).unwrap(),
        literal : 0,
        packets: Vec::new()
    };

    return if p.type_id == 4 {  // packet literal
        let mut bin = String::new();
        let mut index = 7;
        loop {
            bin.push_str(&s[index..index + 4]);
            index += 5;
            if &s[index - 6..index - 5] == "0" { break; }
        }
        p.literal = i64::from_str_radix(&bin, 2).unwrap();
        (p, index - 1)
    } else {                  // operator packet
        if &s[6..7] == "0" {        // type is of sum of packets inside
            let mut sum: usize = 0;
            let length = i32::from_str_radix(&s[7..22], 2).unwrap();
            while sum < length as usize {   // continue adding packets to vec until limit given
                let (pack, s) = break_packet(&s[22 + sum..]);
                sum += s;
                p.packets.push(pack);
            }
            (p, sum + 22)
        } else {                    // length type id is one so contains count of packets inside
            let count = i32::from_str_radix(&s[7..18], 2).unwrap();
            let mut pos = 18;
            for _i in 0..count {    // add packets up to count packets
                let (pack, p1) = break_packet(&s[pos..]);
                pos += p1;
                p.packets.push(pack);
            }
            (p, pos)
        }
    }
}

// sum up all the version numbers in place
fn sum_versions(p : &Packet, total : &mut i32) {
    for x in &p.packets {
        *total += x.version;
        sum_versions(x, total);
    }
}

// compute result of each operator packet
fn resolve_packet(p : &Packet) -> i64 {
    let mut answer = 0;
    if p.type_id == 0 {         // sum
        for x in &p.packets { answer += resolve_packet(x); }
    } else if p.type_id == 1 {  // product
        answer = 1; // prep for product
        for x in &p.packets { answer *= resolve_packet(x); }
    } else if p.type_id == 2 {  // min
        answer = 10000000000; // prep to find min
        for x in &p.packets { answer = cmp::min(answer, resolve_packet(x)); }
    } else if p.type_id == 3 {  // max
        for x in &p.packets { answer = cmp::max(answer, resolve_packet(x)); }
    } else if p.type_id == 4 {  // literal
        answer = p.literal;
    } else if p.type_id == 5 {  // greater than
        answer = (resolve_packet(&p.packets[0]) > resolve_packet(&p.packets[1])) as i64;
    } else if p.type_id == 6 {  // less than
        answer = (resolve_packet(&p.packets[0]) < resolve_packet(&p.packets[1])) as i64;
    } else if p.type_id == 7 {  // equal to
        answer = (resolve_packet(&p.packets[0]) == resolve_packet(&p.packets[1])) as i64;
    }
    answer
}

// convert to binary string
fn hex_to_bin_s(s : String) -> String {
    let mut b = String::new();
    for x in s.chars().collect::<Vec<char>>() {
        b.push_str(match x {
            '0'=>"0000", '1'=>"0001", '2'=>"0010", '3'=>"0011", '4'=>"0100", '5'=>"0101",
            '6'=>"0110", '7'=>"0111", '8'=>"1000", '9'=>"1001", 'A'=>"1010", 'B'=>"1011",
            'C'=>"1100", 'D'=>"1101", 'E'=>"1110", 'F'=>"1111", _=>"0000"
        });
    }
    return b
}

pub fn calculate(inp : Vec<String>) -> std::io::Result<()> {
    let message = hex_to_bin_s(inp[0].clone());
    let (top_level, _size) = break_packet(&message);

    // part 1
    let mut sum = top_level.version;
    sum_versions(&top_level, &mut sum);
    println!("Stage 1: version sum  = {}", sum);

    // part 2 - use the operands
    println!("Stage 2: packet val   = {}", resolve_packet(&top_level));

    Ok(())
}
