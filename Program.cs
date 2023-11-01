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
using Antlr4.Runtime.Sharpen;
using Antlr4.Runtime.Atn;
using Antlr4.Runtime.Dfa;


namespace Protogram;

public class MyListener : CubeScriptBaseListener, IAntlrErrorListener<int>
{
    //varibles array
    public Dictionary<string, object?> Varibles { get; set; } = new();

    //function array
    public List<string?> Functions { get; set; } = new();
    public Dictionary<string, object?> FunctionBody { get; set; } = new();
    public Dictionary<string, object?> FunctionVariables { get; set; } = new();
    public List<string> codeName { get; set; } = new();
public string? newvar { get; set; }
public string? truevar { get; set; }
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
        //split the program into an array of strings
        string[] lines = program.Split('\n');

        foreach (string line in lines)
        {
            //perform the same logic as before for each line
            int startIndex = 0;
            string word = "struct";
            while (startIndex < line.Length)
            {
                int wordIndex = line.IndexOf(word, startIndex);
                if (wordIndex == -1)
                {
                    break;
                }

                int nextWordIndex = line.IndexOf(word, wordIndex + word.Length);
                if (nextWordIndex == -1)
                {
                    nextWordIndex = line.Length;
                }

                int start = wordIndex;
                while (start > 0 && !char.IsWhiteSpace(line[start - 1]))
                {
                    start--;
                }

                int end = nextWordIndex;
                while (end < line.Length && !char.IsWhiteSpace(line[end]))
                {
                    end++;
                }

                string result = line.Substring(start, end - start);
                if (result.EndsWith("<EOF>"))
                {
                    result = result.Substring(0, result.Length - "<EOF>".Length);
                }


                startIndex = end;

                foreach (string results in lines)
                {
                    // Split the line into words
                    string[] words = results.Split(' ');

                    foreach (string wordz in words)
                    {
                        // Perform logic on each word
                        switch (wordz)
                        {
                            case "struct":
                                //get the struct name
                                string[] structname = wordz.Split(' ');
                                string name = structname[1];
                                //add the struct name to the code
                                ConvertedCode.Add("public static void " + name + "()");
                                break;
                            case "var":
                                //get the var name
                                string[] varname = wordz.Split(' ');
                                string var = varname[1];
                                //add the var name to the code
                                ConvertedCode.Add("public " + var + ";");
                                break;
                            case "function":
                                //get the function name
                                string[] functionname = wordz.Split(' ');
                                string func = functionname[1];
                                //add the function name to the code
                                ConvertedCode.Add("public void " + func + "()");
                                break;
                            case "}":
                                //add the end to the code
                                ConvertedCode.Add("}");
                                break;
                            case "if":
                                //get the if statement
                                string[] ifstatement = wordz.Split(' ');
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
                for (int i = startIndex; i < end; i++)
                {

                    Console.WriteLine(lines[i]);
                    Console.WriteLine("exitProgram \n");
                    // perform logic on each line
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
                        case "}":
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

                //switch each statement within the result
                Console.WriteLine("exitProgram \n");
            }
        }
    }

    public override void EnterIdentifiereexpr(CubeScriptParser.IdentifiereexprContext context)
    {
        var varName = context.IDENTIFIER().GetText();
        if (!Varibles.ContainsKey(varName))
        {
            throw new Exception($"varible {varName} is not defined");
        }


    }
    public override void EnterForloop([NotNull] CubeScriptParser.ForloopContext context)
    {
        
        //process the for loop
        Console.WriteLine("EnterForloop \n");
        //get the for loop
        string forloop = context.GetText();
        //get the contents of the for loop
        string forloopcontents = forloop.Substring(forloop.IndexOf("{") + 1, forloop.IndexOf("}") - forloop.IndexOf("{") - 1);
        //add var from the = 
        string[] linesz = forloopcontents.Split('\n');
        foreach (string linez in linesz)
        {
            if (linez.Contains("="))
            {
                //get the first part of the line and add var to it
                string[] parts = linez.Split('=');
                string varname = parts[0];
                string varvalue = parts[1];
                newvar = "var " + varname + " = " + varvalue;
                finishedvar.Add(newvar);
                Console.WriteLine(newvar);
            }
        }
        //split the for loop into an array
        string[] lines = forloop.Split('\n');
        foreach (string line in lines)
        {
            //perform the same logic as before for each line
            int startIndex = 0;
            string word = "for";
            while (startIndex < line.Length)
            {
                int wordIndex = line.IndexOf(word, startIndex);
                if (wordIndex == -1)
                {
                    break;
                }

                int nextWordIndex = line.IndexOf(word, wordIndex + word.Length);
                if (nextWordIndex == -1)
                {
                    nextWordIndex = line.Length;
                }

                int start = wordIndex;
                while (start > 0 && !char.IsWhiteSpace(line[start - 1]))
                {
                    start--;
                }

                int end = nextWordIndex;
                while (end < line.Length && !char.IsWhiteSpace(line[end]))
                {
                    end++;
                }

                string result = line.Substring(start, end - start);
                if (result.EndsWith("<EOF>"))
                {
                    result = result.Substring(0, result.Length - "<EOF>".Length);
                }
                startIndex = end;


                foreach (char linez in result.ToString())
                {
                    // Split the line into words
                    string[] words = linez.ToString().Split(' ');

                    foreach (string wordz in words)
                    {
                        // Perform logic on each word
                        try
                        {

                        switch (wordz)
                        {
                            case "for":
                                //get the for loop
                                string[] forloopname = wordz.Split(' ');
                                string forloopz = forloopname[1];
                                //add the for loop to the code
                                ConvertedCode.Add("for (" + forloopz + ")");
                                break;
                            case "var":
                                //get the var name
                                string[] varname = wordz.Split(' ');
                                string var = varname[1];
                                //add the var name to the code
                                ConvertedCode.Add("public " + var + ";");
                                break;
                            case "function":
                                //get the function name
                                string[] functionname = wordz.Split(' ');
                                string func = functionname[1];
                                //add the function name to the code
                                ConvertedCode.Add("public void " + func + "()");
                                break;
                            case "}":
                                //add the end to the code
                                ConvertedCode.Add("}");
                                break;
                            case "{":
                                //add the start to the code
                                ConvertedCode.Add("{" + newvar?.ToString());
                                break;
                            case "(":
                                //add the start to the code
                                ConvertedCode.Add("(" + truevar?.ToString());
                                break;
                            case ")":
                                //add the end to the code
                                ConvertedCode.Add(")");
                                break;
                             
                            case "int":
                                //get the int name
                                string[] intname = wordz.Split(' ');
                                string intz = intname[1];
                                //add the int name to the code
                                ConvertedCode.Add("public int " + intz + ";");
                                break;
                            
                            
                            case "string":
                                //get the string name
                                string[] stringname = wordz.Split(' ');
                                string stringz = stringname[1];
                                //add the string name to the code
                                ConvertedCode.Add("public string " + stringz + ";");
                                break;
                            case "if":
                                //get the if statement
                                string[] ifstatement = wordz.Split(' ');
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
                        catch (Exception)
                        {
                            Console.WriteLine("error");
                        }
                    }
                }


                Console.WriteLine(result);
                Console.WriteLine("exitForloop \n");
                // perform logic on each line


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

    public void SyntaxError(IRecognizer recognizer, int offendingSymbol, int line, int charPositionInLine, string msg, RecognitionException e)
    {
        Console.Error.WriteLine($"Syntax error at line {line}, position {charPositionInLine}: {msg}");
    }

    public void ReportAmbiguity(Parser recognizer, DFA dfa, int startIndex, int stopIndex, bool exact, BitSet ambigAlts, ATNConfigSet configs)
    {
        // Handle ambiguity errors here
        Console.WriteLine($"Ambiguity error at line {startIndex}, position {stopIndex}");
    }

    public void ReportAttemptingFullContext(Parser recognizer, DFA dfa, int startIndex, int stopIndex, BitSet conflictingAlts, SimulatorState conflictState)
    {
        // Handle full context errors here
        Console.WriteLine($"Attempting full context error at line {startIndex}, position {stopIndex}");
    }

    public void ReportContextSensitivity(Parser recognizer, DFA dfa, int startIndex, int stopIndex, int prediction, SimulatorState acceptState)
    {
        // Handle context sensitivity errors here
        Console.WriteLine($"Context sensitivity error at line {startIndex}, position {stopIndex}");
    }

    public void SyntaxError(TextWriter output, IRecognizer recognizer, int offendingSymbol, int line, int charPositionInLine, string msg, RecognitionException e)
    {
        Console.WriteLine($"Syntax error at line {line}, position {charPositionInLine}: {msg}");
    }
}