
// lexer, tokens and parser for CubeScript

// C 2024 OpenStudioCorporation

pub struct Lexer {
    pub tokens: Vec<Token>,
}


impl Lexer {
    pub fn new() -> Self {
        Self { tokens: Vec::new() }
    }
    pub fn lex(&mut self, code: &str) {
        let mut iter = code.chars().peekable();
        while let Some(c) = iter.next() {
            match c {
                '+' => self.tokens.push(Token::Plus),
                '-' => self.tokens.push(Token::Minus),
                '*' => self.tokens.push(Token::Star),
                '/' => self.tokens.push(Token::Slash),
                '(' => self.tokens.push(Token::LParen),
                ')' => self.tokens.push(Token::RParen),
                '{' => self.tokens.push(Token::LBrace),
                '}' => self.tokens.push(Token::RBrace),
                ';' => self.tokens.push(Token::Semicolon),
                '=' => self.tokens.push(Token::Equal),
                '[' => self.tokens.push(Token::LBracket),
                ']' => self.tokens.push(Token::RBracket),
                '.' => self.tokens.push(Token::Dot),
                ',' => self.tokens.push(Token::Comma),
                ':' => self.tokens.push(Token::Colon),
                '"' => {
                    let mut string = String::new();
                    while let Some(&c) = iter.peek() {
                        if c == '"' {
                            iter.next();
                            break;
                        }
                        string.push(c);
                        iter.next();
                    }
                    self.tokens.push(Token::String(string));
                }
                'a'..='z' | 'A'..='Z' => {
                    let mut ident = String::new();
                    ident.push(c);
                    while let Some(&c) = iter.peek() {
                        if c.is_alphanumeric() || c == '_' {
                            ident.push(c);
                            iter.next();
                        } else if c == ':' {
                            ident.push(c);
                            iter.next();
                            if let Some(&c) = iter.peek() {
                                if c == ':' {
                                    ident.push(c);
                                    iter.next();
                                }
                            }
                        } else if c == '.' {
                            ident.push(c);
                            iter.next();
                        } else if c == '(' {
                            ident.push(c);
                            iter.next();
                            if let Some(&c) = iter.peek() {
                                if c == ')' {
                                    ident.push(c);
                                    iter.next();
                                }
                            }
                        } else {
                            break;
                        }
                    }
                    self.tokens.push(Token::Ident(ident));
                }
                '0'..='9' => {
                    let mut num = String::new();
                    num.push(c);
                    while let Some(&c) = iter.peek() {
                        if c.is_numeric() {
                            num.push(c);
                            iter.next();
                        } else if c == '.' {
                            num.push(c);
                            iter.next();
                        } else if c == 'e' || c == 'E' {
                            num.push(c);
                            iter.next();
                        } else if c == '+' || c == '-' {
                            num.push(c);
                            iter.next();
                        } else {
                            break;
                        }
                    }
                    self.tokens.push(Token::Number(num.parse().unwrap()));
                }
                '+' | '-' | '*' | '/' => {
                    self.tokens.push(Token::Operator(c));
                }
                ' ' | '\n' | '\t' | '\r' | '\0' | '\x0C' => {}
                _ => panic!("Unexpected character: {}", c),
            }
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
            match token {
                Token::Number(num) => {
                    nodes.push(Node::Number(*num));
                }
                Token::Add(left, op, right) => {
                    nodes.push(Node::Add(*left, *op, *right));
                }
                Token::Sub(left, op, right) => {
                    nodes.push(Node::Sub(*left, *op, *right));
                }
                Token::Mul(left, op, right) => {
                    nodes.push(Node::Mul(*left, *op, *right));
                }
                Token::Div(left, op, right) => {
                    nodes.push(Node::Div(*left, *op, *right));
                }
                Token::String(string) => {
                    nodes.push(Node::String(string.clone()));
                }
                Token::Ident(ident) => {
                    nodes.push(Node::Ident(ident.clone()));
                }
            // new line after each token
                Token::Semicolon => {
                    nodes.push(Node::Semicolon);
                }
                Token::EOF => {
                    nodes.push(Node::EOF);
                }
                _ => {}
            }
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
            let mut result = format!("struct {} {{\n", name);
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