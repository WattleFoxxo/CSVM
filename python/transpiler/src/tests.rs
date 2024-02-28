// Tests for CubeScript 
// C 2024 OpenStudioCorporation

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_lex() {
        let mut lexer = Lexer::new();
        lexer.lex("struct main(string[] args) { print(\"Hello, world!\"); }");
        assert_eq!(
            lexer.tokens,
            vec![
                Token::Ident("struct".to_string()),
                Token::Ident("main".to_string()),
                Token::Ident("string".to_string()),
                Token::Ident("args".to_string()),
                Token::Ident("print".to_string()),
                Token::Ident("Hello".to_string()),
                Token::Ident("world".to_string())
            ]
        );
    }

   
}

#[cfg(test)]
mod parser_tests {
    use super::*;
    
    #[test]
    fn test_parse() {
        let mut lexer = Lexer::new();
        lexer.lex("struct main(string[] args) { print(\"Hello, world!\"); }");
        let parser = Parser::new(lexer.tokens);
        let ast = parser.parse();
        assert_eq!(
            ast,
            vec![Node::Struct(
                "main".to_string(),
                vec![Node::Ident("string".to_string()), Node::Ident("args".to_string())],
                vec![Node::Call(
                    "print".to_string(),
                    vec![Node::String("Hello, world!".to_string())]
                )]
            )]
        );
    }
    #[test]
    fn test_lex_number() {
        let mut lexer = Lexer::new();
        lexer.lex("123");
        assert_eq!(lexer.tokens, vec![Token::Number(123)]);
    }
    
    #[test]
    fn test_lex_ident() {
        let mut lexer = Lexer::new();
        lexer.lex("main");
        assert_eq!(lexer.tokens, vec![Token::Ident("main".to_string())]);
    }
    
    #[test]
    fn test_lex_ident_with_underscore() {
        let mut lexer = Lexer::new();
        lexer.lex("main_");
        assert_eq!(lexer.tokens, vec![Token::Ident("main_".to_string())]);
    }
    
    #[test]
    fn test_lex_ident_with_number() {
        let mut lexer = Lexer::new();
        lexer.lex("main123");
        assert_eq!(lexer.tokens, vec![Token::Ident("main123".to_string())]);
    }
    
    #[test]
    fn test_lex_ident_with_underscore_and_number() {
        let mut lexer = Lexer::new();
        lexer.lex("main_123");
        assert_eq!(lexer.tokens, vec![Token::Ident("main_123".to_string())]);
    }
}
