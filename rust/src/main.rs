// include the packages we need
use lib::create_file_with_contents;
use std::io;
mod lib;

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
        "createproject" => {
            println!("Enter the language you want to use: ");
            let mut lang = String::new();
            io::stdin().read_line(&mut lang)
            .expect("Failed to read line\n");
            //
            println!("Enter the name of the project: ");
            let mut name = String::new();
            io::stdin().read_line(&mut name)
            .expect("Failed to read line\n");
            //
            println!("Enter the path to the project: ");
            let mut path = String::new();
            io::stdin().read_line(&mut path)
            .expect("Failed to read line\n");
            // 
            createprojectexecutible(&lang.trim(), &name.trim(), &path.trim());
        }
        _ => {
            println!("Invalid command\n");
        }
    }
}
}
fn help(){
    lib::print("help - display this message");
}

/// creates a new project for making a dll project in multiple languages
fn createprojectdll(lang: &str, name: &str, path: &str){

    
    match lang {
        "rust" => {
            // create a new rust project
            let error = lib::create_file_with_contents("Cargo.toml", "[package]\nname = \"dll\"\nversion = \"0.1.0\"\nedition = \"2018\"\n\n[lib]\ncrate-type = [\"cdylib\"]\n\n[dependencies]\n", &path);
            if error.is_err(){
                println!("Error creating Cargo.toml\n");
            }
        }
        "CSharp" => {
            // create a new C# project
            let error = lib::create_file_with_contents(&format!("{}.csproj", name), &format!("<Project Sdk=\"Microsoft.NET.Sdk\">\n\n  <PropertyGroup>\n    <TargetFramework>netstandard2.0</TargetFramework>\n  </PropertyGroup>\n\n</Project>\n"), &path);
            if error.is_err(){
                println!("Error creating {}.csproj\n", name);
            }
        }
        "C" => {
            // create a new C project's make file with a source file
            let error = lib::create_file_with_contents("Makefile", &format!("CC=gcc\nCFLAGS=-fPIC -Wall\n\n{}.so: {}.o\n\t$(CC) -shared -o {}.so {}.o\n\n{}.o: {}.c\n\t$(CC) -c -o {}.o {}.c\n\n.PHONY: clean\n\nclean:\n\trm -f *.o *.so\n", name, name, name, name, name, name, name, name), &path);
            if error.is_err(){
                println!("Error creating Makefile\n");
            }
        }
        "C++" => {
            // create a new C++ project's make file with a source file
            let error = lib::create_file_with_contents("Makefile", &format!("CC=g++\nCFLAGS=-fPIC -Wall\n\n{}.so: {}.o\n\t$(CC) -shared -o {}.so {}.o\n\n{}.o: {}.cpp\n\t$(CC) -c -o {}.o {}.cpp\n\n.PHONY: clean\n\nclean:\n\trm -f *.o *.so\n", name, name, name, name, name, name, name, name), &path);
            if error.is_err(){
                println!("Error creating Makefile\n");
            }
        }

        _ => {
            println!("Invalid language\n");
        }
    }

}
/// creates a new project for making an executable in multiple languages
fn createprojectexecutible(lang: &str, name: &str, path: &str)
{
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
            let error = lib::create_file_with_contents("Cargo.toml", &format!("[package]\nname = \"{}\"\nversion = \"0.1.0\"\nedition = \"2018\"\n\n[lib]\ncrate-type = [\"cdylib\"]\n\n[dependencies]\n",name), &path);
            if error.is_err(){
                println!("Error creating Cargo.toml\n");
            }
        }
        "CSharp" => {
            // create a new C# project
            let error = lib::create_file_with_contents(&format!("{}.csproj", name), &format!("<Project Sdk=\"Microsoft.NET.Sdk\">\n\n  <PropertyGroup>\n    <OutputType>{output_type}</OutputType>\n    <TargetFramework>netcoreapp3.1</TargetFramework>\n  </PropertyGroup>\n\n</Project>\n", output_type=output_type), &path);
            if error.is_err(){
                println!("Error creating {}.csproj\n", name);
            }
        }
        "C" => {
            // create a new C project's make file with a source file that compiles to an executable
            
            let error = lib::create_file_with_contents("Makefile", &format!("CC=gcc\nCFLAGS=-fPIC -Wall\n\n{}.{}: {}.o\n\t$(CC) -o {}.{} {}.o\n\n{}.o: {}.c\n\t$(CC) -c -o {}.o {}.c\n\n.PHONY: clean\n\nclean:\n\trm -f *.o *.{output_type}\n", name, output_type, name, name, output_type, name, name, name, name, output_type=output_type), &path);
            if error.is_err(){
                println!("Error creating Makefile\n");
            }
        }
        "C++" => {
            // create a new C++ project's make file with a source file that compiles to an executable
            let error = lib::create_file_with_contents("Makefile", &format!("CC=g++\nCFLAGS=-fPIC -Wall\n\n{}.{}: {}.o\n\t$(CC) -o {}.{} {}.o\n\n{}.o: {}.cpp\n\t$(CC) -c -o {}.o {}.cpp\n\n.PHONY: clean\n\nclean:\n\trm -f *.o *.{output_type}\n", name, output_type, name, name, output_type, name, name, name, name, output_type=output_type), &path);
            if error.is_err(){
                println!("Error creating Makefile\n");
            }
        }

        _ => {
            println!("Invalid language\n");
        }
    }
}