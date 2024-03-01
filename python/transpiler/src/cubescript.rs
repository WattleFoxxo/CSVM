pub fn lexer(input: &str) -> Result<Vec<Token>, String> {
    let mut tokens = Vec::new();
    let mut input = input.chars().peekable();
    while let Some(&c) = input.peek() {
        match c {
            'a'..='z' | 'A'..='Z' => {
                let mut s = String::new();
                while let Some(&c) = input.peek() {
                    match c {
                        'a'..='z' | 'A'..='Z' | '0'..='9' | '_' => {
                            s.push(c);
                            input.next();
                        }
                        _ => break,
                    }
                }
                tokens.push(Token::Identifier(s));
            }
            '0'..='9' => {
                let mut s = String::new();
                while let Some(&c) = input.peek() {
                    match c {
                        '0'..='9' => {
                            s.push(c);
                            input.next();
                        }
                        _ => break,
                    }
                }
                tokens.push(Token::Number(s.parse().unwrap()));
            }
            ' ' | '\t' | '\n' => {
                
                input.next();
            }
            _ => {
                
                    tokens.push(Token::Symbol(c));
                input.next();
                
            }
        }
    }
    Ok(tokens)
}

pub fn parser(tokens: Vec<Token>) -> Result<Vec<Statement>, String> {
    // take in the input and convert into a ast
    let mut statements = Vec::new();
    let mut tokens = tokens.into_iter();
    let mut keyword = String::new();
    while let Some(token) = tokens.next() {
        match token {
            Token::Blank => {
                // Skip blanks
            }
            Token::Identifier(s) => match s.as_str() {
                "struct" => {
                    let name = match tokens.next() {
                        Some(Token::Identifier(s)) => s,
                        _ => return Err(format!("expected identifier, found {:?}", tokens)),
                    };
                    let mut fields = Vec::new();
                    loop {
                        match tokens.next() {
                            Some(Token::Symbol(';')) => break,
                            Some(Token::Identifier(s)) => {
                                let ty = match tokens.next() {
                                    Some(Token::Symbol(';')) => "int".to_string(),
                                    Some(Token::Symbol(',')) => match tokens.next() {
                                        Some(Token::Identifier(s)) => s,
                                        _ => return Err(format!("expected identifier, found {:?}", tokens)),
                                    },
                                    _ => return Err("expected ; or ,".to_string()),
                                };
                                fields.push((s, ty));
                            }
                            _ => return Err("expected ; or identifier".to_string()),
                        }
                    }
                    statements.push(Statement::Struct(name, fields));
                }
                "print" => {
                    let expr = match tokens.next() {
                        Some(Token::Identifier(s)) => s,
                        _ => return Err(format!("expected identifier, found {:?}", tokens)),
                    };
                    statements.push(Statement::Print(expr));
                }
                "retint" => {
                    let name = match tokens.next() {
                        Some(Token::Identifier(s)) => s,
                        _ => return Err(format!("expected identifier, found {:?}", tokens)),
                    };
                    statements.push(Statement::RetInt(name));
                }
                "retfloat" => {
                    let name = match tokens.next() {
                        Some(Token::Identifier(s)) => s,
                        _ => return Err(format!("expected identifier, found {:?}", tokens)),
                    };
                    statements.push(Statement::RetFloat(name));
                }
                "retbool" => {
                    let name = match tokens.next() {
                        Some(Token::Identifier(s)) => s,
                        _ => return Err(format!("expected identifier, found {:?}", tokens)),
                    };
                    statements.push(Statement::RetBool(name));
                }
                "retstring" => {
                    let name = match tokens.next() {
                        Some(Token::Identifier(s)) => s,
                        _ => return Err(format!("expected identifier, found {:?}", tokens)),
                    };
                    statements.push(Statement::RetString(name));
                }
                "retvoid" => {
                    let name = match tokens.next() {
                        Some(Token::Identifier(s)) => s,
                        _ => return Err(format!("expected identifier, found {:?}", tokens)),
                    };
                    statements.push(Statement::RetVoid(name));
                }
                "if" => {
                    let cond = match tokens.next() {
                        Some(Token::Identifier(s)) => s,
                        _ => return Err(format!("expected identifier, found {:?}", tokens)),
                    };
                    let body = match tokens.next() {
                        Some(Token::Symbol('{')) => {
                            let mut body = Vec::new();
                            loop {
                                match tokens.next() {
                                    Some(Token::Symbol('}')) => break,
                                    Some(token) => body.push(token),
                                    _ => return Err("expected }".to_string()),
                                }
                            }
                            body
                        }
                        _ => return Err("expected {".to_string()),
                    };
                    statements.push(Statement::If(cond, body));
                }  
                "else" => {
                    let body = match tokens.next() {
                        Some(Token::Symbol('{')) => {
                            let mut body = Vec::new();
                            loop {
                                match tokens.next() {
                                    Some(Token::Symbol('}')) => break,
                                    Some(token) => body.push(token),
                                    _ => return Err("expected }".to_string()),
                                }
                            }
                            body
                        }
                        _ => return Err("expected {".to_string()),
                    };
                    statements.push(Statement::Else(body));
                }
                "int" => {
                    let name = match tokens.next() {
                        Some(Token::Identifier(s)) => s,
                        _ => return Err(format!("expected identifier, found {:?}", tokens)),
                    };
                    let value = match tokens.next() {
                        Some(Token::Number(s)) => s.parse().unwrap(),
                        _ => return Err(format!("expected number, found {:?}", tokens)),
                    };
                    let end: char = match tokens.next() {
                        Some(Token::Symbol(';')) => ';',
                        _ => return Err(format!("expected ;, found {:?}", tokens)),
                    };
                    statements.push(Statement::Int(name, value, end));
                }
                "float" => {
                    let name = match tokens.next() {
                        Some(Token::Identifier(s)) => s,
                        _ => return Err(format!("expected identifier, found {:?}", tokens)),
                    };
                    let value:f32  = match tokens.next() {
                        Some(Token::Number(s)) => s.parse().unwrap(),
                        _ => return Err(format!("expected number, found {:?}", tokens)),
                    };
                    let end: char = match tokens.next() {
                        Some(Token::Symbol(';')) => ';',
                        _ => return Err(format!("expected ;, found {:?}", tokens)),
                    };
                    statements.push(Statement::Float(name, value, end));
                }
                "bool" => {
                    let name = match tokens.next() {
                        Some(Token::Identifier(s)) => s,
                        _ => return Err(format!("expected identifier, found {:?}", tokens)),
                    };
                    let value: bool = match tokens.next() {
                        Some(Token::Identifier(s)) => s.parse().unwrap(),
                        _ => return Err(format!("expected identifier, found {:?}", tokens)),
                    };
                    let end: char = match tokens.next() {
                        Some(Token::Symbol(';')) => ';',
                        _ => return Err(format!("expected ;, found {:?}", tokens)),
                    };
                    statements.push(Statement::Bool(name, value, end));
;
                }
                "string" => {
                    let name = match tokens.next() {
                        Some(Token::Identifier(s)) => s,
                        _ => return Err(format!("expected identifier, found {:?}", tokens)),
                    };
                    let value = match tokens.next() {
                        Some(Token::Identifier(s)) => s,
                        _ => return Err(format!("expected identifier, found {:?}", tokens)),
                    };
                    let end: char = match tokens.next() {
                        Some(Token::Symbol(';')) => ';',
                        _ => return Err(format!("expected ;, found {:?}", tokens)),
                    };
                    statements.push(Statement::String(name, value, end));
                }
                _ => {
                    keyword = s;
                    return Err(format!("unknown keyword {}", &keyword));
                }
                
            }
            Token::Symbol(';') => {
                statements.push(Statement::Semicolon);
            }
            Token::Number(s) => {
                return Err(format!("unexpected number {:?}", s));
            }
            _ => {
                return Err(format!("unexpected token {:?}", token));
            }

        }
    }
    Ok(statements)
}


#[derive(Debug, Clone, PartialEq)]


pub enum Statement {
    Int(String, i32, char),
    Float(String, f32, char),
    Bool(String, bool, char),
    String(String, String, char),
    Struct(String, Vec<(String, String)>),
    Print(String),
    RetInt(String),
    RetFloat(String),
    RetBool(String),
    RetString(String),
    RetVoid(String),
    If(String, Vec<Token>),
    Else(Vec<Token>),
    Semicolon,
}

#[derive(Debug, Clone, PartialEq)]
pub enum Token {
    Identifier(String),
    Symbol(char),
    Number(String),
    Blank,
}







#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_lexer() {
        let input = "struct Foo { x int; y float; z bool; }";
        let tokens = lexer(input).unwrap();
        assert_eq!(
            tokens,
            vec![
                Token::Identifier("struct".to_string()),
                Token::Identifier("Foo".to_string()),
                Token::Symbol('{'),
                Token::Identifier("x".to_string()),
                Token::Identifier("int".to_string()),
                Token::Symbol(';'),
                Token::Identifier("y".to_string()),
                Token::Identifier("float".to_string()),
                Token::Symbol(';'),
                Token::Identifier("z".to_string()),
                Token::Identifier("bool".to_string()),
                Token::Symbol(';'),
                Token::Symbol('}'),
            ]
        );
    }
    #[test]
    fn test_parser() {
        let tokens = vec![
            Token::Identifier("struct".to_string()),
            Token::Identifier("Foo".to_string()),
            Token::Symbol('{'),
            Token::Identifier("int".to_string()),
            Token::Identifier("x".to_string()),
            Token::Symbol('='),
            Token::Number("0".to_string()),
            Token::Symbol(';'),
            Token::Identifier("float".to_string()),
            Token::Identifier("y".to_string()),
            Token::Symbol('='),
            Token::Number("0.0".to_string()),
            Token::Symbol(';'),
            Token::Identifier("bool".to_string()),
            Token::Identifier("z".to_string()),
            Token::Symbol('='),
            Token::Identifier("false".to_string()),
            Token::Symbol(';'),
            Token::Symbol('}'),
        ];
        let ast = parser(tokens).unwrap();
        assert_eq!(
            ast,
            vec![
                Statement::Struct(
                    "Foo".to_string(),
                    vec![
                        ("x".to_string(), "int".to_string()),
                        ("y".to_string(), "float".to_string()),
                        ("z".to_string(), "bool".to_string()),
                    ]
                )
            ]
        );


}