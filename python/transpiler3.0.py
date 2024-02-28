from antlr4 import CommonTokenStream, FileStream

from python.CubeScriptLexer import CubeScriptLexer
from python.CubeScriptParser import CubeScriptParser
from python.CubeScriptVisitor import CubeScriptVisitor
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
input_stream = FileStream("cat.cusp")

# Create a lexer and a token stream
lexer = CubeScriptLexer(input_stream)
token_stream = CommonTokenStream(lexer)

# Create a parser and parse the token stream
parser = CubeScriptParser(token_stream)
tree = parser.program()

class CubeScriptVisitor(CubeScriptVisitor):
    def visitProgram(self, ctx: CubeScriptParser.ProgramContext):
        for statement in ctx.getChildren():
            print(self.visit(statement))


        def visitExpression(self, ctx: CubeScriptParser.ExpressionContext):
            if ctx.multOp():
                return self.visit(ctx.expression(0)) * self.visit(ctx.expression(1))
            elif ctx.addOp():
                left_expr = self.visit(ctx.expression(0))
                right_expr = self.visit(ctx.expression(1))
                if left_expr is None or right_expr is None:
                    return None
                return left_expr + right_expr
          
def main():
    # Create a CubeScript() visitor
    visitor = CubeScriptVisitor()
    print(visitor)
    # Visit the parse tree
    result = visitor.visitProgram(tree)
    # Print the result
    print(result)

if __name__ == "__main__":
    main()
