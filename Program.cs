using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using ProtoGram;


namespace Protogram
{
    class Program
    {




        static void Main(string[] args)
        {

            // Get the path to the CubeScript code file
            string filePath = args[0];

            // Convert the CubeScript code file to a syntax tree
            CubeScriptSyntaxTree syntaxTree = CubeScriptSyntaxTreeConverter.Convert(filePath);
            // Print the syntax tree
            //CubeScriptSyntaxTreeConverter.Print(syntaxTree);

            // setup
            Dictionary<string, string> replacements = new Dictionary<string, string>()
            {
            {"using", "UsingKeyword"},
            {"typeof", "TypeOfKeyword"},
            {"try", "TryKeyword"},
            {"true", "TrueKeyword"},
            {"~", "TildeToken"},
            {"throw", "ThrowKeyword"},
            {"public", "StructKeyword"},
            {"", "StringLiteralToken"},
            {"string", "StringKeyword"},
            {"static", "StaticKeyword"},
            {"/", "SlashToken"},
            {";", "SemicolonToken"},
            {"return", "ReturnKeyword"},
            {"readonly", "ReadOnlyKeyword"},
            {"?", "QuestionToken"},
            {"??", "QuestionQuestionToken"},      
            {"private", "PrivateKeyword"},
            {"+", "PlusToken"},
            {"++", "PlusPlusToken"},
            {"+=", "PlusEqualsToken"},
            {")", "OpenParenToken"},
            {"]", "OpenBracketToken"},
           
            {"  ", "OmittedArraySizeExpressionToken"},
            {"object", "ObjectKeyword"},
            {" ", "NumericLiteralToken"},
            {"null", "NullKeyword"},
            {"new", "NewKeyword"},
            {"lock", "LockKeyword"},
            {"<", "LessThanToken"},
            {"   ", "InterpolatedStringTextToken"},
            {"{", "InterpolatedStringStartToken"},
            {"}", "InterpolatedStringEndToken"},
            {"internal", "InternalKeyword"},
            {"int", "IntKeyword"},
            {"in", "InKeyword"},
            {"if", "IfKeyword"},
            {">", "GreaterThanToken"},
            {"for", "ForKeyword"},
            {"foreach", "ForEachKeyword"},
            {"false", "FalseKeyword"},
            {"!", "ExclamationToken"},
            {"!=", "ExclamationEqualsToken"},
            {"=", "EqualsToken"},
            {"=>", "EqualsGreaterThanToken"},
            {"==", "EqualsEqualsToken"},
            {"enum", "EnumKeyword"},
            {"     ", "EndOfFileToken"},
            {"else", "ElseKeyword"},
            {".", "DotToken"},
            {",", "CommaToken"},
            {":", "ColonToken"},
            {"class", "ClassKeyword"},
            {"char", "CharKeyword"},
            {"catch", "CatchKeyword"},
            {"byte", "ByteKeyword"},
            {"bool", "BoolKeyword"},
            {"||", "BarBarToken"},
            {"*", "AsteriskToken"},
             {"&", "AmpersandToken"},
             {"&&", "AmpersandAmpersandToken"},
             {"endtemplate", "endfunctiontemplate"},
             {"template", "functiontemplate"},
             
            };
            Console.WriteLine(syntaxTree);
            // Convert the CubeScript syntax tree to a C# syntax tree
            CubeScriptSyntaxTree tree = CubeScriptSyntaxTreeConverter.ConvertToCSharp(syntaxTree, replacements);
            
            CubeScriptSyntaxTree finalisedcode = CubeScriptSyntaxTreeConverter.Translate(tree, replacements);



            Console.WriteLine("CubeScript Syntax Tree:", finalisedcode);
        }
    }
}
