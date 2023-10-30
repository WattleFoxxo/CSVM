grammar CubeScript;

program: line* EOF;

line: statement | ifBlock | whileBlock expression | Comment;

statement : assignment #assignmentexpr
    //import statement
    | IMPORT IDENTIFIER ';' #importstatement
    | IMPORT IDENTIFIER '.' IDENTIFIER ';' #importstatement
    //namespace statement
    | 'house:' IDENTIFIER '{' line* '}' #namespacestatement
    //function
    |functiondefinition #functiondefine
    
    //for blank > blank
    | 'for' '(' IDENTIFIER '>' IDENTIFIER')' block #forloop
    //for blank < blank
    | 'for' '(' IDENTIFIER '<' IDENTIFIER')' block #forloop
    // function calls within varible assignment
    | TYPE IDENTIFIER '=' functionCall ';' #variblecallexpr
    //function calls
    | functionCall ';' #functioncallexprr
    //varibles
    | IDENTIFIER '=' expression ';' #varibleexpr
    //varibles with type
    | TYPE IDENTIFIER '=' expression ';' #varibleexpr


    
    

    // for loop with optional identifiers
    //array string{} thing = function call
    | IDENTIFIER? TYPE IDENTIFIER? ARRAY? '=' functionCall ';' #stringarray
    //array definition
    | IDENTIFIER? constant? IDENTIFIER? ARRAY? '=' '[' (expression (',' expression)*)? ']' ';' #arraydefinition
    ;
ifBlock: 'if' expression block ('else' elseifBlock)?;

elseifBlock: block | ifBlock;

whileBlock: WHILE expression block ('else' elseifBlock)?;
functiondefinition: 'struct' IDENTIFIER '(' (IDENTIFIER (',' IDENTIFIER)*)? ')' block;

WHILE: 'while' | 'until';
assignment: IDENTIFIER '=' expression;

//function call with support for . 
functionCall: IDENTIFIER '(' (expression (',' expression)*)? ')' #functioncallexprs
    | IDENTIFIER '.' IDENTIFIER '(' (expression (',' expression)*)? ')' #functioncallexprs
    ;
ARRAY: '['|']'|'{'|'}';


block: '{' line* '}';
expression
    : constant #constantexpr
    | functionCall #functioncallexpr
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
    | expression '.' IDENTIFIER '(' (expression (',' expression)*)? ')' #dotfunctioncallexprs
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
    | IDENTIFIER '.' IDENTIFIER '(' (expression (',' expression)*)? ')' #dotfunctioncallexprs

        
    // foreach block 
    
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
constant : INTEGER | FLOAT | STRING | BOOL | NULL| IDENTIFIER| TYPE;
INTEGER: [0-9]+;
FLOAT: [0-9]* '.' [0-9]+;
fragment ESC: '\\' (["\\/bfnrt] | UNICODE);
fragment UNICODE: 'u' HEX HEX HEX HEX;
fragment HEX: [0-9a-fA-F];
fragment SAFE: ~["\\\u0000-\u001F];
IMPORT: 'using' | '*include' | 'import' ;
STRING: '"' (ESC | SAFE)* '"';
BOOL: 'true' | 'false';
TYPE: 'string' | 'int' | 'float' | 'bool' | 'null';
NULL: 'null';


WS: [ \t\r\n]+ -> skip;



IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;