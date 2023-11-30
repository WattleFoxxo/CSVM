grammar CubeScript;

program: line* EOF;

line: statement | ifBlock | whileBlock expression | Comment | usingStatement;

statement : assignment #assignmentexpr
    //import statement
    | usingStatement #usingstatement
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

//using statements with infinite support for . using CSharp syntax
usingStatement: IMPORT IDENTIFIER ('.' IDENTIFIER)* ';';


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