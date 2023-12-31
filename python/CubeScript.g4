grammar CubeScript;

program: line* EOF;

line: statement | ifBlock | whileBlock expression | Comment | usingStatement| returnstatement;

statement : assignment #assignmentexp

| functionCall #functionCallExp
| ifBlock #ifblockexp
| whileBlock #whileblockexp
| forBlock #forblockexp
| break #breakexp
| returnstatement #returnstatementexp
| expression #expressionexp
| Comment #commentexp
| usingStatement #usingStatementexp
| importStatement #importStatementexp
| includeStatement #includeStatementexp
| arrayDeclaration #arrayDeclarationexp
| switchBlock #switchBlockexp
| functionblock #functionblockexp
;
//assignment
assignment: IDENTIFIER '=' expression ';';

//if block
ifBlock: IF '(' expression ')' '{' line* '}' (ELSE '{' line* '}')?;

//while block
whileBlock: WHILE '(' expression ')' '{' line* '}';


parameterList: TYPE IDENTIFIER (',' TYPE IDENTIFIER)*;

//function body
functionBody: line*;


//function call
functionCall: 
    IDENTIFIER '(' (expression (',' expression)*)? ')' ';'
    | 'struct' IDENTIFIER '(' (parameterList)? ')' '{' functionBody '}'
    ;

//for block
forBlock: FOR '(' expression '>' expression ')' '{' line* '}';

//code block
codeBlock: '{' line* '}';
functionblock: STATES? IDENTIFIER '(' (TYPE IDENTIFIER (',' TYPE IDENTIFIER)*)? ')' codeBlock;


//return statement
returnstatement: RETURN expression ';';

//import, include, using statement
importStatement: IMPORT (IDENTIFIER '.')* IDENTIFIER ';';

//include statement
includeStatement: IMPORT (IDENTIFIER '.')* IDENTIFIER ';';

//array declaration
arrayDeclaration: TYPE IDENTIFIER '{' (expression (',' expression)*)? '}';

//using statement
usingStatement: IMPORT (IDENTIFIER '.')* IDENTIFIER ';';

expression: assignment 
| functionCall 
| ifBlock 
| whileBlock 
| forBlock 
| break 
| returnstatement 
| Comment 
| usingStatement 
| importStatement 
| includeStatement 
| arrayDeclaration
| constant

| expression multOp expression
| expression addOp expression
| expression cmpOp expression
| expression boolOp expression
| '(' expression ')'
| expression '?' expression ':' expression
| expression '[' expression ']'
| expression '.' IDENTIFIER
| expression '(' (expression (',' expression)*)? ')'
| expression '++'
| expression '--'
| '++' expression
| '--' expression
| '!' expression
| '-' expression
| '+' expression
| 'new' IDENTIFIER '(' (expression (',' expression)*)? ')'
| 'new' IDENTIFIER '[' expression ']'
| 'new' IDENTIFIER '[' expression ']' '{' (expression (',' expression)*)? '}'
| 'new' IDENTIFIER '[' expression ']' '{' (expression (',' expression)*)? '}' '{' (expression (',' expression)*)? '}'

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
break: 'stop;'; 
WHILE: 'while';
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
SWITCH: 'switch';
CASE: 'at';
DEFAULT: 'bland';
STATES: 'public' | 'private' | 'protected' | 'static' | 'struct';
switchBlock: SWITCH '(' expression ')' '{' switchCase* defaultCase? '}';
switchCase: CASE constant ':' line*;
defaultCase: DEFAULT ':' line*;


WS: [ \t\r\n]+ -> skip;



IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;