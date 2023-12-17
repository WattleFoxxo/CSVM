// include the packages we need
use creator::{
    create_file_with_contents, create_project_dylib, create_project_executable, SuppportedLanguages,
};
use std::env;
use std::io;

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
const INVALIDINPUT: &str = r#"hmm... that input isn't supported."#;

fn main() {
    //TODO add argument support so that it skips the input

    // Get the current directory
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
        return;
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
