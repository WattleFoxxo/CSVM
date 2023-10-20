﻿using Microsoft.CodeAnalysis;
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
        public Dictionary<string, object?> Varibles { get; } = new();
        //function array
        public Dictionary<string, object?> Functions { get; } = new();
        //converted code array?
        public List<string> ConvertedCode { get; } = new();
        //loaded assemblies array
        public List<Assembly> LoadedAssemblies { get; } = new();
        //function name

    public override void EnterVaribleassignment([NotNull] CubeScriptParser.VaribleassignmentContext context)
    {
        // extract information from an assignment statement
        string variableName = context.IDENTIFIER().GetText();
        string value = context.expression().GetText();

        // convert the assignment statement to C#
        string csharpStatement = $"{variableName} = {value};";
        //save the converted code to the dictionary
        ConvertedCode.Add(csharpStatement);

        Console.WriteLine("C# varible Assignment: {0}", csharpStatement);
    }
    //get the string things from #varibledeclaration
    public override void EnterVaribledeclaration([NotNull] CubeScriptParser.VaribledeclarationContext context)
    {
        // extract information from an assignment statement
        string variableName = context.IDENTIFIER().GetText();
        string value = context.expression().GetText();

        // convert the assignment statement to C#
        string csharpStatement = $"{variableName} = {value};";
        //save the converted code to the dictionary
        ConvertedCode.Add(csharpStatement);

        Console.WriteLine("C# varible Assignment: {0}", csharpStatement);
    }
    


    //finished converting to c#
    public override void EnterProgram([NotNull] CubeScriptParser.ProgramContext context)
        {
            Console.WriteLine("C# Program: {0}", context.GetText());
        }
    public override void EnterAssignment([NotNull] CubeScriptParser.AssignmentContext context)
    {
        // extract information from an assignment statement
        string variableName = context.IDENTIFIER().GetText();
        string value = context.expression().GetText();

        // convert the assignment statement to C#
        string csharpStatement = $"{variableName} = {value};";
        //save the converted code to the dictionary
        ConvertedCode.Add(csharpStatement);

        Console.WriteLine("C# Assignment: {0}", csharpStatement);
    }
        
    //math operations
    public override void EnterMultexpr(CubeScriptParser.MultexprContext context)
    {
        var left = context.expression(0).GetText();
        var right = context.expression(1).GetText();
        var op = context.expression(1).GetText();
        switch (op)
        {
            case "+":
                Console.WriteLine("C# Assignment: {0}" + "add");
                Add(left, right);
                break;
            case "-":
                Console.WriteLine("C# Assignment: {0}" + "subtract");
                Subtract(left, right);

                break;
            default:
                throw new NotImplementedException();
        }
    }
    private object? Add(object? left, object? right)
    {
        if (left is int l && right is int r)
        {
            Console.WriteLine("C# Assignment: {0}", l + r);
            
            return l + r;
        }
        else if (left is string ls && right is string rs)
        {
            Console.WriteLine("C# Assignment: {0}", ls + rs);
            ConvertedCode.Add(ls + rs);
            return ls + rs;
        }
        else
        {
            throw new NotImplementedException();
        }
    }
    private object? Subtract(object? left, object? right)
    {
        if (left is int l && right is int r)
            return l - r;
        if (left is string || right is string)
            return $"{left}{right}";

        if (left is float lfloat && right is int rint)
            return lfloat - rint;

        throw new Exception("Invalid operation cusp00001" + "cannot add values of type " + left?.GetType() + " and " + right?.GetType());
        
    }

    public override object? EnterIdentifierexpression(CubeScriptParser.IdentifierexpressionContext context)
    {
        var varname = context.IDENTIFIER().GetText();
        if (!Varibles.ContainsKey(varname))
        {
            throw new Exception("Variable " + varname + " does not exist");
        }
        Console.WriteLine("C# Assignment: {0}", varname);
        ConvertedCode.Add(varname);
        return Varibles[varname];
    }

    public override void EnterFunctioncallexprs(CubeScriptParser.FunctioncallexprsContext context)
    {
        // extract information from a function call
        string functionName = context.IDENTIFIER(0).GetText();
        string namespaceName = null;
        if (context.IDENTIFIER().Length > 1)
        {
            namespaceName = context.IDENTIFIER(0).GetText();
            functionName = context.IDENTIFIER(1).GetText();
        }

        // convert the function call to C#
        string arguments = string.Join(", ", context.expression().Select(e => e.GetText()));
        string csharpStatement = "";

        switch (functionName)
        {
            case "print":
                csharpStatement = $"Console.WriteLine({arguments});";
                break;
            case "input":
               
                break;
            case "random":
                csharpStatement = $"new Random().Next({arguments})";
                break;
            default:
                if (string.IsNullOrEmpty(functionName))
                {
                    // Do something for empty function name
                }
                else
                {
                    csharpStatement = $"{(namespaceName != null ? namespaceName + "." : "")}{functionName}({arguments});";
                }
                break;
        }

        Console.WriteLine("C# Function Call: {0}", csharpStatement);
        ConvertedCode.Add(csharpStatement);
        
    }
    public override void EnterImportstatement(CubeScriptParser.ImportstatementContext context)
    {


   //set the default location for the assemblies so that they can be loaded
    var assemblyName = context.IDENTIFIER()[0].GetText();
    var dll = ".dll";
    var assemblyLocation = Path.GetDirectoryName($"C://Users//{Environment.UserName}//assembly//{assemblyName}" + dll);
   //if the directory doesnt exist, create it
    if (!Directory.Exists(assemblyLocation))
    {
        Directory.CreateDirectory(assemblyLocation);
    }
    // get the assembly file while only include once if it has already been loaded
    var assemblyFile = Directory.GetFiles(assemblyLocation, assemblyName + dll, SearchOption.AllDirectories).FirstOrDefault();
    if (assemblyFile == null)
    {
        throw new Exception("Assembly file not found");
    }
    //load the assembly while only loading it once
    if (LoadedAssemblies.Any(a => a.FullName == assemblyFile))
    {
        return;
    }
    else{

    
    var assembly = Assembly.LoadFile(assemblyFile);
    //add the assembly to the list
    LoadedAssemblies.Add(assembly);
    Console.WriteLine("C# Assembly: {0}", assembly);
    }

}
    public override void EnterFunctioncallstatment(CubeScriptParser.FunctioncallstatmentContext context)
    {
        // This method is called when the parser enters a function declaration rule in the parse tree
        string functionName = context.IDENTIFIER()[0].GetText();
        string parameters = string.Join(", ", context.IDENTIFIER().Skip(1).Select(i => i.GetText()));
        //replace with c# code
        string csharpStatement = $"public void {functionName}({parameters}) {{ }}";
        Console.WriteLine("C# Function Declaration: {0}", csharpStatement);

        Console.WriteLine("Function Declaration: {0}({1})", functionName, parameters);
        ConvertedCode.Add(csharpStatement);
    }

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

   //convert the code using the listener and switch statements

   if (listener.LoadedAssemblies.Count > 0)
    {
         //get the loaded assemblies and convert them to c#
        foreach (var assembly in listener.LoadedAssemblies)// printing the loaded assemblies will make you think that it's loaded more then once but it's not
        {
            if (assembly == null)
            {
                throw new Exception("Assembly is null");
            }
            else 
            {
                Console.WriteLine("C# Assembly: {0}", assembly);
                listener.ConvertedCode.Add(assembly.ToString());
                return;
            }
        }

        
    }
    //get the converted code and print it
    var convertedCodeString = string.Join(Environment.NewLine, listener.ConvertedCode);
    Console.WriteLine("C# Program: {0}", convertedCodeString);
    
}
}