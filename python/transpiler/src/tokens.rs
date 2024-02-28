// Tokens for CubeScript 
// C 2024 OpenStudioCorporation
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