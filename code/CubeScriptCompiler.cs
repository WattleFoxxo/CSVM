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




            switch (syntaxTree.ToString())
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
                    return "void";
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
                case "InternalKeyword":
                    return "internal";
                case "IntKeyword":
                    return "int";
                case "InKeyword":
                    return "in";
                case "IfKeyword":
                    return "if";
                case "GreaterThanToken":
                    return ">";
                case "ForKeyword":
                    return "for";
                case "ForEachKeyword":
                    return "foreach";
                case "FalseKeyword":
                    return "false";
                case "ExclamationToken":
                    return "!";
                case "ExclamationEqualsToken":
                    return "!=";
                case "EqualsToken":
                    return "=";
                case "EqualsGreaterThanToken":
                    return "=>";
                case "EqualsEqualsToken":
                    return "==";
                case "EnumKeyword":
                    return "enum";
                case "EndOfFileToken":
                    return "     ";
                case "ElseKeyword":
                    return "else";
                case "DotToken":
                    return ".";
                case "CommaToken":
                    return ",";
                case "ColonToken":
                    return ":";
                case "ClassKeyword":
                    return "class";
                case "CharKeyword":
                    return "char";
                case "CatchKeyword":
                    return "catch";
                case "ByteKeyword":
                    return "byte";
                case "BoolKeyword":
                    return "bool";
                case "BarBarToken":
                    return "||";
                case "AsteriskToken":
                    return "*";
                case "AmpersandToken":
                    return "&";
                case "AmpersandAmpersandToken":
                    return "&&";


                default:
                    Console.WriteLine(syntaxTree);
                    throw new Exception("Invalid syntax tree type");
                    Console.WriteLine("cat");
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

   
    
