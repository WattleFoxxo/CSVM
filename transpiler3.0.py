from antlr4 import FileStream, CommonTokenStream
from CubeScriptLexer import CubeScriptLexer
from CubeScriptParser import CubeScriptParser
from CubeScriptVisitor import CubeScriptVisitor

# Read the input from a file
input_stream = FileStream('OpenStudioCLI.cusp')

# Create a lexer and a token stream
lexer = CubeScriptLexer(input_stream)
token_stream = CommonTokenStream(lexer)

# Create a parser and parse the token stream
parser = CubeScriptParser(token_stream)
tree = parser.program()

# reform the tokens back in CSharp language

class MyTranspiler(CubeScriptVisitor):
    def visitProgram(self, ctx):
        # Initialize an empty list to hold the code for each statement
        statements = []

        # Visit each statement in the program
        for i in range(ctx.getChildCount()):
            statement = self.visit(ctx.getChild(i))
            if statement:
                statements.append(statement)

        # Join the statements with newlines and return the result
        return '\n'.join(statements)



def main():
    # Create a visitor and visit the tree
    visitor = MyTranspiler()
    code = visitor.visit(tree)
    print(code)


main()


