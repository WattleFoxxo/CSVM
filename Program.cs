using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using System;
using Antlr4.Runtime;
using Antlr4.Runtime.Tree;
using Antlr4.Runtime.Misc;
using System.Collections.Generic;
using System.Linq;
using static Protogram.CubeScriptVisitor;
using System.Text;
using System.Threading.Tasks;
using System.Reflection;
using System.IO;

namespace Protogram;

public class MyListener : CubeScriptBaseListener
{
    //varibles array
    public Dictionary<string, object?> Varibles { get; set; } = new();

    //function array
    public List<string?> Functions { get; set; } = new();
    public Dictionary<string, object?> FunctionBody { get; set; } = new();
    public Dictionary<string, object?> FunctionVariables { get; set; } = new();
    public List<string> codeName { get; set; } = new();

    public List<string> FunctionName { get; set; } = new();

    //converted code array?
    public List<string> ConvertedCode { get; set; } = new();

    //loaded assemblies array
    public List<Assembly> LoadedAssemblies { get; set; } = new();

    public List<string> finishedvar { get; set; } = new();

    //function name
    static void Main(string[] args)
    {
        // Get the path to the CubeScript code file
        string filePath = "trial2.cusp";

        // create a stream of your input code
        var inputStream = new AntlrInputStream(File.ReadAllText(filePath));

        // create a lexer that reads from the input stream
        var lexer = new CubeScriptLexer(inputStream);

        // create a token stream from the lexer
        var tokenStream = new CommonTokenStream(lexer);

        // create a parser that reads from the token stream
        var parser = new CubeScriptParser(tokenStream);

        // call the appropriate method on the parser to parse your input code
        var tree = parser.program();

        // create an instance of your listener class
        var listener = new MyListener();

        // traverse the parse tree using the listener
        var walker = new ParseTreeWalker();
        walker.Walk(listener, tree);

        string finishedcode = "";
foreach (string line in listener.ConvertedCode)
{
    finishedcode += line + "\n";
}

string[] lines = finishedcode.Split('\n');
foreach (string line in lines)
{
  Console.WriteLine(line);
}
       

    }

    public override void EnterProgram([NotNull] CubeScriptParser.ProgramContext context)
    {
        Console.WriteLine("EnterProgram");
    }


    public override void EnterBlock([NotNull] CubeScriptParser.BlockContext context)
    {
       
    }
    public override void EnterFunctioncallexprs([NotNull] CubeScriptParser.FunctioncallexprsContext context)
    {
         //strip the entire function call
        string functioncall = context.GetText();
        //since the lines are seperated by ; we can split the function call by ;
        string[] lines = functioncall.Split(';');
        //put a space between the =
        string[] lines2 = lines[0].Split('=');
        //add the function call to the converted code array
      Console.WriteLine(lines2[0].ToString());
       
        
    }

    public override void EnterAssignment([NotNull] CubeScriptParser.AssignmentContext context)
    {
        //strip the entire assignment
        string assignment = context.GetText();
        //since the lines are seperated by ; we can split the assignment by ;
        string[] lines = assignment.Split(';');
        //put a space between the =
        string[] lines2 = lines[0].Split('=');
        //add the assignment to the converted code array
        ConvertedCode.Add(lines2[0].ToString() + " = " + lines2[1].ToString());
    }

    public override void ExitProgram([NotNull] CubeScriptParser.ProgramContext context)
    {
        Console.WriteLine("ExitProgram");
    }
    /*
    antlr grammer file
    
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
    |  '/*' .*? '* /'
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
    */
}