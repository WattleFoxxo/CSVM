using ProtoGram;
using System;
using Microsoft.CodeAnalysis.Syntax;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;

using System.Collections.Generic;


namespace ProtoGram
{
    public class CompilerFunctions
    {
        public static string Compile(CubeScriptSyntaxTree syntaxTree)
        {
            Console.WriteLine(syntaxTree);
            switch (syntaxTree.token.ToString())
            {
                case "UsingKeyword":
                    return "using";
                case "TypeOfKeyword":
                    return "typeof";
                case "TryKeyword":
                    return "try";
                case "TrueKeyword":
                    return "true";
                case "TildeToken":
                    return "~";
                case "ThrowKeyword":
                    return "throw";
                case "StructKeyword":
                    return "public";
                case "StringLiteralToken":
                    return "";
                case "StringKeyword":
                    return "string";
                case "StaticKeyword":
                    return "static";
                case "SlashToken":
                    return "/";
                case "SemicolonToken":
                    return ";";
                case "ReturnKeyword":
                    return "return";
                case "ReadOnlyKeyword": 
                    return "readonly";
                case "QuestionToken":   
                    return "?";
                case "QuestionQuestionToken":   
                    return "??";
                case "PrivateKeyword":
                    return "private";
                case "PlusToken":
                    return "+";
                case "PlusPlusToken":
                    return "++";
                case "PlusEqualsToken":
                    return "+=";
                case "OpenParenToken":
                    return ")";
                case "OpenBracketToken":
                    return "]";
                case "OmittedArraySizeExpressionToken":
                    return "  ";
                case "ObjectKeyword":
                    return "object";
                case "NumericLiteralToken":
                    return "";
                case "NullKeyword":
                    return "null";
                case "NewKeyword":
                    return "new";
                case "LockKeyword":
                    return "lock";
                case "LessThanToken":
                    return "<";
                case "InterpolatedStringTextToken": 
                    return "   ";
                case "InterpolatedStringStartToken":
                    return "{";
                case "InterpolatedStringEndToken":
                    return "}";
                case "InterpolatedStringMidToken":
                    return " ";
                    
                default:
                    throw new Exception("Invalid syntax tree type");
            }
        }
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
    }
}
   
    
