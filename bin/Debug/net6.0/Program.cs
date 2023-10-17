using System;
using System.IO;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;

namespace MyNamespace
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length == 0)
            {
                Console.WriteLine("Please specify a C# file to analyze.");
                return;
            }

            string filePath = args[0];

            

            try
            {
                // Parse the C# code file
                SyntaxTree tree = CSharpSyntaxTree.ParseText(File.ReadAllText(filePath));

                // Get the root of the syntax tree
                SyntaxNode root = tree.GetRoot();

                // Do something with the syntax tree
                // (e.g., print out the name of all methods)
                foreach (var method in root.DescendantNodes().OfType<MethodDeclarationSyntax>())
                {
                    Console.WriteLine(method.Identifier.ValueText);
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error analyzing file:");
                Console.WriteLine(ex.Message);
            }
        }
    }
}