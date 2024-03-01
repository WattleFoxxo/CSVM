#![feature(try_blocks)]

//struct main (string[] args)
// {
//   print("Hello, world!");
// }
// demo cubescript code
//






mod cubescript;

use crate::cubescript::Node;


use crate::cubescript::Parser;

fn main() {
    let result: Result<(), std::io::Error> = try {
        let mut lexer = cubescript::Lexer::new();
        // read an input file
        let input = std::fs::read("src/testcase.cusp").unwrap();
        // strip the newlines including any whitespace and tabs
        let input = String::from_utf8_lossy(&input);
        // tokenize the input
        println!("{}", input);
        lexer.lex(&input);
        println!("{:?}", lexer.tokens);
        Parser::new(lexer.tokens).parse();

    };

    if let Err(error) = result {
        // Handle the error here
        println!("An error occurred: {}", error);
    }
}
    