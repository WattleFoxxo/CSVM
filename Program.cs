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
         //grab everything in the function call
        string functioncall = context.GetText();
        //split the function call into an array
        string[] functioncallarray = functioncall.Split(' ');
        //grab the function name
        string functionname = functioncallarray[0];
        //grab the function arguments
        string functionargs = functioncallarray[1];
        //split the function arguments into an array
        string[] functionargsarray = functionargs.Split(',');
        //grab the function body
        string functionbody = FunctionBody[functionname].ToString();
        //split the function body into an array
        string[] functionbodyarray = functionbody.Split('\n');
        //grab the function variables
        string functionvariables = FunctionVariables[functionname].ToString();
        //split the function variables into an array
        string[] functionvariablesarray = functionvariables.Split(',');
        //grab the function code
        string functioncode = "";
        //loop through the function body array
        foreach (string line in functionbodyarray)
        {
            //loop through the function variables array
            foreach (string variable in functionvariablesarray)
            {
                //if the line contains the variable
                if (line.Contains(variable))
                {
                    //replace the variable with the argument
                    functioncode += line.Replace(variable, functionargsarray[Array.IndexOf(functionvariablesarray, variable)]) + "\n";
                }
            }
        }
        //split the function code into an array
        string[] functioncodearray = functioncode.Split('\n');
        //loop through the function code array
        foreach (string line in functioncodearray)
        {
            //add the line to the converted code array
            ConvertedCode.Add(line);
        }

        //print the converted code
        foreach (string line in ConvertedCode)
        {
            Console.WriteLine(line);
        }
       
        
    }

    public override void EnterAssignment([NotNull] CubeScriptParser.AssignmentContext context)
    {
        
    }

    public override void ExitProgram([NotNull] CubeScriptParser.ProgramContext context)
    {
        Console.WriteLine("ExitProgram");
    }
   
}