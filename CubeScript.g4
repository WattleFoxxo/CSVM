grammar CubeScript;

program: line* EOF;

line: statement | ifBlock | whileBlock;

statement : assignment #assignmentexpr
    | 'using' IDENTIFIER? ('.' IDENTIFIER?)* ';' #importstatement
    | 'for' '(' IDENTIFIER?  expression  IDENTIFIER? ')' block #forstatement
    | 'struct' IDENTIFIER? '(' IDENTIFIER? (',' IDENTIFIER?)* ')' '{' line* '}' #functioncallstatment
    | 'struct' IDENTIFIER? '(' TYPE? (',' TYPE?)* ')' '{' line* '}' #functioncallstatement
    | 'for' '(' IDENTIFIER? '>' expression? ')' block #foreachstatement
    | functionCall ';'#functioncallstatement
    | TYPE IDENTIFIER? '=' expression ';' #varibledeclaration
    // array string{} thing = function call
    | IDENTIFIER? 'string' IDENTIFIER? ARRAY? '=' functionCall ';' #stringarray
    | 'string' IDENTIFIER? ARRAY? '=' STRING ';' #stringarray
    | IMPORT? IDENTIFIER? ';' #importstatement
    // IMPORT with any amount of . and identifiers
    | 'return' expression ';' #returnstatement
    | 'break' ';' #breakstatement
    | 'continue' ';' #continuestatement
    | 'house' ':' IDENTIFIER?  #housestatement
    // for loop with optional identifiers
    //array string{} thing = function call
    | IDENTIFIER? TYPE IDENTIFIER? ARRAY? '=' functionCall ';' #stringarray
    //array definition
    | IDENTIFIER? constant? IDENTIFIER? ARRAY? '=' '[' (expression (',' expression)*)? ']' ';' #arraydefinition
    ;
ifBlock: 'if' expression block ('else' elseifBlock)?;

elseifBlock: block | ifBlock;

whileBlock: WHILE expression block ('else' elseifBlock)?;


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
    
    | IDENTIFIER constant '=' expression #varibleassignment
    | IDENTIFIER #identifierexpression
    | functionCall #functioncallexpr
    | '(' expression ')' #parenthesisexpr
    | '!' expression #notexpr
    | expression multOp expression #multexpr
    | expression addOp expression #addexpr
    | expression cmpOp expression #cmpexpr
    | expression boolOp expression #boolexpr
    | expression '?' expression ':' expression #ternaryexpr
    | expression '[' expression ']' #arrayexpr
    | expression '.' IDENTIFIER #dotexpr
    | expression '.' IDENTIFIER? '('? (expression (',' expression)*)? ')'? #dotfunctioncallexprs
    | expression '.' IDENTIFIER? '('? (expression (',' expression)*)? ')'? '.'? IDENTIFIER? #dotfunctioncallexprs
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