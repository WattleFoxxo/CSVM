///struct main (string[] args)
/// {
///   print("Hello, world!");
/// }
/// demo cubescript code
///




use parser;
use lexer::Lexer;
use parser::Parser;
use lexer::Token;
use std::collections::HashMap;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;
use std::path::Path;







fn main() {
    let mut lexer = Lexer::new();
    // read an input file
    let input = std::fs::read("src/testcase.cusp").unwrap();
    let input = String::from_utf8(input).unwrap();
    lexer.lex(&input);
    println!("{:?}", lexer.tokens)
}