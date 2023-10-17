using FrooxEngine;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Newtonsoft.Json;
using System.Linq;
using System.Xml.Linq;


namespace ProtoGram
{
    //create a template for syntax of CubeScript

    public class CubeScriptSyntax
    {
        public string Name { get; set; }
        public string Type { get; set; }
        public string Value { get; set; }
        public string Token { get; set; }
        public string Defaultvalue { get; set; }
        public string Returntype { get; set; }
        
        public override string ToString()
        {
            return  " Type: " + Type + " Value: " + Value ;
        }

    }

    public class CubeScriptSyntaxTree
    {
        public List<CubeScriptSyntax> Syntax { get; set; }
        public object RootNode { get; internal set; }
        List<CubeScriptSyntax> translatedSyntax = new List<CubeScriptSyntax>();
        internal object token;

        public override string ToString()
        {
            return string.Join("\n", Syntax.Select((s) => s .ToString()));
        }
    }
    public class CubeScriptSyntaxTreeConverter
    {

        public static CubeScriptSyntaxTree Convert(string filePath)
        {
            // Create a list to store the tokens
            List<CubeScriptSyntax> syntax = new List<CubeScriptSyntax>();

            // Parse the CubeScript code file
            // read the file extention
            string extention = Path.GetExtension(filePath);

            if (extention != ".cusp")
            {
                Exception e = new Exception("Syntax Error: CUSP0004: File Read Error"); // ether the file faild to read or the extention is not cusp
                throw e;
            }

            SyntaxTree tree = CSharpSyntaxTree.ParseText(File.ReadAllText(filePath));

            Console.WriteLine("File Read Sucessful");
            Console.WriteLine(tree.ToString());

            // Get the root of the syntax tree and iterate over each token
            SyntaxNode root = tree.GetRoot();
            foreach (SyntaxToken token in root.DescendantTokens())
            {
                // Get the token type and value
                var tokenType = token.Kind().ToString();
                var tokenValue = token.ValueText;

                // Add the token to the list
                
                syntax.Add(new CubeScriptSyntax { Type = tokenType, Value = tokenValue });
            }

            // Create a new CubeScriptSyntaxTree and add the tokens
            CubeScriptSyntaxTree syntaxTree = new CubeScriptSyntaxTree();
            syntaxTree.Syntax = syntax;
            Console.WriteLine(syntaxTree.ToString());
            // Return the CubeScriptSyntaxTree
            return syntaxTree;
        }
        public static CubeScriptSyntaxTree Translate(CubeScriptSyntaxTree syntaxTree, Dictionary<string, string> translationDictionary)
{
    // Create a new list to store the translated tokens
    List<CubeScriptSyntax> translatedSyntax = new List<CubeScriptSyntax>();

    // Iterate over each token in the syntax tree
    foreach (CubeScriptSyntax token in syntaxTree.Syntax)
    {
        // Check if the token's value is in the translation dictionary
        if (translationDictionary.ContainsKey(token.Type))
        {
            // If it is, replace the token's value with the translated value
            translatedSyntax.Add(new CubeScriptSyntax { Type = token.Type, Value = translationDictionary[token.Value] });
        }
        else
        {
            // If it's not, add the original token to the translated syntax list
            translatedSyntax.Add(token);
        }
    }

    // Create a new CubeScriptSyntaxTree and add the translated tokens
    CubeScriptSyntaxTree translatedSyntaxTree = new CubeScriptSyntaxTree();
    translatedSyntaxTree.Syntax = translatedSyntax;

    // Return the translated CubeScriptSyntaxTree
    return translatedSyntaxTree;
}
        public static void Print(CubeScriptSyntaxTree syntaxTree)
        {
            // Iterate over each token in the syntax tree
            foreach (CubeScriptSyntax syntax in syntaxTree.Syntax)
            {
                // Print the token type and value
                Console.WriteLine($"Type: {syntax.Type}, Value: {syntax.Value}");
            }
        }

        public static void Save(CubeScriptSyntaxTree syntaxTree, string filePath)
        {
            // Serialize the syntax tree to a JSON string
            string json = JsonConvert.SerializeObject(syntaxTree, Formatting.Indented);

            // Write the JSON string to the specified file
            File.WriteAllText(filePath, json);
        }

        public static CubeScriptSyntaxTree Load(string filePath)
        {
            // Read the JSON string from the specified file
            string json = File.ReadAllText(filePath);

            // Deserialize the JSON string to a CubeScriptSyntaxTree
            CubeScriptSyntaxTree syntaxTree = JsonConvert.DeserializeObject<CubeScriptSyntaxTree>(json);

            // Return the CubeScriptSyntaxTree
            return syntaxTree;
        }

        public static void PrintJson(CubeScriptSyntaxTree syntaxTree)
        {
            // Serialize the syntax tree to a JSON string
            string json = JsonConvert.SerializeObject(syntaxTree, Formatting.Indented);

            // Print the JSON string
            Console.WriteLine(json);
        }


        public static string GetTemplate()
        {
            //define the syntax for CubeScript so that on compile it checks against it using templates and then outputs the correct code
            string template = @"<|functiontemplate|>"
                              + "<|name|> : <|returntype|> = <|defaultvalue|>"
                              + @"<|endfunctiontemplate|>";
            return template;
        }

        public static string Template_function()
        {
            //define the syntax for CubeScript so that on compile it checks against it using templates and then outputs the correct code
            string template = "StructKeyword name OpenParentToken CloseParentToken OpenBraceToken <|functionbody|> CloseBraceToken";
            return template;
        }

        public static string Template_Varibles()
        {
            string template = @"<|varible|> <|name|> = <|defaultvalue|>;"
                              + @"<|endvarible|> ";
            return template;
        }
        public static List<string> Template_VaribleDesignation()
        {
            //define every type that uses the <||> in the templates so that on compile it checks against it using templates and then outputs the correct code
            List<string> VaribleDesignation = new List<string>();
            VaribleDesignation.Add("AmpersandAmpersandToken");
            VaribleDesignation.Add("AmpersandToken");
            VaribleDesignation.Add("AsteriskToken");
            VaribleDesignation.Add("BarBarToken");
            VaribleDesignation.Add("BoolKeyword");
            VaribleDesignation.Add("ByteKeyword");
            VaribleDesignation.Add("CatchKeyword");
            VaribleDesignation.Add("CharKeyword");
            VaribleDesignation.Add("CharacterLiteralToken");
            VaribleDesignation.Add("ClassKeyword");
            VaribleDesignation.Add("CloseBraceToken");
            VaribleDesignation.Add("CloseBracketToken");
            VaribleDesignation.Add("CloseParenToken");
            VaribleDesignation.Add("ColonToken");
            VaribleDesignation.Add("CommaToken");
            VaribleDesignation.Add("DotToken");
            VaribleDesignation.Add("ElseKeyword");
            VaribleDesignation.Add("EndOfFileToken");
            VaribleDesignation.Add("EnumKeyword");
            VaribleDesignation.Add("EqualsEqualsToken");
            VaribleDesignation.Add("EqualsGreaterThanToken");
            VaribleDesignation.Add("EqualsToken");
            VaribleDesignation.Add("ExclamationEqualsToken");
            VaribleDesignation.Add("ExclamationToken");
            VaribleDesignation.Add("FalseKeyword");
            VaribleDesignation.Add("ForEachKeyword");
            VaribleDesignation.Add("ForKeyword");
            VaribleDesignation.Add("GreaterThanToken");
            VaribleDesignation.Add("IdentifierToken");
            VaribleDesignation.Add("IfKeyword");
            VaribleDesignation.Add("InKeyword");
            VaribleDesignation.Add("IntKeyword");
            VaribleDesignation.Add("InternalKeyword");
            VaribleDesignation.Add("InterpolatedStringEndToken");
            VaribleDesignation.Add("InterpolatedStringStartToken");
            VaribleDesignation.Add("InterpolatedStringTextToken");
            VaribleDesignation.Add("LessThanToken");
            VaribleDesignation.Add("LockKeyword");
            VaribleDesignation.Add("NewKeyword");
            VaribleDesignation.Add("NullKeyword");
            VaribleDesignation.Add("NumericLiteralToken");
            VaribleDesignation.Add("ObjectKeyword");
            VaribleDesignation.Add("OmittedArraySizeExpressionToken");
            VaribleDesignation.Add("OpenBraceToken");
            VaribleDesignation.Add("OpenBracketToken");
            VaribleDesignation.Add("OpenParenToken");
            VaribleDesignation.Add("PlusEqualsToken");
            VaribleDesignation.Add("PlusPlusToken");
            VaribleDesignation.Add("PlusToken");
            VaribleDesignation.Add("PrivateKeyword");
            VaribleDesignation.Add("PublicKeyword");
            VaribleDesignation.Add("QuestionQuestionToken");
            VaribleDesignation.Add("QuestionToken");
            VaribleDesignation.Add("ReadOnlyKeyword");
            VaribleDesignation.Add("ReturnKeyword");
            VaribleDesignation.Add("SemicolonToken");
            VaribleDesignation.Add("SlashToken");
            VaribleDesignation.Add("StaticKeyword");
            VaribleDesignation.Add("StringKeyword");
            VaribleDesignation.Add("StringLiteralToken");
            VaribleDesignation.Add("StructKeyword");
            VaribleDesignation.Add("ThrowKeyword");
            VaribleDesignation.Add("TildeToken");
            VaribleDesignation.Add("TrueKeyword");
            VaribleDesignation.Add("TryKeyword");
            VaribleDesignation.Add("TypeOfKeyword");
            VaribleDesignation.Add("UsingKeyword");
            return VaribleDesignation;
        }
        public static CubeScriptSyntaxTree ReplaceValues(CubeScriptSyntaxTree syntaxTree, Dictionary<string, string> replacements)
        {
            // Create a new list to store the translated tokens
            List<CubeScriptSyntax> translatedSyntax = new List<CubeScriptSyntax>();

            // Iterate over each token in the syntax tree
            foreach (CubeScriptSyntax token in syntaxTree.Syntax)
            {
                // Check if the token's type is in the translation dictionary
                if (replacements.ContainsKey(token.Type))
                {
                    // If it is, replace the token's value with the translated value
                    translatedSyntax.Add(new CubeScriptSyntax { Type = token.Type, Value = replacements[token.Type] });
                }
                else
                {
                    // If it's not, add the original token to the translated syntax list
                    translatedSyntax.Add(token);
                }
            }

            // Create a new CubeScriptSyntaxTree and add the translated tokens
            CubeScriptSyntaxTree translatedSyntaxTree = new CubeScriptSyntaxTree();
            translatedSyntaxTree.Syntax = translatedSyntax;

            // Return the translated CubeScriptSyntaxTree
            return translatedSyntaxTree;
        }

        //public static CubeScriptSyntaxTree ReplaceTargetOfClassOrMethod(string syntax, string replacement)
        //{

        //    // Get the target class or method and its contents
        //    int indexOfClassOrMethod = -1;
        //    for (int i = 0; i < syntax.Count; i++)
        //    {
        //        if ((syntax[i].Type == "ClassKeyword" || syntax[i].Type == "OpenBraceToken") && syntax[i].Value == target)
        //        {
        //            indexOfClassOrMethod = i;
        //            break;
        //        }
        //    }
        //    if (indexOfClassOrMethod == -1)
        //    {
        //        return; // Target not found, do nothing
        //    }
        //    int indexOfOpeningBrace = -1, indexOfClosingBrace = -1, depth = 1;
        //    for (int i = indexOfClassOrMethod; i < syntax.Count; i++)
        //    {
        //        if (syntax[i].Type == "OpenBraceToken")
        //        {
        //            if (indexOfOpeningBrace == -1)
        //            {
        //                indexOfOpeningBrace = i;
        //            }
        //            depth++;
        //        }
        //        else if (syntax[i].Type == "CloseBraceToken")
        //        {
        //            depth--;
        //            if (depth == 0)
        //            {
        //                indexOfClosingBrace = i;
        //                break;
        //            }
        //        }
        //    }
        //    if (indexOfOpeningBrace == -1 || indexOfClosingBrace == -1)
        //    {
        //        return; // Error in syntax, do nothing
        //    }
        //    // Insert the replacement code between the opening and closing braces
        //    translatedSyntax.InsertRange(indexOfOpeningBrace + 1, CSharpSyntaxTree.ParseText(replacement).GetRoot().DescendantTokens()
        //        .Select(token => new CubeScriptSyntax { Type = token.Kind().ToString(), Value = token.ValueText }));
        //    // Remove the old class or method and its content
        //    translatedSyntax.RemoveRange(indexOfClassOrMethod, indexOfClosingBrace - indexOfClassOrMethod);
        //    return translatedSyntaxTree;
        //}

        //public static void ReplaceCodeInsideForEachLoop(string forEach)
        //{
        //    // Get the opening and closing parenthesis of the foreach loop
        //    int indexOfOpeningParen = -1, indexOfClosingParen = -1, depth = 1;
        //    for (int i = 0; i < syntax.Count; i++)
        //    {
        //        if (syntax[i].Type == "ForEachKeyword" && syntax[i].Value == forEach)
        //        {
        //            indexOfOpeningParen = i + 1;
        //            break;
        //        }
        //    }
        //    if (indexOfOpeningParen == -1)
        //    {
        //        return; // Foreach not found, do nothing
        //    }
        //    for (int i = indexOfOpeningParen; i < syntax.Count; i++)
        //    {
        //        if (syntax[i].Type == "OpenParenToken")
        //        {
        //            depth++;
        //        }
        //        else if (syntax[i].Type == "CloseParenToken")
        //        {
        //            depth--;
        //            if (depth == 0)
        //            {
        //                indexOfClosingParen = i;
        //                break;
        //            }
        //        }
        //    }
        //    if (indexOfClosingParen == -1)
        //    {
        //        return; // Error in syntax, do nothing
        //    }
        //    // Get the index of opening brace after the foreach loop variable declaration
        //    int indexOfOpeningBrace = -1;
        //    for (int i = indexOfClosingParen; i < syntax.Count; i++)
        //    {
        //        if (syntax[i].Type == "OpenBraceToken")
        //        {
        //            indexOfOpeningBrace = i;
        //            break;
        //        }
        //    }
        //    if (indexOfOpeningBrace == -1)
        //    {
        //        return; // Error in syntax, do nothing
        //    }
        //    // Insert a new line and a tab character at the index of the opening brace
        //    translatedSyntax.Insert(indexOfOpeningBrace, new CubeScriptSyntax { Type = "WhitespaceTrivia", Value = "\n\t" });
        //    // Get the index of the closing brace
        //    int indexOfClosingBrace = -1, scopeCount = 1;
        //    for (int i = indexOfOpeningBrace; i < syntax.Count; i++)
        //    {
        //        if (syntax[i].Type == "OpenBraceToken")
        //        {
        //            scopeCount++;
        //        }
        //        else if (syntax[i].Type == "CloseBraceToken")
        //        {
        //            scopeCount--;
        //            if (scopeCount == 0)
        //            {
        //                indexOfClosingBrace = i;
        //                break;
        //            }
        //        }
        //    }
        //    if (indexOfClosingBrace == -1)
        //    {
        //        return; // Error in syntax, do nothing
        //    }
        //    // Get the content between the opening and closing braces
        //    string codeInsideForeach = string.Join("", syntax.GetRange(indexOfOpeningBrace + 1, indexOfClosingBrace - indexOfOpeningBrace - 1)
        //        .Select(foreachToken => foreachToken.Value));
        //    // Remove the content inside the braces
        //    translatedSyntax.RemoveRange(indexOfOpeningBrace + 1, indexOfClosingBrace - indexOfOpeningBrace - 1);
        //    // Insert a new line and a tab character at the index of the opening brace
        //    translatedSyntax.Insert(indexOfOpeningBrace + 1, new CubeScriptSyntax { Type = "WhitespaceTrivia", Value = "\n\t" });
        //    // Insert the content inside the braces with a tab character prefix
        //    translatedSyntax.InsertRange(indexOfOpeningBrace + 2, CSharpSyntaxTree.ParseText(codeInsideForeach).GetRoot().DescendantTokens()
        //        .Select(token => new CubeScriptSyntax { Type = token.Kind().ToString(), Value = "\t" + token.ValueText }));
        //    // Insert a new line and a tab character at the index of the closing brace
        //    translatedSyntax.Insert(indexOfClosingBrace, new CubeScriptSyntax { Type = "WhitespaceTrivia", Value = "\n\t" });
        //}


    }

}








