# welcome to the rewrite of the transpiler.py file
# this file contains the parser and lexer for Cubescript.

# the output of this file will be C# code


from transpiler import keywords
import re
from templates import TokenTypes


class Error:
    # this class takes in the line number, the position of the error, the line for the error and the error message
    
    def __init__(self, line_num, pos, line, error):
        self.line_num = line_num
        self.pos = pos
        self.line = line
        self.error = error
    def __repr__(self):
        """ returns the error message in a way that mimmics Rusts error messages
        """
        return f"Error: {self.error}\nLine: {self.line_num}\nPosition: {self.pos}\nLine: {self.line}"
    def __str__(self):
        """ returns the error message in a way that mimmics Rusts error messages
        """
        return f"Error: {self.error}\nLine: {self.line_num}\nPosition: {self.pos}\nLine: {self.line}"
class Token:
    def __init__(self, type, value, line_num, pos):
        self.type = type
        self.value = value
        self.line_num = line_num
        self.pos = pos
    def __repr__(self):
        return f"Token({self.type}, {self.value}, {self.line_num}, {self.pos})"
    def __str__(self):
        return f"Token({self.type}, {self.value}, {self.line_num}, {self.pos})"
    
    
    
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]
        self.current_token = None
        self.current_type = None
        self.tokens = []
        self.types = []
        self.keywords = keywords
        
    def error(self, error):
        raise Exception(error)
    
    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
            
        else:
            self.current_char = self.text[self.pos]
            
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
            
    def number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
            
        if self.current_char == ".":
            result += self.current_char
            self.advance()
            
            while self.current_char is not None and self.current_char.isdigit():
                result += self.current_char
                self.advance()
                
            token = Token(TokenTypes["NUMBER"], float(result), self.line_num, self.pos)
            self.tokens.append(token)
            self.types.append(TokenTypes["NUMBER"])
            return token
        
        token = Token(TokenTypes["NUMBER"], int(result), self.line_num, self.pos)
        self.tokens.append(token)
        self.types.append(TokenTypes["NUMBER"])
        return token
    
    def string(self):
        result = ''
        self.advance()
        
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()
            
        self.advance()
        token = Token(TokenTypes["STRING"], result, self.line_num, self.pos)
        self.tokens.append(token)
        self.types.append(TokenTypes["STRING"])
        return token
    
    def identifier(self):
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()
            
        token = Token(TokenTypes["IDENTIFIER"], result, self.line_num, self.pos)
        self.tokens.append(token)
        self.types.append(TokenTypes["IDENTIFIER"])
        return token
    
    def comment(self):
        result = ''
        while self.current_char is not None and self.current_char != '\n':
            result += self.current_char
            self.advance()
            
        token = Token(TokenTypes["COMMENT"], result, self.line_num, self.pos)
        self.tokens.append(token)
        self.types.append(TokenTypes["COMMENT"])
        return token

    def newline(self):
        token = Token(TokenTypes["NEWLINE"], "\n", self.line_num, self.pos)
        self.tokens.append(token)
        self.types.append(TokenTypes["NEWLINE"])
        return token
    
    def operator(self):
        result = ''
        while self.current_char is not None and self.current_char in "!=<>+-*/%":
            result += self.current_char
            self.advance()
            
        token = Token(TokenTypes["OPERATOR"], result, self.line_num, self.pos)
        self.tokens.append(token)
        self.types.append(TokenTypes["OPERATOR"])
        return token
    
    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                
            if self.current_char.isdigit():
                return self.number()
            
            if self.current_char == '"':
                return self.string()
            
            if self.current_char.isalpha():
                return self.identifier()
            
            if self.current_char == '#':
                return self.comment()
            
            if self.current_char == '\n':
                return self.newline()
            
            if self.current_char in "!=<>+-*/%":
                return self.operator()
            
            if self.current_char == '(':
                token = Token(TokenTypes["LBRACE"], "(", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["LBRACE"])
                self.advance()
                return token
            
            if self.current_char == ')':
                token = Token(TokenTypes["RBRACE"], ")", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["RBRACE"])
                self.advance()
                return token
            
            if self.current_char == '{':
                token = Token(TokenTypes["LBRACKET"], "{", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["LBRACKET"])
                self.advance()
                return token
            
            if self.current_char == '}':
                token = Token(TokenTypes["RBRACKET"], "}", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["RBRACKET"])
                self.advance()
                return token
            
            if self.current_char == ';':
                token = Token(TokenTypes["SEMICOLON"], ";", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["SEMICOLON"])
                self.advance()
                return token
            
            if self.current_char == ',':
                token = Token(TokenTypes["COMMA"], ",", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["COMMA"])
                self.advance()
                return token
            
            if self.current_char == '.':
                token = Token(TokenTypes["DOT"], ".", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["DOT"])
                self.advance()
                return token
            
            if self.current_char == ':':
                token = Token(TokenTypes["COLON"], ":", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["COLON"])
                self.advance()
                return token
            
            if self.current_char == '[':
                token = Token(TokenTypes["LBRACKET"], "[", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["LBRACKET"])
                self.advance()
                return token
            
            if self.current_char == ']':
                token = Token(TokenTypes["RBRACKET"], "]", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["RBRACKET"])
                self.advance()
                return token
            
            if self.current_char == '$':
                token = Token(TokenTypes["DOLLAR"], "$", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["DOLLAR"])
                self.advance()
                return token
            
            if self.current_char == '@':
                token = Token(TokenTypes["AT"], "@", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["AT"])
                self.advance()
                return token
            
            if self.current_char == '&':
                token = Token(TokenTypes["AMPERSAND"], "&", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["AMPERSAND"])
                self.advance()
                return token
            
            if self.current_char == '^':
                token = Token(TokenTypes["CARET"], "^", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["CARET"])
                self.advance()
                return token
            
            if self.current_char == '~':
                token = Token(TokenTypes["TILDE"], "~", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["TILDE"])
                self.advance()
                return token
            
            if self.current_char == '|':
                token = Token(TokenTypes["PIPE"], "|", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["PIPE"])
                self.advance()
                return token
            
            if self.current_char == '?':
                token = Token(TokenTypes["QUESTION"], "?", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["QUESTION"])
                self.advance()
                return token
            
            if self.current_char == '!':
                token = Token(TokenTypes["EXCLAMATION"], "!", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["EXCLAMATION"])
                self.advance()
                return token
                
            if self.current_char == 'using':
                token = Token(TokenTypes["USING"], "using", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["USING"])
                self.advance
                return token
            if self.current_char == 'switch':
                token = Token(TokenTypes["SWITCH"], "switch", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["SWITCH"])
                self.advance
                return token
            if self.current_char == 'stop':
                token = Token(TokenTypes["USING"], "using", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["USING"])
                self.advance
                return token
            if self.current_char == 'at':
                token = Token(TokenTypes["USING"], "using", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["USING"])
                self.advance
                return token
            if self.current_char == 'bland':
                token = Token(TokenTypes["USING"], "using", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["USING"])
                self.advance
                return token
            if self.current_char == 'struct':
                token = Token(TokenTypes["STRUCT"], "struct", self.line_num, self.pos)
                self.tokens.append(token)
                self.types.append(TokenTypes["STRUCT"])
                self.advance
                return token
            # if self.current_char == 'using':
            #     token = Token(TokenTypes["USING"], "using", self.line_num, self.pos)
            #     self.tokens.append(token)
            #     self.types.append(TokenTypes["USING"])
            #     self.advance
            #     return token
            # if self.current_char == 'using':
            #     token = Token(TokenTypes["USING"], "using", self.line_num, self.pos)
            #     self.tokens.append(token)
            #     self.types.append(TokenTypes["USING"])
            #     self.advance
            #     return token
            # if self.current_char == 'using':
            #     token = Token(TokenTypes["USING"], "using", self.line_num, self.pos)
            #     self.tokens.append(token)
            #     self.types.append(TokenTypes["USING"])
            #     self.advance
            #     return token
            # if self.current_char == 'using':
            #     token = Token(TokenTypes["USING"], "using", self.line_num, self.pos)
            #     self.tokens.append(token)
            #     self.types.append(TokenTypes["USING"])
            #     self.advance
            #     return token
            
            
            
            self.error(f"Invalid character: {self.current_char}")
            
        return Token(TokenTypes["EOF"], None, self.line_num, self.pos)
    
    def lex(self):
        self.line_num = 1
        while self.current_char is not None:
            token = self.get_next_token()
            if token.type == TokenTypes["NEWLINE"]:
                self.line_num += 1
            self.advance()
            
        return self.tokens, self.types
    

    
    

class Nodes:
    def __init__(self):
        pass
    
    def __repr__(self):
        return f"{self.__class__.__name__}"
    
    def __str__(self):
        return f"{self.__class__.__name__}"
    
class IfNode(Nodes):
    def __init__(self, condition, if_block, else_block):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block
        
    def __repr__(self):
        return f"IfNode({self.condition}, {self.if_block}, {self.else_block})"
    
    def __str__(self):
        return f"IfNode({self.condition}, {self.if_block}, {self.else_block})"
    
class ElseNode(Nodes):
    def __init__(self, else_block):
        self.else_block = else_block
        
    def __repr__(self):
        return f"ElseNode({self.else_block})"
    
    def __str__(self):
        return f"ElseNode({self.else_block})"
    
class WhileNode(Nodes):
    def __init__(self, condition, while_block):
        self.condition = condition
        self.while_block = while_block
        
    def __repr__(self):
        return f"WhileNode({self.condition}, {self.while_block})"
    
    def __str__(self):
        return f"WhileNode({self.condition}, {self.while_block})"
    
class NewNode(Nodes):
    def __init__(self, new_block):
        self.new_block = new_block
        
    def __repr__(self):
        return f"NewNode({self.new_block})"
    
    def __str__(self):
        return f"NewNode({self.new_block})"
    
class ForNode(Nodes):
    def __init__(self, for_block):
        self.for_block = for_block
        
    def __repr__(self):
        return f"ForNode({self.for_block})"
    
    def __str__(self):
        return f"ForNode({self.for_block})"
    
class SwitchNode(Nodes):
    def __init__(self, switch_block):
        self.switch_block = switch_block
        
    def __repr__(self):
        return f"SwitchNode({self.switch_block})"
    
    def __str__(self):
        return f"SwitchNode({self.switch_block})"
    
class CaseNode(Nodes):
    def __init__(self, case_block):
        self.case_block = case_block
        
    def __repr__(self):
        return f"CaseNode({self.case_block})"
    
    def __str__(self):
        return f"CaseNode({self.case_block})"
    
class DefaultNode(Nodes):
    def __init__(self, default_block):
        self.default_block = default_block
        
    def __repr__(self):
        return f"DefaultNode({self.default_block})"
    
    def __str__(self):
        return f"DefaultNode({self.default_block})"
    
class BreakNode(Nodes):
    def __init__(self, break_block):
        self.break_block = break_block
        
    def __repr__(self):
        return f"BreakNode({self.break_block})"
    
    def __str__(self):
        return f"BreakNode({self.break_block})"
    
class ContinueNode(Nodes):
    def __init__(self, continue_block):
        self.continue_block = continue_block
        
    def __repr__(self):
        return f"ContinueNode({self.continue_block})"
    
    def __str__(self):
        return f"ContinueNode({self.continue_block})"
    
class ReturnNode(Nodes):
    def __init__(self, return_block):
        self.return_block = return_block
        
    def __repr__(self):
        return f"ReturnNode({self.return_block})"
    
    def __str__(self):
        return f"ReturnNode({self.return_block})"
    
class PublicNode(Nodes):
    def __init__(self, public_block):
        self.public_block = public_block
        
    def __repr__(self):
        return f"PublicNode({self.public_block})"
    
    def __str__(self):
        return f"PublicNode({self.public_block})"

class BlockNode(Nodes):
    def __init__(self, block):
        self.block = block
        
    def __repr__(self):
        return f"BlockNode({self.block})"
    
    def __str__(self):
        return f"BlockNode({self.block})"
class BraceNode(Nodes):
    def __init__(self, brace):
        self.brace = brace
        
    def __repr__(self):
        return f"BlockNode({self.brace})"
    
    def __str__(self):
        return f"BlockNode({self.brace})"
class Parser:
    def __init__(self, tokens, types):
        self.tokens = tokens
        self.types = types
        self.pos = 0
        self.current_token = self.tokens[self.pos]
        self.current_type = self.types[self.pos]
        
    def error(self, error):
        raise Exception(error)
    
    def advance(self):
        self.pos += 1
        if self.pos > len(self.tokens) - 1:
            self.current_token = None
            self.current_type = None
            
        else:
            self.current_token = self.tokens[self.pos]
            self.current_type = self.types[self.pos]
            
    def skip_whitespace(self):
        while self.current_token is not None and self.current_token.isspace():
            self.advance()
            
            
            
    def parse(self):
        while self.current_token is not None:
            if self.current_token.type == 'IDENTIFIER':
                print(f'Identifier: {self.current_token.value}')
            elif self.current_token.type == 'LBRACE':
                self.parse_block()
            elif self.current_token.type == 'KEYWORD':
                self.parse_keyword()
            elif self.current_token.type == 'STRING':
                self.parse_string()
            elif self.current_token.type == 'USING':
                self.parse_import()
            elif self.current_token.type == 'SWITCH':
                self.parse_switch(self)
            elif self.current_token.type == 'CASE':
                self.parse_case(self)
            elif self.current_token.type == 'DEFAULT':
                self.parse_default(self)
                
            self.advance()

    def parse_block(self):
        print('Start of block')
        self.advance()  # Skip past the opening brace
        while self.current_token is not None and self.current_token.type != 'RBRACE':
            if self.current_token.type == 'IDENTIFIER':
                print(f'Identifier: {self.current_token.value}')
            self.advance()
        print('End of block')
        
    def parse_import(self):
        print('Start of import')
        self.advance()  # Skip past the 'using' keyword
        while self.current_token is not None and self.current_token.type == 'IDENTIFIER':
            print(f'Import: {self.current_token.value}')
            self.advance()
        print('End of import')
        
    def parse_keyword(self):
        # Define a dictionary of keywords and their corresponding parse methods
        keyword_methods = {
            "new": self.parse_new(self),
            "if": self.parse_if(self),
            "else": self.parse_else(self),
            "while": self.parse_while(self),
            "using": self.parse_import(self),
            "for": self.parse_for(self),
            "switch": self.parse_switch(self),
            "case": self.parse_case(self),
            "default": self.parse_default(self),
            "break": self.parse_break(self),
            
        }

        # Get the parse method for the current keyword
        keyword_method = keyword_methods.get(self.current_token.value)

        if keyword_method is not None:
            # Call the parse method
            keyword_method()
        else:
            # Raise an error if the keyword is not recognized
            self.error(f"Invalid keyword: {self.current_token.value}")
    
    def parse_if(self):
        # Iterate through the if statement and extract the contents of the if loop
        if_token = self.current_token
        
        # Check if the next token is an opening parenthesis
        if if_token.type != 'IF':
            self.error('Expected "IF" keyword')
        
        # Move to the next token
        self.advance()
        
        # Parse the condition expression
        condition = self.parse_expression()
        
        # Check if the next token is a closing parenthesis
        if self.current_token.type != 'RPAREN':
            self.error('Expected ")"')
        
        # Move to the next token
        self.advance()
        
        # Parse the if block
        if_block = self.parse_block()
        
        # Check if there is an "ELSE" keyword
        if self.current_token.type == 'ELSE':
            # Move to the next token
            self.advance()
            
            # Parse the else block
            else_block = self.parse_block()
        else:
            else_block = None
        
        # Create an IfNode with the parsed information
        if_node = IfNode(condition, if_block, else_block)
        
        return if_node
    def parse_brace(self):
        # Iterate through the brace statement and extract the contents of the brace block
        brace_token = self.current_token
        
        # Check if the next token is an opening brace
        if brace_token.type != 'BRACE':
            self.error('Expected "{"')
        
        # Move to the next token
        self.advance()
        
        # Parse the brace block
        brace_block = self.parse_block()
        
        # Check if the next token is a closing brace
        if self.current_token.type != 'BRACE':
            self.error('Expected "}"')
        
        # Move to the next token
        self.advance()
        
        # Create a BraceNode with the parsed information
        brace_node = BraceNode(brace_block)
        
        return brace_node
    
    def parse_brace_end(self):
        brace_end_token = self.current_token
        
        # Check if the next token is a closing brace
        if brace_end_token.type != 'RBRACE':
            self.error('Expected ")"')
        
        # Move to the next token
        self.advance()
        
        # Return the brace end token
        return brace_end_token
            
    
    def parse_else(self):
        # Iterate through the else statement and extract the contents of the else loop
        else_token = self.current_token
        
        # Check if the next token is an opening parenthesis
        if else_token.type != 'ELSE':
            self.error('Expected "ELSE" keyword')
        
        # Move to the next token
        self.advance()
        
        # Parse the else block
        else_block = self.parse_block()
        
        # Create an ElseNode with the parsed information
        else_node = ElseNode(else_block)
        
        return else_node
    
    def parse_while(self):
        # Iterate through the while statement and extract the contents of the while loop
        while_token = self.current_token
        
        # Check if the next token is an opening parenthesis
        if while_token.type != 'WHILE':
            self.error('Expected "WHILE" keyword')
        
        # Move to the next token
        self.advance()
        
        # Parse the condition expression
        condition = self.parse_expression()
        
        # Check if the next token is a closing parenthesis
        if self.current_token.type != 'RPAREN':
            self.error('Expected ")"')
        
        # Move to the next token
        self.advance()
        
        # Parse the while block
        while_block = self.parse_block()
        
        # Create a WhileNode with the parsed information
        while_node = WhileNode(condition, while_block)
        
        return while_node
    
    def parse_new(self):
        # Iterate through the new statement and extract the contents of the new loop
        new_token = self.current_token
        
        # Check if the next token is an opening parenthesis
        if new_token.type != 'NEW':
            self.error('Expected "NEW" keyword')
        
        # Move to the next token
        self.advance()
        
        # Parse the new block
        new_block = self.parse_block()
        
        # Create a NewNode with the parsed information
        new_node = NewNode(new_block)
        
        return new_node
    
    def parse_for(self):
        
        # Iterate through the for statement and extract the contents of the for loop
        for_token = self.current_token
        
        # Check if the next token is an opening parenthesis
        if for_token.type != 'FOR':
            self.error('Expected "FOR" keyword')
        
        # Move to the next token
        self.advance()
        
        # Parse the for block
        for_block = self.parse_block()
        
        # Create a ForNode with the parsed information
        for_node = ForNode(for_block)
        
        return for_node
    
    def parse_switch(self):
            
            # Iterate through the switch statement and extract the contents of the switch loop
            switch_token = self.current_token
            
            # Check if the next token is an opening parenthesis
            if switch_token.type != 'SWITCH':
                self.error('Expected "SWITCH" keyword')
            
            # Move to the next token
            self.advance()
            
            # Parse the switch block
            switch_block = self.parse_block()
            
            # Create a SwitchNode with the parsed information
            switch_node = SwitchNode(switch_block)
            
            return switch_node
        
    def parse_case(self):
                
                # Iterate through the case statement and extract the contents of the case loop
                case_token = self.current_token
                
                # Check if the next token is an opening parenthesis
                if case_token.type != 'CASE':
                    self.error('Expected "CASE" keyword')
                
                # Move to the next token
                self.advance()
                
                # Parse the case block
                case_block = self.parse_block()
                
                # Create a CaseNode with the parsed information
                case_node = CaseNode(case_block)
                
                return case_node
            
    def parse_default(self):
                        
        # Iterate through the default statement and extract the contents of the default loop
        default_token = self.current_token
        
        # Check if the next token is an opening parenthesis
        if default_token.type != 'DEFAULT':
            self.error('Expected "DEFAULT" keyword')
        
        # Move to the next token
        self.advance()
        
        # Parse the default block
        default_block = self.parse_block()
        
        # Create a DefaultNode with the parsed information
        default_node = DefaultNode(default_block)
        
        return default_node
    
    def parse_break(self):
                                
        # Iterate through the break statement and extract the contents of the break loop
        break_token = self.current_token

        # Check if the next token is an opening parenthesis
        if break_token.type != 'BREAK':
            self.error('Expected "BREAK" keyword')

        # Move to the next token
        self.advance()

        # Parse the break block
        break_block = self.parse_block()

        # Create a BreakNode with the parsed information
        break_node = BreakNode(break_block)

        return break_node   
    
    def parse_block(self):
        # Iterate through the block and extract the contents of the block
        block_token = self.current_token
        
        # Check if the next token is an opening parenthesis
        if block_token.type != 'LBRACKET':
            self.error('Expected "{"')
        
        # Move to the next token
        self.advance()
        
        # Parse the block
        block = self.parse_expression()
        
        # Check if the next token is a closing parenthesis
        if self.current_token.type != 'RBRACKET':
            self.error('Expected "}"')
        
        # Move to the next token
        self.advance()
        
        return block
    
    def parse_identifier(self):
        # Iterate through the identifier and extract the contents of the identifier
        identifier_token = self.current_token
        
        # Check if the next token is an opening parenthesis
        if identifier_token.type != 'IDENTIFIER':
            self.error('Expected "IDENTIFIER"')
        
        # Move to the next token
        self.advance()
        
        # Parse the identifier
        identifier = self.parse_expression()
        
        # Check if the next token is a closing parenthesis
        if self.current_token.type != 'IDENTIFIER':
            self.error('Expected "IDENTIFIER"')
        
        # Move to the next token
        self.advance()
        
        return identifier
    
    def parse_number(self):
        # Iterate through the number and extract the contents of the number
        number_token = self.current_token
        
        # Check if the next token is an opening parenthesis
        if number_token.type != 'NUMBER':
            self.error('Expected "NUMBER"')
        
        # Move to the next token
        self.advance()
        
        # Parse the number
        number = self.parse_expression()
        
        # Check if the next token is a closing parenthesis
        if self.current_token.type != 'NUMBER':
            self.error('Expected "NUMBER"')
        
        # Move to the next token
        self.advance()
        
        return number
    
    def parse_string(self):
        # Iterate through the string and extract the contents of the string
        string_token = self.current_token
        
        # Check if the next token is an opening parenthesis
        if string_token.type != 'STRING':
            self.error('Expected "STRING"')
        
        # Move to the next token
        self.advance()
        
        # Parse the string
        string = self.parse_expression()
        
        # Check if the next token is a closing parenthesis
        if self.current_token.type != 'STRING':
            self.error('Expected "STRING"')
        
        # Move to the next token
        self.advance()
        
        return string
    
    def parse_operator(self):
        # Iterate through the operator and extract the contents of the operator
        operator_token = self.current_token
        
        # Check if the next token is an opening parenthesis
        if operator_token.type != 'OPERATOR':
            self.error('Expected "OPERATOR"')
        
        # Move to the next token
        self.advance()
        
        # Parse the operator
        operator = self.parse_expression()
        
        # Check if the next token is a closing parenthesis
        if self.current_token.type != 'OPERATOR':
            self.error('Expected "OPERATOR"')
        
        # Move to the next token
        self.advance()
        
        return operator
    
    def parse_comment(self):
        # Iterate through the comment and extract the contents of the comment
        comment_token = self.current_token
        
        # Check if the next token is an opening parenthesis
        if comment_token.type != 'COMMENT':
            self.error('Expected "COMMENT"')
        
        # Move to the next token
        self.advance()
        
        # Parse the comment
        comment = self.parse_expression()
        
        # Check if the next token is a closing parenthesis
        if self.current_token.type != 'COMMENT':
            self.error('Expected "COMMENT"')
        
        # Move to the next token
        self.advance()
        
        return comment
    
    def parse_newline(self):
        # Iterate through the newline and extract the contents of the newline
        newline_token = self.current_token
        
        # Check if the next token is an opening parenthesis
        if newline_token.type != 'NEWLINE':
            self.error('Expected "NEWLINE"')
        
        # Move to the next token
        self.advance()
        
        # Parse the newline
        newline = self.parse_expression()
        
        # Check if the next token is a closing parenthesis
        if self.current_token.type != 'NEWLINE':
            self.error('Expected "NEWLINE"')
        
        # Move to the next token
        self.advance()
        
        return newline
    
    def parse_eof(self):
        # Iterate through the eof and extract the contents of the eof
        eof_token = self.current_token
        
        # Check if the next token is an opening parenthesis
        if eof_token.type != 'EOF':
            self.error('Expected "EOF"')
        
        # Move to the next token
        self.advance()
        
        # Parse the eof
        eof = self.parse_expression()
        
        # Check if the next token is a closing parenthesis
        if self.current_token.type != 'EOF':
            self.error('Expected "EOF"')
        
        # Move to the next token
        self.advance()
        
        return eof
    def parse_end_block(self):
        # Iterate through the end of a block and extract the contents
        end_block_token = self.current_token
        
        # Check if the next token is an end of block token
        if end_block_token.type != 'RBRACKET':
            self.error('Expected "}"')
        
        # Move to the next token
        self.advance()
        
        # Parse the end of block
        end_block = self.parse_expression()
        
        # Check if the next token is a closing parenthesis
        if self.current_token.type != 'RBRACE':
            self.error('Expected "}"')
        
        # Move to the next token
        self.advance()
        
        return end_block
        
    def parse_expression(self):
        # Define a dictionary of token types and their corresponding parse methods
        parse_methods = {
            "KEYWORD": self.parse_keyword,
            "IDENTIFIER": self.parse_identifier,
            "NUMBER": self.parse_number,
            "STRING": self.parse_string,
            "OPERATOR": self.parse_operator,
            "COMMENT": self.parse_comment,
            "NEWLINE": self.parse_newline,
            "EOF": self.parse_eof,
            "LBRACKET": self.parse_block,
            "RBRACKET": self.parse_end_block,
            "LBRACE": self.parse_brace,
            "RBRACE": self.parse_brace_end,
        }

        while self.current_token is not None:
            # Get the parse method for the current token type
            parse_method = parse_methods.get(self.current_type)

            if parse_method is not None:
                # Call the parse method
                parse_method()
            else:
                # Raise an error if the token type is not recognized
                self.error(f"Invalid token type: {self.current_type}")

        return self.tokens, self.types
    
    
    

        


def run():
    import os
    import argparse

    # setup argument parser
    args = argparse.ArgumentParser(description="Cubescript to C# transpiler")

    args.add_argument("-o", type=str, nargs="?", help="the output file for the cusp program")
    args.add_argument("input_file", type=str, nargs="?", help="the input file for the cusp program")
    args = args.parse_args()

    # open the file
    file = open(args.input_file, "r") 
    text = file.read()
    file.close()
    
    # create the lexer and parser
    lexer = Lexer(text)
    tokens, types = lexer.lex()
    parser = Parser(tokens, types)
    tokens, types = parser.parse()
    
    # print the tokens and types
    print(tokens)
    print(types)

run()
