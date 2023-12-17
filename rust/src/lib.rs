use std::path::Path;
use std::fs::File;
use std::io::prelude::*;
use main::SUPPORTEDLANGUAGES;
pub fn print(message: &str) {
    println!("{}", message);
}

pub fn create_file_with_contents(
    filename: &str,
    contents: &str,
    path: &str,
) -> std::io::Result<()> {
    // Create the file path by joining the specified path and the filename
    let file_path = Path::new(path).join(filename);

    // Create a file at the specified path
    let mut file = File::create(&file_path)?;

    // Write the contents to the file
    file.write_all(contents.as_bytes())?;

    // Return OK
    Ok(())
}
pub fn createprojectdll(lang: &str, name: &str, path: &str) {
    match lang {
        "rust" => {
            // create a new rust project
            let error = create_file_with_contents(
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
            let error = create_file_with_contents(
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
            let error = create_file_with_contents(
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
            let error = create_file_with_contents(
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
pub fn createprojectexecutible(lang: &str, name: &str, path: &str) {
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
            let error = create_file_with_contents(
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
            let error = create_file_with_contents(
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

            let error = create_file_with_contents(
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
            let error = create_file_with_contents(
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