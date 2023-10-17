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
            Dictionary<string, string> replacements = new Dictionary<string, string>();
            replacements.Add("functiontemplate", "template");
            replacements.Add("endfunctiontemplate", "endtemplate");
            replacements.Add("AmpersandAmpersandToken", "&&");
            replacements.Add("AmpersandToken", "&");
            replacements.Add("AsteriskToken", "*");
            replacements.Add("BarBarToken", "||");
            replacements.Add("BoolKeyword", "bool");
            replacements.Add("ByteKeyword", "byte");
            replacements.Add("CatchKeyword", "catch");
            replacements.Add("CharKeyword", "char");
            replacements.Add("ClassKeyword", "class");
            replacements.Add("CloseBraceToken", "}");
            replacements.Add("CloseBracketToken", "]");
            replacements.Add("CloseParenToken", ")");
            replacements.Add("ColonToken", ":");
            replacements.Add("CommaToken", ",");
            replacements.Add("DotToken", ".");
            replacements.Add("ElseKeyword", "else");
            replacements.Add("EndOfFileToken", "");
            replacements.Add("EnumKeyword", "enum");
            replacements.Add("EqualsEqualsToken", "==");
            replacements.Add("EqualsGreaterThanToken", "=>");
            replacements.Add("EqualsToken", "=");
            replacements.Add("ExclamationEqualsToken", "!=");
            replacements.Add("ExclamationToken", "!");
            replacements.Add("FalseKeyword", "false");
            replacements.Add("ForEachKeyword", "foreach");
            replacements.Add("ForKeyword", "for");
            replacements.Add("GreaterThanToken", ">");
            replacements.Add("IfKeyword", "if");
            replacements.Add("InKeyword", "in");
            replacements.Add("IntKeyword", "int");
            replacements.Add("InternalKeyword", "internal");
            replacements.Add("InterpolatedStringEndToken", "}");
            replacements.Add("InterpolatedStringStartToken", "{");
            replacements.Add("InterpolatedStringTextToken", "");
            replacements.Add("LessThanToken", "<");
            replacements.Add("LockKeyword", "lock");
            replacements.Add("NewKeyword", "new");
            replacements.Add("NullKeyword", "null");
            replacements.Add("NumericLiteralToken", "");
            replacements.Add("ObjectKeyword", "object");
            replacements.Add("OmittedArraySizeExpressionToken", "");
            replacements.Add("OpenBraceToken", "{");
            replacements.Add("OpenBracketToken", "[");
            replacements.Add("OpenParenToken", "(");
            replacements.Add("PlusEqualsToken", "+=");
            replacements.Add("PlusPlusToken", "++");
            replacements.Add("PlusToken", "+");
            replacements.Add("PrivateKeyword", "private");
            replacements.Add("PublicKeyword", "public");
            replacements.Add("QuestionQuestionToken", "??");
            replacements.Add("QuestionToken", "?");
            replacements.Add("ReadOnlyKeyword", "readonly");
            replacements.Add("ReturnKeyword", "return");
            replacements.Add("SemicolonToken", ";");
            replacements.Add("SlashToken", "/");
            replacements.Add("StaticKeyword", "static");
            replacements.Add("StringKeyword", "string");
            replacements.Add("StringLiteralToken", "");
            replacements.Add("StructKeyword", "public");
            replacements.Add("ThrowKeyword", "throw");
            replacements.Add("TildeToken", "~");
            replacements.Add("TrueKeyword", "true");
            replacements.Add("TryKeyword", "try");
            replacements.Add("TypeOfKeyword", "typeof");
            replacements.Add("UsingKeyword", "using");
            Console.WriteLine(syntaxTree);
            // Convert the CubeScript syntax tree to a C# syntax tree
            CubeScriptSyntaxTree tree = CubeScriptSyntaxTreeConverter.ConvertToCSharp(syntaxTree, replacements);
            
            
            

    
            Console.WriteLine("CubeScript Syntax Tree:", tree.ToString());
        }
    }
}
