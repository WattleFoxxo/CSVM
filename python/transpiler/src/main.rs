// threading
use std::thread;
use std::collections::HashMap;
mod cubescript;
use std::env::args;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;
use std::io::Write;
// fn main() {


//     let handle = thread::spawn(move || {
//         pub fn parser2(mut input: String) -> String {
//             let mut output = String::new();
//             let lines: Vec<&str> = input.lines().collect(); // Collect lines into a vector

//             for (i, line) in lines.iter().enumerate() {
//                 let tokens: Vec<&str> = line.split_whitespace().collect(); // Collect tokens into a vector

//                 for (j, token) in tokens.iter().enumerate() {
//                     match *token {
//                         "struct" => output.push_str("static\n"),
//                         "print" => output.push_str("Console.WriteLine\n"),
//                         "retint" => output.push_str("public static int\n"),
//                         "retfloat" => output.push_str("public static float\n"),
//                         "retbool" => output.push_str("public static bool\n"),
//                         "retstring" => output.push_str("public static string\n"),
//                         "retvoid" => output.push_str("public static void\n"),
//                         "int" => output.push_str("int\n"),
//                         "float" => output.push_str("float\n"),
//                         "bool" => output.push_str("bool\n"),
//                         "string" => output.push_str("string \n"),
//                         _ => output.push_str(token),
//                     }
//                     output.push(' '); // Add space after each token
//                 }
//                 output.push('\n'); // Add line break after each line
//             }
//             println!("{}", output);
//             output
//         }

//         //read the args

//         let args: Vec<String> = args().collect();
//         let mut input = String::new();
//         let mut file = File::open(&args[1]).unwrap();
//         file.read_to_string(&mut input).unwrap();
//         let mut cat = parser2(input);
//         print!("{}", cat);
//     });



//     handle.join().unwrap();


// }
fn main() {
    let args: Vec<String> = args().collect();
    let mut input = String::new();
    let mut file = File::open(&args[1]).unwrap();
    file.read_to_string(&mut input).unwrap();
    let tokens = cubescript::lexer(&input).unwrap();
    let ast = cubescript::parser(tokens).unwrap();
    let mut output = String::new();
    for statement in ast {
        match statement {
            cubescript::Statement::Struct(name, fields) => {
                output.push_str(&format!("struct {} {{\n", name));
                for (field, ty) in fields {
                    output.push_str(&format!("    {} {}\n", ty, field));
                }
                output.push_str("}\n");
            }
            cubescript::Statement::Print(expr) => {
                output.push_str(&format!("Console.WriteLine({});\n", expr));
            }
            cubescript::Statement::RetInt(name) => {
                output.push_str(&format!("public static int {}() {{\n", name));
            }
            cubescript::Statement::RetFloat(name) => {
                output.push_str(&format!("public static float {}() {{\n", name));
            }
            cubescript::Statement::RetBool(name) => {
                output.push_str(&format!("public static bool {}() {{\n", name));
            }
            cubescript::Statement::RetString(name) => {
                output.push_str(&format!("public static string {}() {{\n", name));
            }
            cubescript::Statement::RetVoid(name) => {
                output.push_str(&format!("public static void {}() {{\n", name));
            }
            cubescript::Statement::Int(name, _, _) => {
                output.push_str(&format!("int {} = 0;\n", name));
            }
            cubescript::Statement::Float(name, _, _) => {
                output.push_str(&format!("float {} = 0;\n", name));
            }
            cubescript::Statement::Bool(name, _, _) => {
                output.push_str(&format!("bool {} = false;\n", name));
            }
            cubescript::Statement::String(name, _, _) => {
                output.push_str(&format!("string {} = \"\";\n", name));
            }
            
           
            _ => {}
        }
    }
    println!("{}", output);
}