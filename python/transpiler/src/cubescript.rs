
// lexer, tokens and parser for CubeScript

// C 2024 OpenStudioCorporation
pub impl Lexer {
    pub fn new() -> Self {
        Self { tokens: Vec::new() }
    }

    pub fn lex(&mut self, code: &str) {
        let mut iter = code.chars().peekable();
        while let Some(c) = iter.next() {
            match c {
                'a'..='z' | 'A'..='Z' => {
                    let mut ident = String::new();
                    ident.push(c);
                    while let Some(&c) = iter.peek() {
                        if c.is_alphanumeric() || c == '_' {
                            ident.push(c);
                            iter.next();
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
                        } else {
                            break;
                        }
                    }
                    self.tokens.push(Token::Number(num.parse().unwrap()));
                }
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
                ' ' | '\n' | '\t' => {}
                _ => panic!("Unexpected character: {}", c),
            }
        }
    }
}


pub struct Parser {
    pub tokens: Vec<Token>,
}

pub impl Parser {
    pub fn new(tokens: Vec<Token>) -> Self {
        Self { tokens }
    }

    pub fn parse(&self) -> Vec<Node> {
        let mut nodes = Vec::new();
        for token in &self.tokens
        {
            match token {
                Token::Ident(ident) => {
                    nodes.push(Node::Ident(ident.clone()));
                }
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
}