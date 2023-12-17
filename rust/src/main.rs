use std::*;
use slint::*;
use lib::*;
use std::path::PathBuf;
use std::io;
use std::io::Write;
use std::env;
use std::fs;
use std::fs::File;
mod lib;
mod window;


const SUPPORTEDLANGUAGES: [&str; 4] = ["rust", "CSharp", "C", "C++"];

/* error messages */
const INVALIDLANGUAGE: &str =
    r#"hmm... that language isn't supported.
did you spell it correctly or is it not supported?
if you think it should be supported, please open an issue on github.

supported languages:
"#;

const INVALIDPROJECTTYPE: &str =
    r#"hmm... that project type isn't supported.
did you spell it correctly or is it not supported?
if you think it should be supported, please open an issue on github.

supported project types:
"#;
const INVALIDINPUT: &str = r#"hmm... that input isn't supported."#;

//TODO add error messages for when the program does something wrong.
fn get_current_dir() -> PathBuf {
    env::current_dir().expect("Failed to get current directory")
}

pub fn main() {
    // if there is an argument, use that as the import, if nothin let the user run it as a normal program
    if env::args().len() > 1 {
        let args: Vec<String> = env::args().collect();
        let lang: &str = &args[1];
        let name: &str = &args[2];
        let path: &str = &args[3];
        let project_type: &str = &args[4];
        if project_type == "dll"
        {
            let result = lib::createprojectdll(&lang, &name, &path);
        }
    } 
    else 
    {
        // Get the current directory
        let current_dir = get_current_dir();

        //take in input
        //what type of project does the user want to make?
        println!("Enter the language you want to use: ");
        let mut lang = String::new();
        io::stdin().read_line(&mut lang).expect(&INVALIDINPUT.trim_end());
        //check if the language is supported
        if !SUPPORTEDLANGUAGES.contains(&lang.trim()) {
            // trim removes the newline character, which is needed for the contains function
            print(INVALIDLANGUAGE); // print error message
            for language in SUPPORTEDLANGUAGES.iter() {
                eprintln!("{}", language);
            }
            //panic!("AAAHHHHHHH NOOOOOOOO DAMMMITTT, goodbye. CUSP00015"); // exit the program
            window::windowz();
        }
        // whats the name of the project?
        println!("Enter the name of the project: ");
        let mut name = String::new();
        io::stdin().read_line(&mut name).expect(panic!("Failed to read line"));

        //does the user want it to be a dll or an executable?

        // Use the current directory instead of asking for the path
        let binding = current_dir;
        let path = &binding.to_str().expect("Failed to convert path to string");

        let result = createprojectexecutible(&lang.trim(), &name.trim(), &path);
    }
    
}
/// creates a new project for making a dll project in multiple languages

//TODO add support for other languages

//tests
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_get_current_dir() {
        let current_dir = get_current_dir();
        let current_dir_string = current_dir.to_str().expect("Failed to convert path to string");
        assert_eq!(current_dir_string, "/home/runner/work/ProjectCreator/ProjectCreator");
    }
    #[test]
    fn test_createprojectdll() {
        let current_dir = get_current_dir();
        let path = &current_dir.to_str().expect("Failed to convert path to string");
        let name = "test";
        let lang = "rust";
        createprojectdll(&lang, &name, &path);
        let path = format!("{}/Cargo.toml", path);
        let contents = std::fs::read_to_string(path).expect("Failed to read file");
        assert_eq!(
            contents,
            "[package]\nname = \"dll\"\nversion = \"0.1.0\"\nedition = \"2018\"\n\n[lib]\ncrate-type = [\"cdylib\"]\n\n[dependencies]\n"
        );
    }
    #[test]
    fn test_createprojectexecutible() {
        let current_dir = get_current_dir();
        let path = &current_dir.to_str().expect("Failed to convert path to string");
        let name = "test";
        let lang = "rust";
        createprojectexecutible(&lang, &name, &path);
        let path = format!("{}/Cargo.toml", path);
        let contents = std::fs::read_to_string(path).expect("Failed to read file");
        assert_eq!(
            contents,
            "[package]\nname = \"test\"\nversion = \"0.1.0\"\nedition = \"2018\"\n\n[lib]\ncrate-type = [\"cdylib\"]\n\n[dependencies]\n"
        );
    }
}
