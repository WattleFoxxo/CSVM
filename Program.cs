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
            { "functiontemplate", "template"},
            {"endfunctiontemplate", "endtemplate"},
            {"AmpersandAmpersandToken", "&&"},
            {"AmpersandToken", "&"},
            {"AsteriskToken", "*"},
            {"BarBarToken", "||"},
            {"BoolKeyword", "bool"},
            {"ByteKeyword", "byte"},
            {"CatchKeyword", "catch"},
            {"CharKeyword", "char"},
            {"ClassKeyword", "class"},
            {"CloseBraceToken", "}"},
            {"CloseBracketToken", "]"},
            {"CloseParenToken", ")"},
            {"ColonToken", ":"},
            {"CommaToken", ","},
            {"DotToken", "."},
            {"ElseKeyword", "else"},
            {"EndOfFileToken", ""},
            {"EnumKeyword", "enum"},
            {"EqualsEqualsToken", "=="},
            {"EqualsGreaterThanToken", "=>"},
            {"EqualsToken", "="},
            {"ExclamationEqualsToken", "!="},
            {"ExclamationToken", "!"},
            {"FalseKeyword", "false"},
            {"ForEachKeyword", "foreach"},
            {"ForKeyword", "for"},
            {"GreaterThanToken", ">"},
            {"IfKeyword", "if"},
            {"InKeyword", "in"},
            {"IntKeyword", "int"},
            {"InternalKeyword", "internal"},
            {"InterpolatedStringEndToken", "}"},
            {"InterpolatedStringStartToken", "{"},
            {"InterpolatedStringTextToken", ""},
            {"LessThanToken", "<"},
            {"LockKeyword", "lock"},
            {"NewKeyword", "new"},
            {"NullKeyword", "null"},
            {"NumericLiteralToken", ""},
            {"ObjectKeyword", "object"},
            {"OmittedArraySizeExpressionToken", ""},
            {"OpenBraceToken", "{"},
            {"OpenBracketToken", "["},
            {"OpenParenToken", "("},
            {"PlusEqualsToken", "+="},
            {"PlusPlusToken", "++"},
            {"PlusToken", "+"},
            {"PrivateKeyword", "private"},
            {"PublicKeyword", "public"},
            {"QuestionQuestionToken", "??"},
            {"QuestionToken", "?"},
            {"ReadOnlyKeyword", "readonly"},
            {"ReturnKeyword", "return"},
            {"SemicolonToken", ";"},
            {"SlashToken", "/"},

            {"StaticKeyword", "static"},
            {"StringKeyword", "string"},
            {"StringLiteralToken", ""},
            {"StructKeyword", "public"},
            {"ThrowKeyword", "throw"},
            {"TildeToken", "~"},
            {"TrueKeyword", "true"},
            {"TryKeyword", "try"},
            {"TypeOfKeyword", "typeof"},
            {"UsingKeyword", "using"},
            };
            Console.WriteLine(syntaxTree);
            // Convert the CubeScript syntax tree to a C# syntax tree
            CubeScriptSyntaxTree tree = CubeScriptSyntaxTreeConverter.ConvertToCSharp(syntaxTree, replacements);
            
            CubeScriptSyntaxTree finalisedcode = CubeScriptSyntaxTreeConverter.Translate(syntaxTree, replacements);



            Console.WriteLine("CubeScript Syntax Tree:", finalisedcode);
        }
    }
}
