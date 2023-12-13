// include the packages we need
use std::io;
use std::cmp::Ordering;
fn print(msg: &str){
    println!("{}", msg);
}
fn main() {
    //take in input
    let mut cmd = String::new();
    loop {
        
        println!("Enter a command: ");
        io::stdin().read_line(&mut cmd)
        .expect("Failed to read line\n");
    
    //parse input
    match cmd.trim(){
        // handle specific cases here
        
        "help" => {
            help();
        }
        _ => {
            println!("Invalid command\n");
        }
    }
}
}
fn help(){
    print("help - display this message");
}
