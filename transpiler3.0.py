from antlr4 import FileStream, CommonTokenStream
from CubeScriptLexer import CubeScriptLexer
from CubeScriptParser import CubeScriptParser
from CubeScriptVisitor import CubeScriptVisitor

# Read the input from a file
input_stream = FileStream('OpenStudioCLI.cusp')

# Create a lexer and a token stream
lexer = CubeScriptLexer(input_stream)
token_stream = CommonTokenStream(lexer)

# Create a parser and parse the token stream
parser = CubeScriptParser(token_stream)
tree = parser.program()

# reform the tokens back in CSharp language

class MyTranspiler(CubeScriptVisitor):
    def visitProgram(self, ctx):
        # Initialize an empty list to hold the code for each statement
        statements = []

        # Visit each statement in the program
        for i in range(ctx.getChildCount()):
            statement = self.visit(ctx.getChild(i))
            if statement:
                statements.append(statement)

        # Join the statements with newlines and return the result
        return '\n'.join(statements)

    def visitAssignment(self, ctx):
        # Generate code for a CSharp style assignment
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        return f'{name} = {value};'

    def visitExpr(self, ctx):
        # Generate code for a CSharp style expression
        if ctx.getChildCount() == 1:
            # expr: ID
            return ctx.ID().getText()
        elif ctx.getChildCount() == 3:
            # expr: expr op=('*'|'/') expr
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()
            return f'{left} {op} {right}'
        else:
            # expr: '(' expr ')'
            return self.visit(ctx.expr(0))

    def visitIfStatement(self, ctx):
        # Generate code for a CSharp style if statement
        condition = self.visit(ctx.expr())
        block = self.visit(ctx.block())
        return f'if ({condition}) {block}'
    
    def visitIfBlock(self, ctx):
        # Generate code for a CSharp style if statement
        condition = self.visit(ctx.expr())
        block = self.visit(ctx.block())
        return f'if ({condition}) {block}'
    
    def visitWhileBlock(self, ctx):
        # Generate code for a CSharp style if statement
        condition = self.visit(ctx.expr())
        block = self.visit(ctx.block())
        return f'while ({condition}) {block}'
    
    def visitForBlock(self, ctx):
        # Generate code for a CSharp style if statement
        condition = self.visit(ctx.expr())
        block = self.visit(ctx.block())
        return f'for ({condition}) {block}'
    
    def visitForeachBlock(self, ctx):
        # Generate code for a CSharp style if statement
        condition = self.visit(ctx.expr())
        block = self.visit(ctx.block())
        return f'foreach ({condition}) {block}'
    
    def visitFunctiondefinition(self, ctx):
        # Generate code for a CSharp function
        
        # Get the function name
        name = ctx.IDENTIFIER().getText()
        
        # Get the function parameters
        params = []
        for param in ctx.param():
            param_str = self.visit(param)
            params.append(param_str)
            
        # Get the function body
        body = self.visit(ctx.block())
        
        # Generate the function definition
        params = ', '.join(params)
        return f'public static void {name}({params}) {body}'

    def visitParam(self, ctx):
        # Generate code for a CSharp function parameter
        param = ctx.IDENTIFIER().getText()
        return param

    def visitBlock(self, ctx):
        # Generate code for a CSharp block
        statements = []
        for i in range(ctx.getChildCount()):
            statement = self.visit(ctx.getChild(i))
            if statement:
                statements.append(statement)
        statements = '\n'.join(statements)
        return f'{{\n{statements}\n}}'

    def visitFunctionCall(self, ctx):
        # Generate code for a CSharp function call
        name = ctx.IDENTIFIER().getText()
        args = []
        for arg in ctx.expr():
            arg_str = self.visit(arg)
            if arg_str:
                args.append(arg_str)
        args = ', '.join(args)
        return f'{name}({args})'
    
    def visitUsingStatement(self, ctx: CubeScriptParser.UsingStatementContext):
        # Generate code for a CSharp using statement with support for importing multiple layers, like using System.collections.generic;
        
        # Get the namespace name
        name = ctx.IDENTIFIER()[0].getText()
        
        # Get the namespace parameters
        params = []
        for param in ctx.IDENTIFIER():
            param_str = self.visit(param)
            if param_str:
                params.append(param_str)
            
        # Generate the namespace definition
        params = '.'.join(params)
        return f'using {name}.{params};'
        
        
    
    
def main():
    # Create a visitor and visit the tree
    visitor = MyTranspiler()
    code = visitor.visit(tree)
    print(code)


main()


""" g4 grammer for the Programming language for reference
    grammar CubeScript;

program: line* EOF;

line: statement | ifBlock | whileBlock expression | Comment;

statement : assignment #assignmentexpr
    //import statement
    | IMPORT IDENTIFIER ';' #importstatement
    | IMPORT IDENTIFIER '.' IDENTIFIER ';' #importstatement
    //namespace statement
    | 'house' IDENTIFIER block #namespacestatement
    | 'room' IDENTIFIER block #classstatement

    //function
    |functiondefinition #functiondefine

    //for blank > blank
    | 'for' '(' IDENTIFIER '>' IDENTIFIER')' block #forloop
    //for blank < blank
    | 'for' '(' IDENTIFIER '<' IDENTIFIER')' block #forloop
    // function calls within varible assignment
    | TYPE IDENTIFIER '=' functionCall ';' #variblecallexprs
    //function calls
    | functionCall ';' #functionCallexprrr
    | 'switch' '(' expression ')' '{' (switchCase | defaultCase)* '}' #switchblockexprs
    //varibles
    | IDENTIFIER '=' expression ';' #varibleexpr
    //varibles with type
    | TYPE IDENTIFIER '=' expression ';' #varibleexpr
    | TYPE IDENTIFIER '=' functionCall ';' #varibleexpr
    // function calls  within varible assignmnt
    | TYPE IDENTIFIER '=' functionCall ';' #variblecallexprz
    | TYPE IDENTIFIER '=' functionCall '.' IDENTIFIER ';' #variblecallexprz
    //varibles with type and array
    | TYPE IDENTIFIER ARRAY '=' expression ';' #varibleexpr
    //varibles with type and array
    | TYPE IDENTIFIER ARRAY '=' functionCall ';' #varibleexpr
    //varibles with type and array
    | TYPE IDENTIFIER ARRAY '=' '[' (expression (',' expression)*)? ']' ';' #varibleexpr

    //array definition
    | IDENTIFIER ARRAY '=' '[' (expression (',' expression)*)? ']' ';' #arraydefinition
    //array definition
    | IDENTIFIER ARRAY '=' functionCall ';' #arraydefinition

    //function calls within varible assignment
    | TYPE IDENTIFIER '=' functionCall ';' #variblecallexprs
    //function calls
    //varibles
    | IDENTIFIER '=' functionCall ';' #varibleexpr
    //varibles with type
    | TYPE IDENTIFIER '=' functionCall ';' #varibleexpr
    //varibles with type and array
    | TYPE IDENTIFIER ARRAY '=' functionCall ';' #varibleexpr
    // for loop with optional identifiers
    //array string{} thing = function call
    | IDENTIFIER? TYPE IDENTIFIER? ARRAY? '=' functionCall ';' #stringarray
    //array definition
    | IDENTIFIER? constant? IDENTIFIER? ARRAY? '=' '[' (expression (',' expression)*)? ']' ';' #arraydefinition
    |'struct' IDENTIFIER block #structstatement
    ;
switchBlock: 'switch' '(' expression* ')' '{' (switchCase | defaultCase)* '}';
defaultCase: 'bland' ':' statement* 'stop;' ';';
switchCase: 'at' expression ':' statement* 'stop;';
ifBlock: 'if' expression block ('else' elseifBlock)?;
ifStatement: 'if' '(' expression ')' block ('else' block)?;
elseifBlock: block | ifBlock;
forBlock: 'for' '(' assignment ';' expression ';' assignment ')' block;
foreachBlock: 'foreach' '(' IDENTIFIER 'in' IDENTIFIER ')' block;

incrementOp: '++';
decrementOp: '--';

modifier: 'public' | 'private' | 'protected' | 'static';
funcdef: 'struct' | 'function' | 'void' | 'pubtask' | 'pubbool' | 'pubstring' | 'pubint' | 'pubfloat' | 'pubvoid' | 'task' ;

forInit: (TYPE IDENTIFIER '=' expression) | (IDENTIFIER '=' expression);
forUpdate: IDENTIFIER (incrementOp | decrementOp);
//while block with support for switch statements and other things
whileBlock: WHILE '(' expression ')' block;
functiondefinition:  modifier? 'struct' IDENTIFIER '(' (param (',' param)*)? ')' block;

// CSharp like params
param: TYPE IDENTIFIER | TYPE IDENTIFIER ARRAY | TYPE IDENTIFIER ARRAY '=' expression | TYPE IDENTIFIER '=' expression | TYPE IDENTIFIER '=' functionCall | TYPE IDENTIFIER '=' functionCall;

WHILE: 'while' | 'until';
assignment: IDENTIFIER '=' expression;

//function call with support for . using CSharp syntax
functionCall: IDENTIFIER '(' (expression (',' expression)*)? ')' #functionCallexprr
    | IDENTIFIER '.' IDENTIFIER '(' (expression (',' expression)*)? ')' #functionCallexprr
    // function calls within varible assignment
    | TYPE IDENTIFIER '=' IDENTIFIER '(' (expression (',' expression)*)? ')' ';' #variblecallexpr
    | IDENTIFIER '(' (expression (',' expression)*)? ')' '.' IDENTIFIER #functionCallexprr;

ARRAY: '['|']'|'{'|'}';
block: '{' line* '}';
expression
    : constant #constantexpr
    | functionCall #functionCallexpr
    | '(' expression ')' #parenthesisexpr
    | IDENTIFIER #identifiereexpr
    //binary expressions
    | expression multOp expression #binaryexpr
    | expression addOp expression #binaryexpr
    | expression cmpOp expression #binaryexpr
    | expression boolOp expression #binaryexpr
    //negation
    | '-' expression #negationexpr
    | '!' expression #negationexpr
    | expression '?' expression ':' expression #ternaryexpr
    //varibles
    | expression '.' IDENTIFIER #dotexpr
    | expression '.' IDENTIFIER '(' (expression (',' expression)*)? ')' #dotfunctionCallexprs
    //array
    | expression '[' expression? ']' #arrayexpr
    | expression '{' expression ?'}' #arrayexpr
    
    // expression++ and expression--
    | expression '++' #incrementexpr
    | expression '--' #decrementexpr
    // identifier++ and identifier--
    | IDENTIFIER '++' #incrementexpr
    | IDENTIFIER '--' #decrementexpr
    //constant++ and constant--
    | constant '++' #incrementexpr
    | constant '--' #decrementexpr
    //array 
    | expression '[' expression? ']' '=' expression #arrayassignment
    | expression '[' expression? ']' '=' functionCall #arrayassignment
    | expression '{' expression ?'}' '=' expression #arrayassignment
    | expression '{' expression* ?'}' '=' functionCall #arrayassignment
    //varibles in functions
    | IDENTIFIER '.' IDENTIFIER #dotexpr
    | IDENTIFIER '.' IDENTIFIER '(' (expression (',' expression)*)? ')' #dotfunctionCallexprs
    //varibles
    | IDENTIFIER #identifiereexpr
    | IDENTIFIER '(' (expression (',' expression)*)? ')' #functionCallexprs
    | IDENTIFIER '(' (expression (',' expression)*)? ')' '.' IDENTIFIER #functionCallexprs
    | IDENTIFIER '(' (expression (',' expression)*)? ')' '.' IDENTIFIER '(' (expression (',' expression)*)? ')' #functionCallexprs
    | IDENTIFIER '(' (expression (',' expression)*)? ')' '.' IDENTIFIER '(' (expression (',' expression)*)? ')' '.' IDENTIFIER #functionCallexprs

    //functions
    | functionCall #functionCallexpr
    | functionCall '.' IDENTIFIER #functionCallexpr
    | functionCall '.' IDENTIFIER '(' (expression (',' expression)*)? ')' #functionCallexpr
    | functionCall '.' IDENTIFIER '(' (expression (',' expression)*)? ')' '.' IDENTIFIER #functionCallexpr
    | functionCall '.' IDENTIFIER '(' (expression (',' expression)*)? ')' '.' IDENTIFIER '(' (expression (',' expression)*)? ')' #functionCallexpr
    | functionCall '.' IDENTIFIER '(' (expression (',' expression)*)? ')' '.' IDENTIFIER '(' (expression (',' expression)*)? ')' '.' IDENTIFIER #functionCallexpr
    //statements 
    | statement #statementexpr
    //if statements
    | ifStatement #ifstatementexpr
    //switch statements
    | switchBlock #switchblockexpr
    //while statements
    | whileBlock #whileblockexpr
    //for statements    
    | forBlock #forblockexpr
    //foreach statements
    | foreachBlock #foreachblockexpr
    

        
    // foreach block
    | 'for' '(' IDENTIFIER '>' IDENTIFIER ')' block #foreachblockexpr
    // function start and end
    | 'struct' IDENTIFIER '(' (param (',' param)*)? ')' block #functiondefineexpr
    ;
Comment
  :  ('//' ~( '\r' | '\n' )*
    |  '/*' .*? '*/'
      |  '#' ~( '\r' | '\n' )*)
      -> skip
  ;  
multOp: '*' | '/' | '%' | '^' | '<<' | '>>' |'&' | '|' | '&&' | '||' | '='| '+=' | '-=' | '*='; 
addOp: '+' | '-'; 
cmpOp: '<' | '>' | '<=' | '>=' | '==' | '!='; 
boolOp: BOOL_OPERATOR;
//array definition
BOOL_OPERATOR: 'and' | 'or' | 'xor';
constant : INTEGER | FLOAT | STRING | BOOL | IDENTIFIER| TYPE;
INTEGER: [0-9]+;
FLOAT: [0-9]* '.' [0-9]+;
fragment ESC: '\\' (["\\/bfnrt] | UNICODE);
fragment UNICODE: 'u' HEX HEX HEX HEX;
fragment HEX: [0-9a-fA-F];
fragment SAFE: ~["\\\u0000-\u001F];
IMPORT: 'using' | '*include' | 'import' ;
STRING: '"' (ESC | SAFE)* '"';
BOOL: 'true' | 'false';
TYPE: 'string' | 'int' | 'float' | 'bool' | 'null'| 'string[]'|'int[]' | 'float[]' | 'bool[]' | 'null[]';



WS: [ \t\r\n]+ -> skip;



IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
    """
