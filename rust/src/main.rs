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
        let result = createprojectexecutible(&lang.trim(), &name.trim(), &path.trim());
    } else {
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
            main::new().unwrap().run().unwrap();
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
fn createprojectdll(lang: &str, name: &str, path: &str) {
    match lang {
        "rust" => {
            // create a new rust project
            let error = lib::create_file_with_contents(
                "Cargo.toml",
                "[package]\nname = \"dll\"\nversion = \"0.1.0\"\nedition = \"2018\"\n\n[lib]\ncrate-type = [\"cdylib\"]\n\n[dependencies]\n",
                &path
            );
            if error.is_err() {
                eprintln!("Error creating Cargo.toml\n");
            }
        }
        "CSharp" => {
            // create a new C# project
            let error = lib::create_file_with_contents(
                &std::format!("{}.csproj", name),
                &std::format!(
                    "<Project Sdk=\"Microsoft.NET.Sdk\">\n\n  <PropertyGroup>\n    <TargetFramework>netstandard2.0</TargetFramework>\n  </PropertyGroup>\n\n</Project>\n"
                ),
                &path
            );
            if error.is_err() {
                eprintln!("Error creating {}.csproj\n", name);
            }
        }
        "C" => {
            // create a new C project's make file with a source file
            let error = lib::create_file_with_contents(
                "Makefile",
                &std::format!(
                    "CC=gcc\nCFLAGS=-fPIC -Wall\n\n{}.so: {}.o\n\t$(CC) -shared -o {}.so {}.o\n\n{}.o: {}.c\n\t$(CC) -c -o {}.o {}.c\n\n.PHONY: clean\n\nclean:\n\trm -f *.o *.so\n",
                    name,
                    name,
                    name,
                    name,
                    name,
                    name,
                    name,
                    name
                ),
                &path
            );
            if error.is_err() {
                eprintln!("Error creating Makefile\n");
            }
        }
        "C++" => {
            // create a new C++ project's make file with a source file
            let error = lib::create_file_with_contents(
                "Makefile",
                &std::format!(
                    "CC=g++\nCFLAGS=-fPIC -Wall\n\n{}.so: {}.o\n\t$(CC) -shared -o {}.so {}.o\n\n{}.o: {}.cpp\n\t$(CC) -c -o {}.o {}.cpp\n\n.PHONY: clean\n\nclean:\n\trm -f *.o *.so\n",
                    name,
                    name,
                    name,
                    name,
                    name,
                    name,
                    name,
                    name
                ),
                &path
            );
            if error.is_err() {
                eprintln!("Error creating Makefile\n");
            }
        }

        _ => {
            // trim removes the newline character, which is needed for the contains function
            eprintln!("Invalid language"); // print error message
            eprintln!("please choose from the following languages:");
            for language in SUPPORTEDLANGUAGES.iter() {
                eprintln!("{}", language);
            }
        }
    }
}
/// creates a new project for making an executable in multiple languages
fn createprojectexecutible(lang: &str, name: &str, path: &str) {
    let os_info = os_info::get();
    let mut output_type = String::new();

    if os_info.os_type() == os_info::Type::Windows {
        output_type = "Exe".to_string();
        println!("Windows");
    } else if os_info.os_type() == os_info::Type::Linux {
        output_type = "bin".to_string();
        println!("Linux");
    } else if os_info.os_type() == os_info::Type::Macos {
        output_type = "appimage".to_string();
        println!("Macos");
    } else {
        println!("Unknown");
    }
    match lang {
        "rust" => {
            // create a new rust project
            let error = lib::create_file_with_contents(
                "Cargo.toml",
                &std::format!("[package]\nname = \"{}\"\nversion = \"0.1.0\"\nedition = \"2018\"\n\n[lib]\ncrate-type = [\"cdylib\"]\n\n[dependencies]\n", name),
                &path
            );
            if error.is_err() {
                println!("Error creating Cargo.toml\n");
            }
        }
        "CSharp" => {
            // create a new C# project
            let error = lib::create_file_with_contents(
                &std::format!("{}.csproj", name),
                &std::format!(
                    "<Project Sdk=\"Microsoft.NET.Sdk\">\n\n  <PropertyGroup>\n    <OutputType>{output_type}</OutputType>\n    <TargetFramework>netcoreapp3.1</TargetFramework>\n  </PropertyGroup>\n\n</Project>\n",
                    output_type = output_type
                ),
                &path
            );
            if error.is_err() {
                println!("Error creating {}.csproj\n", name);
            }
        }
        "C" => {
            // create a new C project's make file with a source file that compiles to an executable

            let error = lib::create_file_with_contents(
                "Makefile",
                &std::format!(
                    "CC=gcc\nCFLAGS=-fPIC -Wall\n\n{}.{}: {}.o\n\t$(CC) -o {}.{} {}.o\n\n{}.o: {}.c\n\t$(CC) -c -o {}.o {}.c\n\n.PHONY: clean\n\nclean:\n\trm -f *.o *.{output_type}\n",
                    name,
                    output_type,
                    name,
                    name,
                    output_type,
                    name,
                    name,
                    name,
                    name,
                    output_type = output_type
                ),
                &path
            );
            if error.is_err() {
                println!("Error creating Makefile\n");
            }
        }
        "C++" => {
            // create a new C++ project's make file with a source file that compiles to an executable
            let error = lib::create_file_with_contents(
                "Makefile",
                &std::format!(
                    "CC=g++\nCFLAGS=-fPIC -Wall\n\n{}.{}: {}.o\n\t$(CC) -o {}.{} {}.o\n\n{}.o: {}.cpp\n\t$(CC) -c -o {}.o {}.cpp\n\n.PHONY: clean\n\nclean:\n\trm -f *.o *.{output_type}\n",
                    name,
                    output_type,
                    name,
                    name,
                    output_type,
                    name,
                    name,
                    name,
                    name,
                    output_type = output_type
                ),
                &path
            );
            if error.is_err() {
                println!("Error creating Makefile\n");
            }
        }

        _ => {
            eprintln!("Invalid language\n");
            eprintln!("please choose from the following languages:");
            for language in SUPPORTEDLANGUAGES.iter() {
                eprintln!("{}", language);
            }
        }
    }
}

slint::slint!{
    export component main {
        Text {
            text: "hello world";
            color: green;
        }
    }
}
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
