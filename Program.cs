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
         
       
        
    }

    public override void EnterAssignment([NotNull] CubeScriptParser.AssignmentContext context)
    {
        
    }

    public override void ExitProgram([NotNull] CubeScriptParser.ProgramContext context)
    {
        Console.WriteLine("ExitProgram");
    }
   
}