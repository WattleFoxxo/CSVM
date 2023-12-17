use std::env;
use std::fs::{File, OpenOptions};
use std::io::{BufRead, BufReader, BufWriter, Seek, SeekFrom, Write};
use std::path::Path;
use std::process::Command;

pub enum ProjectType {
    Executable,
    Library,
}

pub fn create_file_with_contents(
    type_: ProjectType,
    is_rust: bool,
    filename: &str,
    contents: &str,
    path: &str,
) -> std::io::Result<()> {
    match type_ {
        ProjectType::Executable => create_executable(is_rust, filename, contents, path),
        ProjectType::Library => create_library(is_rust, filename, contents, path),
    }
}

fn create_executable(
    is_rust: bool,
    filename: &str,
    contents: &str,
    path: &str,
) -> std::io::Result<()> {
    todo!()
}

fn create_library(
    is_rust: bool,
    filename: &str,
    contents: &str,
    path: &str,
) -> std::io::Result<()> {
    if is_rust {
        // Get current_dir
        let current_dir = env::current_dir().expect("Failed to get current directory");

        // Set the path to the current directory + the specified path
        let path = Path::new(&current_dir).join(path);

        // Create the crate if it doesn't exist
        Command::new("cargo")
            .arg("new")
            .arg("")
            .arg("--lib")
            .spawn()
            .expect("Failed to create rust project");

        // Read the Cargo.toml file and add the cdylib crate type
        read_cargo_toml_and_add_dylib(&path)?;
        Ok(())
    } else {
        let file_path = Path::new(path).join(filename);

        // Create a file at the specified path
        let mut file = File::create(&file_path)?;

        // Write the contents to the file
        file.write_all(contents.as_bytes())?;

        // Return OK
        Ok(())
    }
}

fn read_cargo_toml_and_add_dylib(path: &Path) -> std::io::Result<()> {
    let new_path = path;
    let mut file = OpenOptions::new().write(true).read(true).open(path)?;
    let reader = BufReader::new(&file);
    let mut lines: Vec<String> = reader.lines().map(|l| l.expect("Can't get line")).collect();
    lines[5] = "crate-type = [\"cdylib\"]".to_string();

    file.set_len(0)?;
    file.seek(SeekFrom::Start(0))?;

    let temp_path = new_path.with_extension("tmp");
    let temp_file = OpenOptions::new()
        .write(true)
        .create(true)
        .open(&temp_path)?;
    let mut writer = BufWriter::new(&temp_file);
    for line in &lines {
        writeln!(writer, "{}", line)?;
    }
    writer.flush()?;

    // Replace the original file with the temporary file
    std::fs::remove_file(&new_path)?;
    std::fs::rename(&temp_path, &new_path)?;

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
