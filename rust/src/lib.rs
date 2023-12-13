use std::fs::File;
use std::io::prelude::*;
use std::path::Path;
pub fn print(message: &str){
    println!("{}", message);
}

pub fn create_file_with_contents(filename: &str, contents: &str, path: &str) -> std::io::Result<()> {
    // Create the file path by joining the specified path and the filename
    let file_path = Path::new(path).join(filename);

    // Create a file at the specified path
    let mut file = File::create(&file_path)?;

    // Write the contents to the file
    file.write_all(contents.as_bytes())?;

    // Return OK
    Ok(())
}