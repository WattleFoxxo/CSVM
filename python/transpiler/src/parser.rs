
// parser for CubeScript

// C 2024 OpenStudioCorporation

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
