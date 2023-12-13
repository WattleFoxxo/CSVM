// include the packages we need
use std::io;


mod header;

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
    header::print("help - display this message");
}

fn createprojectdll(){

    //create a new dll project for CSharp



}
