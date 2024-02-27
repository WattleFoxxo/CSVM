from antlr4 import CommonTokenStream, FileStream

from CubeScriptLexer import CubeScriptLexer
from CubeScriptParser import CubeScriptParser
from CubeScriptVisitor import CubeScriptVisitor
import re
#### CSharp language ####

importstatement = "using"
ifstatement = "if"
elsestatement = "else"
forstatement = "for"
whilestatement = "while"
switchstatement = "switch"
case = "case"
breakstatement = "stop"
continuestatement = "continue"
returnstatement = "return"
public = "public"
private = "private"
protected = "protected"
static = "static"
classstatement = "class"
interfacestatement = "interface"
namespacestatement = "namespace"
abstractstatement = "abstract"
virtualstatement = "virtual"
overridestatement = "override"
newstatement = "new"
thisstatement = "this"
basestatement = "base"
isstatement = "is"
asstatement = "as"
sizeofstatement = "sizeof"


#########################

# Read the input from a file
input_stream = FileStream("OpenStudioCLI.cusp")

# Create a lexer and a token stream
lexer = CubeScriptLexer(input_stream)
token_stream = CommonTokenStream(lexer)

# Create a parser and parse the token stream
parser = CubeScriptParser(token_stream)
tree = parser.program()

class CubeScriptVisitor(CubeScriptVisitor):
    def visitProgram(self, ctx: CubeScriptParser.ProgramContext):
        def visitProgram(self, ctx: CubeScriptParser.ProgramContext):
            print("Program")
            self.visitChildren(ctx)
            return



# Move the main() function below the MyTranspiler class definition
def main():
    # Create a CubeScript() visitor
    visitor = CubeScriptVisitor()

    # Visit the parse tree
    code = visitor.visit(tree)

    # Print the result
    print(code)

if __name__ == "__main__":
    main()
