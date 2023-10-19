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
    public override void EnterAssignment([NotNull] CubeScriptParser.AssignmentContext context)
    {
        // extract information from an assignment statement
        string variableName = context.IDENTIFIER().GetText();
        string value = context.expression().GetText();
        Console.WriteLine("Assignment: {0} = {1}", variableName, value);
    }

    public override void EnterFunctioncallexprs([NotNull] CubeScriptParser.FunctioncallexprsContext context)
    {
        // extract information from a function call
        string functionName = context.IDENTIFIER(0).GetText();
        string namespaceName = null;
        if (context.IDENTIFIER().Length > 1)
        {
            namespaceName = context.IDENTIFIER(0).GetText();
            functionName = context.IDENTIFIER(1).GetText();
        }
        Console.WriteLine("Function call: {0}.{1}", namespaceName, functionName);
        foreach (var expression in context.expression())
        {
            Console.WriteLine("Argument: {0}", expression.GetText());
        }
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
}
}