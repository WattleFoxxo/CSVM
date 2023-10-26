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
        Console.WriteLine("Finished Code: \n");
        foreach (string line in lines)
        {
            
            Console.WriteLine(line);
        }
        

    }

    public override void EnterProgram([NotNull] CubeScriptParser.ProgramContext context)
    {
        Console.WriteLine("EnterProgram \n");

        //get the program
        string program = context.GetText();
        //split the lines after the word struct
        string[] lines = program.Split('\n');
        int startIndex = 0;
        string word = "struct";
        while (startIndex < program.Length)
        {
            int wordIndex = program.IndexOf(word, startIndex);
            if (wordIndex == -1)
            {
                break;
            }

            int nextWordIndex = program.IndexOf(word, wordIndex + word.Length);
            if (nextWordIndex == -1)
            {
                nextWordIndex = program.Length;
            }

            int start = wordIndex;
            while (start > 0 && !char.IsWhiteSpace(program[start - 1]))
            {
                start--;
            }

            int end = nextWordIndex;
            while (end < program.Length && !char.IsWhiteSpace(program[end]))
            {
                end++;
            }

            string result = program.Substring(start, end - start);
            if (result.EndsWith("<EOF>"))
            {
                result = result.Substring(0, result.Length - "<EOF>".Length);
            }
            Console.WriteLine(result);

            startIndex = end;


            //switch each statement within the result
            switch (result)
            {
                case "struct":
                    //get the struct name
                    string[] structname = result.Split(' ');
                    string name = structname[1];
                    //add the struct name to the code
                    ConvertedCode.Add("public static void " + name + "()");
                    break;
                case "var":
                    //get the var name
                    string[] varname = result.Split(' ');
                    string var = varname[1];
                    //add the var name to the code
                    ConvertedCode.Add("public " + var + ";");
                    break;
                case "function":
                    //get the function name
                    string[] functionname = result.Split(' ');
                    string func = functionname[1];
                    //add the function name to the code
                    ConvertedCode.Add("public void " + func + "()");
                    break;
                case "end":
                    //add the end to the code
                    ConvertedCode.Add("}");
                    break;
                case "if":
                    //get the if statement
                    string[] ifstatement = result.Split(' ');
                    string ifstate = ifstatement[1];
                    //add the if statement to the code
                    ConvertedCode.Add("if (" + ifstate + ")");
                    break;
                case "else":
                    //add the else statement to the code
                    ConvertedCode.Add("else");
                    break;

            }

        }
    }


    public override void EnterBlock([NotNull] CubeScriptParser.BlockContext context)
    {
        Console.WriteLine("EnterBlock \n");
        // get the block
        string block = context.GetText();
        Console.WriteLine(block);
        Console.WriteLine("exitBlock \n");
    }
    public override void EnterFunctioncallexprs([NotNull] CubeScriptParser.FunctioncallexprsContext context)
    {
        Console.WriteLine("EnterFunctioncallexprs \n");
        //grab everything in the function call
        string functioncall = context.GetText();
        //split the function call into an array
        Console.WriteLine(functioncall);
        Console.WriteLine("exitFunctioncallexprs \n");


    }

    public override void EnterAssignment([NotNull] CubeScriptParser.AssignmentContext context)
    {
        Console.WriteLine("EnterAssignment");
        string assignment = context.GetText();
        //take each assignment and add var at the start of the line
        string[] lines = assignment.Split('\n');
        foreach (string line in lines)
        {
            if (line.Contains("="))
            {
                //get the first part of the line and add var to it
                string[] parts = line.Split('=');
                string varname = parts[0];
                string varvalue = parts[1];
                string newvar = "var " + varname + " = " + varvalue;
                finishedvar.Add(newvar);
                Console.WriteLine(newvar);
            }
        }
        Console.WriteLine("exitAssignment \n");

    }

    public override void ExitProgram([NotNull] CubeScriptParser.ProgramContext context)
    {
        Console.WriteLine("ExitProgram \n");
    }

}