use std::collections::HashMap;

// lexer, tokens and parser for CubeScript

// C 2024 OpenStudioCorporation

pub struct Lexer {
    pub tokens: Vec<Token>,
}

// array for tokens
use std::fmt::Display;


impl Lexer {
    pub fn new() -> Self {
        Self { tokens: Vec::new() }
    }
    pub fn lex(&mut self, code: &str) {
        
        let mut token_types = HashMap::new();
        token_types.insert(Token::Ident("struct".to_string()), "struct");
        token_types.insert(Token::Ident("call".to_string()), "call");
        token_types.insert(Token::Ident("if".to_string()), "if");
        token_types.insert(Token::Ident("else".to_string()), "else");
        token_types.insert(Token::Ident("while".to_string()), "while");
        token_types.insert(Token::Ident("for".to_string()), "for");
        token_types.insert(Token::Ident("return".to_string()), "return");
        token_types.insert(Token::Ident("break".to_string()), "break");
        token_types.insert(Token::Ident("continue".to_string()), "continue");
        token_types.insert(Token::Ident("true".to_string()), "true");
        token_types.insert(Token::Ident("false".to_string()), "false");
        token_types.insert(Token::Ident("null".to_string()), "null");
        token_types.insert(Token::Ident("print".to_string()), "print");
        token_types.insert(Token::Ident("println".to_string()), "println");
       
        //string lex
        let mut string = String::new();
        let mut in_string = false;
        //number lex
        let mut number = String::new();
        let mut in_number = false;
        //ident lex
        let mut ident = String::new();
        let mut in_ident = false;
        //comment lex
        let mut in_comment = false;
        let mut in_block_comment = false;
        let mut comment = String::new();
        //operator lex
        let mut operator = String::new();
        let mut in_operator = false;
        //tokenize the input
        


        for c in code.chars() {
            if in_string {
                if c == '"' {
                    self.tokens.push(Token::String(string.clone()));
                    string.clear();
                    in_string = false;
                } else {
                    string.push(c);
                }
            } else if in_number {
                if c.is_numeric() {
                    number.push(c);
                } else {
                    self.tokens.push(Token::Number(number.parse().unwrap()));
                    number.clear();
                    in_number = false;
                }
            } else if in_ident {
                if c.is_alphanumeric() {
                    ident.push(c);
                } else {
                    self.tokens.push(Token::Ident(ident.clone()));
                    ident.clear();
                    in_ident = false;
                }
            } else if in_comment {
                if c == '\n' {
                    self.tokens.push(Token::String(comment.clone()));
                    comment.clear();
                    in_comment = false;
                } else {
                    comment.push(c);
                }
            } else if in_block_comment {
                if c == '*' {
                    in_block_comment = false;
                }
            } else if in_operator {
                if c == '+' || c == '-' || c == '*' || c == '/' {
                    operator.push(c);
                } else {
                    self.tokens.push(Token::Operator(operator.chars().next().unwrap()));
                    operator.clear();
                    in_operator = false;
                }
            } else {
                match c {
                    ' ' | '\t' | '\n' => {}
                    '{' => {
                        self.tokens.push(Token::LBrace);
                    }
                    '}' => {
                        self.tokens.push(Token::RBrace);
                    }
                    ',' => {
                        self.tokens.push(Token::Comma);
                    }
                    '"' => {
                        in_string = true;
                    }
                    '(' => {
                        self.tokens.push(Token::LParen);
                    }
                    ')' => {
                        self.tokens.push(Token::RParen);
                    }
                    '/' => {
                        // check if seccond shash is present
                        if code.chars().nth(1).unwrap() == '/' {
                            in_comment = true;
                        } else if code.chars().nth(1).unwrap() == '*' {
                            in_block_comment = true;
                        }
                    }

                    '0'..='9' => {
                        in_number = true;
                        number.push(c);
                    }
                    'a'..='z' | 'A'..='Z' => {
                        //get the character that we just checked for
                        in_ident = true;
                        ident.push(c);
                    }
                    ';' => {
                        self.tokens.push(Token::Semicolon);
                    }
                    '/' => {
                        if code.chars().nth(1).unwrap() == '/' {
                            in_comment = true;
                        } else if code.chars().nth(1).unwrap() == '*' {
                            in_block_comment = true;
                        }
                    }
                    '+' | '-' | '*' | '/'| '='| '>' | '<'| '!' | '|' | '&'| '^'| '%'| '~'| '?'| ':' => {
                        in_operator = true;
                        operator.push(c);
                    }
                    _ => {}
                }

            }

        }
        // after doing char by char, now we can do string searching.

            // for i in 0..self.tokens.len() {
            //     //convert the token to a string for binary operations
            //     let token = &self.tokens[i];

            //     let token_str = format!("{:?}", token);

            //     //check if the token is a binary operator
            //     if token_str.contains("Operator") {
            //         if token_str.contains("+") {
            //             self.tokens[i] = Token::Plus;
            //         } else if token_str.contains("-") {
            //             self.tokens[i] = Token::Minus;
            //         } else if token_str.contains("*") {
            //             self.tokens[i] = Token::Star;
            //         } else if token_str.contains("/") {
            //             self.tokens[i] = Token::Slash;
            //         } else if token_str.contains("=") {
            //             self.tokens[i] = Token::Equal;
            //         } else if token_str.contains(">") {
            //             self.tokens[i] = Token::Greater;
            //         } else if token_str.contains("<") {
            //             self.tokens[i] = Token::Less;
            //         } else if token_str.contains("!") {
            //             self.tokens[i] = Token::Bang;
            //         } else if token_str.contains("|") {
            //             self.tokens[i] = Token::Or;
            //         } else if token_str.contains("&") {
            //             self.tokens[i] = Token::And;
            //         } else if token_str.contains("^") {
            //             self.tokens[i] = Token::Caret;
            //         } else if token_str.contains("%") {
            //             self.tokens[i] = Token::Mod;
            //         } else if token_str.contains("~") {
            //             self.tokens[i] = Token::Tilde;
            //         } else if token_str.contains("?") {
            //             self.tokens[i] = Token::Question;
            //         } else if token_str.contains(":") {
            //             self.tokens[i] = Token::Colon;
            //         }
            //     }
               
            
        
            self.tokens.push(Token::EOF);
        


            }
    }
-


pub struct Parser {
    pub tokens: Vec<Token>,
}
impl Parser {
    pub fn new(tokens: Vec<Token>) -> Self {
        Self { tokens }
    }
    pub fn peek(&self) -> Option<&Token> {
        self.tokens.get(0)
    }
    pub fn next(&mut self) -> Option<Token> {
        if self.tokens.is_empty() {
            None
        } else {
            Some(self.tokens.remove(0))
        }
    }

    pub fn parse(&self) -> Vec<Node> {
        let mut nodes = Vec::new();
        for token in &self.tokens
        {
            println!("{:?}\n", token );
        }
        nodes
    }
}


pub enum Node {
    Struct(String, Vec<Node>, Vec<Node>),
    Call(String, Vec<Node>),
    Ident(String),
    Add(i32, char, i32),
    Sub(i32, char, i32),
    Mul(i32, char, i32),
    Div(i32, char, i32),
    Number(i32),
    String(String),
    Program(Vec<Node>),
    Semicolon,
    EOF,

}



impl std::fmt::Debug for Token {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{:?}", self);
        Ok(())
    }
}
#[derive(Eq, Hash, PartialEq)]
pub enum Token {
  
    
    Struct(String, Vec<Token>, Vec<Token>),
    Call(String, Vec<Token>),
    Ident(String),
    Number(i32),
    Add(i32, char, i32),
    Sub(i32, char, i32),
    Mul(i32, char, i32),
    Div(i32, char, i32),
    String(String),
    LParen,
    RParen,
    LBrace,
    RBrace,
    Comma,
    Semicolon,
    Colon,
    Equal,
    LBracket,
    RBracket,
    Dot,
    Arrow,
    EOF,
    Plus,
    Minus,
    Star,
    Slash,
    Bang,
    Mod,
    Question,
    Tilde,
    Caret,
    And,
    Or,
    EqualEqual,
    BangEqual,
    Less,
    LessEqual,
    Greater,
    GreaterEqual,
    LeftShift,
    RightShift,
    UnsignedRightShift,
    AddEqual,
    SubEqual,
    MulEqual,
    DivEqual,
    ModEqual,
    AndEqual,
    OrEqual,
    XorEqual,
    LeftShiftEqual,
    RightShiftEqual,
    UnsignedRightShiftEqual,
    Increment,
    Decrement,
    Operator(char),
    Comment(String),
    BlockComment(String),
    If,
    Else,
    While,
    For,
    Foreach,
    Break,
    Continue,
    Goto,
    Return,
   

    
}


// // built in functions

// fn print(args: Vec<Node>) -> Node {
//     for arg in args {
//         match arg {
//             Node::Number(num) => {
//                 println!("{}", num);
//             }
//             Node::String(string) => {
//                 println!("{}", string);
//             }
//             _ => {}
//         }
//     }
//     Node::Number(0)
// }

// fn add(args: Vec<Node>) -> Node {
//     let mut result = 0;
//     for arg in args {
//         match arg {
//             Node::Number(num) => {
//                 result += num;
//             }
//             _ => {}
//         }
//     }
//     Node::Number(result)
// } 
// fn sub(args: Vec<Node>) -> Node {
//     let mut result = 0;
//     for arg in args {
//         match arg {
//             Node::Number(num) => {
//                 result -= num;
//             }
//             _ => {}
//         }
//     }
//     Node::Number(result)
// }
// fn mul(args: Vec<Node>) -> Node {
//     let mut result = 1;
//     for arg in args {
//         match arg {
//             Node::Number(num) => {
//                 result *= num;
//             }
//             _ => {}
//         }
//     }
//     Node::Number(result)
// }
// fn div(args: Vec<Node>) -> Node {
//     let mut result = 1;
//     for arg in args {
//         match arg {
//             Node::Number(num) => {
//                 result /= num;
//             }
//             _ => {}
//         }
//     }
//     Node::Number(result)
// }

// built in structs

fn vec(args: Vec<Node>) -> Node {
    Node::Struct("Vec".to_string(), args, Vec::new())
}

fn map(args: Vec<Node>) -> Node {
    Node::Struct("Map".to_string(), args, Vec::new())
}

fn set(args: Vec<Node>) -> Node {
    Node::Struct("Set".to_string(), args, Vec::new())
}

fn list(args: Vec<Node>) -> Node {
    Node::Struct("List".to_string(), args, Vec::new())
}

fn tuple(args: Vec<Node>) -> Node {
    Node::Struct("Tuple ".to_string(), args, Vec::new())
    
}

fn string(args: Vec<Node>) -> Node {
    Node::Struct("String".to_string(), args, Vec::new())
}

fn file(args: Vec<Node>) -> Node {
    Node::Struct("File".to_string(), args, Vec::new())
}

fn path(args: Vec<Node>) -> Node {
    Node::Struct("Path".to_string(), args, Vec::new())
}

// transpile the code to CSharp

pub fn program(nodes: Vec<Node>) -> Node {
    Node::Program(nodes)
}


pub fn transpile(node: Node) -> String {
    match node {
        Node::Semicolon => ";\n".to_string(),
        Node::EOF => "".to_string(),
        Node::Struct(name, args, body) => {
            let mut result = format!("struct {} {{ \n", name);
            for arg in args {
                result.push_str(&transpile(arg));
            }
            for field in body {
                result.push_str(&transpile(field));
            }
            result.push_str("}\n");
            result
        }
        Node::Call(name, args) => {
            let mut result = format!("{}(", name);
            for arg in args {
                result.push_str(&transpile(arg));
            }
            result.push_str(");\n");
            println!("{}", result);
            result
        }
        Node::Ident(name) => format!("{} ", name),
        Node::Add(left, op, right) => format!("{} + {} \n", left, right),
        Node::Sub(left, op, right) => format!("{} - {} \n", left, right),
        Node::Mul(left, op, right) => format!("{} * {} \n", left, right),
        Node::Div(left, op, right) => format!("{} / {} \n", left, right),
        Node::Number(num) => format!("{} ", num),
        Node::String(string) => format!("\"{}\" ", string),
        Node::Program(nodes) => {
            let mut result = String::new();
            for node in nodes {
                result.push_str(&transpile(node));
            }
            result
        }
    }
}

