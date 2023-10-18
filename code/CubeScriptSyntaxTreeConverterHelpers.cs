using ProtoGram;

public static class CubeScriptCompilerCheck
{

    public static void PrintContentsToFile(CubeScriptSyntaxTree syntaxTree)
    {
        // itterate thru the syntax tree and print the contents to a file while only Writing one of each syntax type to the file
        if (syntaxTree == null)
        {
            Exception e = new Exception("Syntax Error: CUSP0005: File Read Error"); // ether the file faild to read or the extention is not cusp
            throw e;
        }
        // Create a list to store the tokens
        List<CubeScriptSyntax> syntax = new List<CubeScriptSyntax>();
        // itterate thru the syntax tree and print the contents to a file while only Writing one of each syntax type to the file
        foreach (CubeScriptSyntax syntax1 in syntaxTree.Syntax)
        {
            // check if the syntax is already in the list

            // if it is not then add it to the list
            syntax.Add(syntax1);
            //write the contents to a file
            File.AppendAllText("output.cusps", syntax1.Type + "\n");
        }
        return;
        
    }



}
