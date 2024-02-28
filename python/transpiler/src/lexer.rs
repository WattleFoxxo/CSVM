pub struct Lexer {
    pub tokens: Vec<Token>,
}

// lexer for CubeScript


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

