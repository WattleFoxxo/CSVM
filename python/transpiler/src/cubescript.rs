use std::collections::HashMap;

// lexer, tokens and parser for CubeScript

// C 2024 OpenStudioCorporation

pub struct Lexer {
    pub tokens: Vec<Token>,
}

// array for tokens

impl Lexer {
    pub fn new() -> Self {
        Self { tokens: Vec::new() }
    }
    pub fn lex(&mut self, code: &str) {
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
                        for c in code.chars() {
                            if in_string {
                                // Handle string characters
                                if c == '"' {
                                    self.tokens.push(Token::String(string.clone()));
                                    string.clear();
                                    in_string = false;
                                } else {
                                    string.push(c);
                                }
                            } else if in_ident {
                                // Handle identifiers (functions/variables)
                                if c.is_alphanumeric() || c == '_' {
                                    ident.push(c);
                                } else if c == '(' {
                                    // Start of function call
                                    self.tokens.push(Token::Call(ident.clone(), Vec::new()));
                                    ident.clear();
                                    in_ident = false;
                                } else {
                                    // End of identifier, push as token
                                    self.tokens.push(Token::Ident(ident.clone()));
                                    ident.clear();
                                    in_ident = false;
                                }
                            } else {
                                match c {
                                    // Handle other characters and tokens
                                    
                                    '\0'..='/' => {
                                        self.tokens.push(Token::Operator(c));
                                    }
                                    ':'..='\u{d7ff}' => {
                                        self.tokens.push(Token::Operator(c));
                                    }
                                    '\u{e000}'..='\u{10ffff}' => {
                                        self.tokens.push(Token::Operator(c));
                                    }
                                    '0'..='9' => {
                                        for c in code.chars() {
                                            if in_number {
                                                if c.is_numeric() {
                                                    number.push(c);
                                                } else {
                                                    self.tokens.push(
                                                        Token::Number(number.parse().unwrap())
                                                    );
                                                    number.clear();
                                                    in_number = false;
                                                }
                                            } else {
                                                in_number = true;
                                                number.push(c);
                                            }
                                        }
                                    }
                                }
                            }
                        }let mut in_struct_block = false;
                        let mut block_depth = 0;
                        let mut index = 0;
                        let mut field = String::new();
                        let mut struct_fields = Vec::new();
                        let mut struct_name = String::new();

                        for token in self.tokens.iter().skip(index + 2) {
                            match token {
                                Token::Ident(ident) => {
                                    struct_name = ident.clone();
                                }
                                _ => {}
                            }
                        }

                        

                        // Parse struct block
                        for token in self.tokens.iter().skip(index + 3) {
                            match token {
                                Token::LBrace => {
                                    in_struct_block = true;
                                    block_depth += 1;
                                }
                                Token::RBrace => {
                                    block_depth -= 1;
                                    if block_depth == 0 {
                                        break; // End of struct block
                                    }
                                }
                                Token::Ident(ident) if in_struct_block && block_depth == 1 => {
                                    field = ident.clone();
                                    struct_fields.push(field.clone());
                                }
                                _ => {}
                            }
                        }

                        // Now we have the struct name and struct fields
                        println!("Struct Name: {}", struct_name);
                        println!("Struct Fields: {:?}", struct_fields);
                    }
                    _ => {}
                }
            }
            // after doing char by char, now we can do string searching.

            self.tokens.push(Token::EOF);
        }
    }
}

#[derive(Debug, PartialEq)]
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
        if self.tokens.is_empty() { None } else { Some(self.tokens.remove(0)) }
    }

    pub fn parse(&self) -> Vec<Node> {
        let mut nodes = Vec::new();
        for token in &self.tokens {
            println!("{:?}\n", token);
        }
        nodes
    }
}

#[derive(Debug, PartialEq)]
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
#[derive(Debug, PartialEq)]
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
    clone,
}

// built in functions

fn print(args: Vec<Node>) -> Node {
    for arg in args {
        match arg {
            Node::Number(num) => {
                println!("{}", num);
            }
            Node::String(string) => {
                println!("{}", string);
            }
            _ => {}
        }
    }
    Node::Number(0)
}

fn add(args: Vec<Node>) -> Node {
    let mut result = 0;
    for arg in args {
        match arg {
            Node::Number(num) => {
                result += num;
            }
            _ => {}
        }
    }
    Node::Number(result)
}
fn sub(args: Vec<Node>) -> Node {
    let mut result = 0;
    for arg in args {
        match arg {
            Node::Number(num) => {
                result -= num;
            }
            _ => {}
        }
    }
    Node::Number(result)
}
fn mul(args: Vec<Node>) -> Node {
    let mut result = 1;
    for arg in args {
        match arg {
            Node::Number(num) => {
                result *= num;
            }
            _ => {}
        }
    }
    Node::Number(result)
}
fn div(args: Vec<Node>) -> Node {
    let mut result = 1;
    for arg in args {
        match arg {
            Node::Number(num) => {
                result /= num;
            }
            _ => {}
        }
    }
    Node::Number(result)
}

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
