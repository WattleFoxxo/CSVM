// include the packages we need
use creator::{
    create_file_with_contents, create_project_dylib, create_project_executable, SuppportedLanguages,
};
use std::array;
use std::env;
use std::io;
use std::panic;
use log;
use std::env::args;
mod window;
mod other;




/* error messages */
const INVALIDLANGUAGE: &str = r#"hmm... that language isn't supported.
did you spell it correctly or is it not supported?
if you think it should be supported, please open an issue on github.

supported languages:
"#;

const INVALIDPROJECTTYPE: &str = r#"hmm... that project type isn't supported.
did you spell it correctly or is it not supported?
if you think it should be supported, please open an issue on github.

supported project types:
"#;
const INVALIDINPUT: &str = r#"hmm... seems like whatever you put in, i couldn't understand. i guess try again? "#;

fn main() {
    let args = env::args().collect::<Vec<String>>(); // Collect command line arguments into a vector

    if args.len() > 1 {
        // Execute the block of code if there are command line arguments
        let mut array = Vec::new(); // Declare arrayforargs as a vector
        for arg in args.iter().skip(1) {
            // Process each command line argument here
            println!("Command line argument: {}", arg);
            array.push(arg.to_string()); // Use push method to add elements to the vector
        }
        if array.len() >= 4 {
            if array[0] == "create" {
                let name = String::from(&array[1]);
                let lang = String::from(&array[2]);
                let path = String::from(&array[3]);
                create_project_executable(&lang, &name, &path);
            }
        }
    } else {
        // Execute the rest of the code if there are no command line arguments
        let current_dir = env::current_dir().expect("Failed to get current directory");

    //take in input
    //what type of project does the user want to make?
    for language in SuppportedLanguages::enumerate() {
        println!("{}", language);
    }
    println!("Enter the language you want to use: ");
    let mut lang = String::new();
    io::stdin().read_line(&mut lang).expect(&INVALIDINPUT);
    //check if the language is supported
    if !SuppportedLanguages::enumerate().contains(&lang.trim().to_string()) {
        // trim removes the newline character, which is needed for the contains function
        println!("{}", INVALIDLANGUAGE); // print error message
        for language in SuppportedLanguages::enumerate() {
            println!("{}", language);
        }
        log::error!("CUSP 000015"); // log the error
        panic!("CUSP 000015"); // exit the program
    }
    // whats the name of the project?
    println!("Enter the name of the project: ");
    let mut name = String::new();
    io::stdin().read_line(&mut name).expect(&INVALIDINPUT);

    //does the user want it to be a dll or an executable?

    // Use the current directory instead of asking for the path
    let binding = current_dir;
    let path = &binding.to_str().expect("Failed to convert path to string");

    create_project_executable(&lang.trim(), &name.trim(), &path);
}
}
