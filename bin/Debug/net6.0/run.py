# Open the input file for reading
input = """ {"using", "UsingKeyword"},
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
{"{", "OpenBraceToken"},
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
{"template", "functiontemplate"},"""
def main():
    # take the input string and remove duplicate lines
    lines = input.splitlines()
    lines = list(dict.fromkeys(lines))
    # print the output without the keys
    for line in lines:
        print(line.split(',')[0].strip())



main()