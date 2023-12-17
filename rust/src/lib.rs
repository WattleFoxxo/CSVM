use std::fmt;
use std::fs::{File, OpenOptions};
use std::io::{BufRead, BufReader, BufWriter, Seek, SeekFrom, Write};
use std::path::Path;
use std::process::Command;

pub enum SuppportedLanguages {
    Rust,
    CSharp,
    C,
    Cpp,
}

pub enum ProjectType {
    Executable,
    Library,
}

impl fmt::Display for SuppportedLanguages {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            SuppportedLanguages::Rust => write!(f, "Rust"),
            SuppportedLanguages::CSharp => write!(f, "C#"),
            SuppportedLanguages::C => write!(f, "C"),
            SuppportedLanguages::Cpp => write!(f, "C++"),
        }
    }
}

impl SuppportedLanguages {
    pub fn enumerate() -> Vec<String> {
        vec![
            SuppportedLanguages::Rust.to_string(),
            SuppportedLanguages::CSharp.to_string(),
            SuppportedLanguages::C.to_string(),
            SuppportedLanguages::Cpp.to_string(),
        ]
    }
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
    if is_rust {
        // Create the crate if it doesn't exist
        let path = Path::new(path);
        Command::new("cargo")
            .arg("new")
            .arg(filename)
            .arg("--bin")
            .arg(&path)
            .spawn()
            .expect("Failed to create rust project");
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

fn create_library(
    is_rust: bool,
    filename: &str,
    contents: &str,
    path: &str,
) -> std::io::Result<()> {
    if is_rust {
        // Create the crate if it doesn't exist
        let path = Path::new(path);
        Command::new("cargo")
            .arg("new")
            .arg(filename)
            .arg("--lib")
            .arg(&path)
            .spawn()
            .expect("Failed to create rust project");

        // Read the Cargo.toml file and add the cdylib crate type
        read_cargo_toml_and_add_dylib(path)?;
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
pub fn create_project_dylib(lang: &str, name: &str, path: &str) {
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
            for language in SuppportedLanguages::enumerate() {
                println!("{}", language);
            }
            println!("{}", SuppportedLanguages::C);
        }
    }
}
/// creates a new project for making an executable in multiple languages
pub fn create_project_executable(lang: &str, name: &str, path: &str) {
    let filenames = [&format!("{}.csproj", name), "Makefile"];

    let os_info = os_info::get().os_type();
    let mut output_type = String::new();

    match os_info {
        os_info::Type::Windows => {
            output_type = "exe".to_string();
        }
        os_info::Type::Macos => {
            output_type = "appimage".to_string();
        }
        os_info::Type::Linux => {
            output_type = "".to_string();
        }
        _ => {
            println!("Unsupported OS");
            return;
        }
    }

    let contents = [
        &format!("<Project Sdk=\"Microsoft.NET.Sdk\">\n\n  <PropertyGroup>\n    <OutputType>{}</OutputType>\n    <TargetFramework>netcoreapp3.1</TargetFramework>\n  </PropertyGroup>\n\n</Project>\n", output_type),
        &format!("CC=gcc\nCFLAGS=-fPIC -Wall\n\n{0}.{1}: {0}.o\n\t$(CC) -o {0}.{1} {0}.o\n\n{0}.o: {0}.c\n\t$(CC) -c -o {0}.o {0}.c\n\n.PHONY: clean\n\nclean:\n\trm -f *.o *.{1}\n", name, output_type),
        &format!("CC=g++\nCFLAGS=-fPIC -Wall\n\n{0}.{1}: {0}.o\n\t$(CC) -o {0}.{1} {0}.o\n\n{0}.o: {0}.cpp\n\t$(CC) -c -o {0}.o {0}.cpp\n\n.PHONY: clean\n\nclean:\n\trm -f *.o *.{1}\n", name, output_type)
    ];

    match lang.to_lowercase().as_str() {
        "rust" => {
            // create a new rust project
            let error = create_file_with_contents(ProjectType::Executable, true, name, "", &path);
            if error.is_err() {
                println!("Error creating Cargo.toml\n");
            }
        }
        "c#" => {
            // create a new C# project
            let error = create_file_with_contents(
                ProjectType::Executable,
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
            // create a new C project's make file with a source file that compiles to an executable

            let error = create_file_with_contents(
                ProjectType::Executable,
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
            // create a new C++ project's make file with a source file that compiles to an executable
            let error = create_file_with_contents(
                ProjectType::Executable,
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
            println!("Invalid language\n");
            println!("please choose from the following languages:");
            for language in SuppportedLanguages::enumerate() {
                println!("{}", language);
            }
        }
    }
}
