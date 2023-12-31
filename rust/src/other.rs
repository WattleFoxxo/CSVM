use std::path::{Path, self, PathBuf};
use std::process::Command;
use std::fmt;


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

pub fn print_help() {
    println!("help");
}
