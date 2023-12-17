// include the packages we need
use creator::create_file_with_contents;
use creator::ProjectType;
use std::env;
use std::io;
const SUPPORTEDLANGUAGES: [&str; 4] = ["Rust", "C#", "C", "C++"];

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
    for language in SUPPORTEDLANGUAGES.iter() {
        println!("{}", language);
    }
    println!("Enter the language you want to use: ");
    let mut lang = String::new();
    io::stdin().read_line(&mut lang).expect(&INVALIDINPUT);
    //check if the language is supported
    if !SUPPORTEDLANGUAGES.contains(&lang.trim().to_lowercase().as_str()) {
        // trim removes the newline character, which is needed for the contains function
        println!("{}", INVALIDLANGUAGE); // print error message
        for language in SUPPORTEDLANGUAGES.iter() {
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

    createprojectexecutible(&lang.trim(), &name.trim(), &path);
}

fn help() {
    println!("help - display this message");
}
/// creates a new project for making a dll project in multiple languages
fn createprojectdll(lang: &str, name: &str, path: &str) {
    let filenames = [&format!("{}.csproj", name), "Makefile"];
    let contents = [
        &format!("<Project Sdk=\"Microsoft.NET.Sdk\">\n\n  <PropertyGroup>\n    <TargetFramework>netstandard2.0</TargetFramework>\n  </PropertyGroup>\n\n</Project>\n"),
        &format!("CC=gcc\nCFLAGS=-fPIC -Wall\n\n{0}.so: {}.o\n\t$(CC) -shared -o {0}.so {0}.o\n\n{0}.o: {0}.c\n\t$(CC) -c -o {0}.o {0}.c\n\n.PHONY: clean\n\nclean:\n\trm -f *.o *.so\n", name),
        &format!("CC=g++\nCFLAGS=-fPIC -Wall\n\n{0}.so: {0}.o\n\t$(CC) -shared -o {0}.so {0}.o\n\n{}.o: {0}.cpp\n\t$(CC) -c -o {0}.o {0}.cpp\n\n.PHONY: clean\n\nclean:\n\trm -f *.o *.so\n", name)
    ];

    match lang.to_lowercase().as_str() {
        "rust" => {
            // create a new rust project
            let error = create_file_with_contents(ProjectType::Library, true, name, "", &path);
            if error.is_err() {
                println!("Error creating Cargo.toml\n");
            }
        }
        "c#" => {
            // create a new C# project
            let error = create_file_with_contents(
                ProjectType::Library,
                false,
                filenames[0],
                contents[0],
                &path,
            );
            if error.is_err() {
                println!("Error creating {}.csproj\n", name);
            }
        }
        "c" => {
            // create a new C project's make file with a source file
            let error = create_file_with_contents(
                ProjectType::Library,
                false,
                filenames[1],
                contents[1],
                &path,
            );
            if error.is_err() {
                println!("Error creating Makefile\n");
            }
        }
        "c++" => {
            // create a new C++ project's make file with a source file
            let error = create_file_with_contents(
                ProjectType::Library,
                false,
                filenames[1],
                contents[2],
                &path,
            );
            if error.is_err() {
                println!("Error creating Makefile\n");
            }
        }

        _ => {
            // trim removes the newline character, which is needed for the contains function
            println!("Invalid language"); // print error message
            println!("please choose from the following languages:");
            for language in SUPPORTEDLANGUAGES.iter() {
                println!("{}", language);
            }
        }
    }
}
/// creates a new project for making an executable in multiple languages
fn createprojectexecutible(lang: &str, name: &str, path: &str) {
    let filenames = [&format!("{}.csproj", name), "Makefile"];
    let contents = [
        &format!("<Project Sdk=\"Microsoft.NET.Sdk\">\n\n  <PropertyGroup>\n    <TargetFramework>netstandard2.0</TargetFramework>\n  </PropertyGroup>\n\n</Project>\n"),
        &format!("CC=gcc\nCFLAGS=-fPIC -Wall\n\n{0}.so: {}.o\n\t$(CC) -shared -o {0}.so {0}.o\n\n{0}.o: {0}.c\n\t$(CC) -c -o {0}.o {0}.c\n\n.PHONY: clean\n\nclean:\n\trm -f *.o *.so\n", name),
        &format!("CC=g++\nCFLAGS=-fPIC -Wall\n\n{0}.so: {0}.o\n\t$(CC) -shared -o {0}.so {0}.o\n\n{}.o: {0}.cpp\n\t$(CC) -c -o {0}.o {0}.cpp\n\n.PHONY: clean\n\nclean:\n\trm -f *.o *.so\n", name)
    ];

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
            let error = create_file_with_contents(ProjectType::Executable, true, name, "", &path);
            if error.is_err() {
                println!("Error creating Cargo.toml\n");
            }
        }
        "CSharp" => {
            // create a new C# project
            let error = create_file_with_contents( ProjectType::Executable, false, filenames[0], &format!("<Project Sdk=\"Microsoft.NET.Sdk\">\n\n  <PropertyGroup>\n    <OutputType>{}</OutputType>\n    <TargetFramework>netcoreapp3.1</TargetFramework>\n  </PropertyGroup>\n\n</Project>\n", output_type), &path);
            if error.is_err() {
                println!("Error creating {}.csproj\n", name);
            }
        }
        "C" => {
            // create a new C project's make file with a source file that compiles to an executable

            let error = create_file_with_contents(ProjectType::Executable, false, filenames[1], &format!("CC=gcc\nCFLAGS=-fPIC -Wall\n\n{}.{}: {}.o\n\t$(CC) -o {}.{} {}.o\n\n{}.o: {}.c\n\t$(CC) -c -o {}.o {}.c\n\n.PHONY: clean\n\nclean:\n\trm -f *.o *.{output_type}\n", name, output_type, name, name, output_type, name, name, name, name, output_type), &path);
            if error.is_err() {
                println!("Error creating Makefile\n");
            }
        }
        "C++" => {
            // create a new C++ project's make file with a source file that compiles to an executable
            let error = create_file_with_contents(ProjectType::Executable, false, filenames[1], &format!("CC=g++\nCFLAGS=-fPIC -Wall\n\n{}.{}: {}.o\n\t$(CC) -o {}.{} {}.o\n\n{}.o: {}.cpp\n\t$(CC) -c -o {}.o {}.cpp\n\n.PHONY: clean\n\nclean:\n\trm -f *.o *.{output_type}\n", name, output_type, name, name, output_type, name, name, name, name, output_type), &path);
            if error.is_err() {
                println!("Error creating Makefile\n");
            }
        }

        _ => {
            println!("Invalid language\n");
            println!("please choose from the following languages:");
            println!("rust");
            println!("CSharp");
            println!("C");
            println!("C++");
        }
    }
}
