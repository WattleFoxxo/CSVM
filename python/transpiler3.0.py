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


#########################

# Read the input from a file
input_stream = FileStream("OpenStudioCLI.cusp")

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

        # Visit each statement in the program.0
        for i in range(ctx.getChildCount()):
            statement = self.visit(ctx.getChild(i))
            if statement:
                statements.append(statement)

        # Join the statements with newlines and return the result
        return "\n".join(statements)

    def visitStatement(self, ctx):
        # Visit the expression and return the result
        statement = ctx.getText()
        return statement

    def visitExpression(self, ctx):
        # Visit the expression and return the result
        expression = ctx.getText()
        expressions = []
        if expression.startswith("using"):
            # Insert a space after "using"
            expression = importstatement + " " + expression[5:]
            expressions.append(expression.split())

        elif expression.startswith("if"):
            # Insert a space after "if"
            expression = ifstatement + " " + expression[2:]
            expressions.append(expression.split())

        else:
            # if the expression is not any of the above, then it is a function call
            for i in range(ctx.getChildCount()):
                expressions.append(ctx.getChild(i).getText().split())
        print(expressions)

    def visitSwitchStatement(self, ctx):
        # get the contents of the statement
        switchstatements = ctx.getText()
        switchstatement = []
        if switchstatements.startswith("switch"):
            # Insert a space after "switch"
            switchstatements = switchstatement + " " + switchstatements[6:]
            switchstatement.append(switchstatements.split())
        else:
            # if the expression is not any of the above, then it is a function call
            for i in range(ctx.getChildCount()):
                switchstatement.append(ctx.getChild(i).getText().split())
                
    def visitAddOp(self, ctx: CubeScriptParser.AddOpContext):
        return super().visitAddOp(ctx)

    def visitSwitchBlock(self, ctx: CubeScriptParser.SwitchBlockContext):
        # get the contents of the statement
        switchblocks = ctx.getText()
        switchblock = []
        if switchblocks.startswith("switch"):
            # Insert a space after "switch"
            switchblocks = switchstatement + " " + switchblocks[6:]
            switchblock.append(switchblocks.split())
        else:
            # if the expression is not any of the above, then it is a function call
            for i in range(ctx.getChildCount()):
                switchblock.append(ctx.getChild(i).getText().split())

    def visitIfStatement(self, ctx):
        # get the contents of the statement
        ifblocks = ctx.getText()
        ifblock = []
        if ifblocks.startswith("if"):
            # Insert a space after "if"
            ifblocks = ifstatement + " " + ifblocks[2:]
            ifblock.append(ifblocks.split())
        else:
            # if the expression is not any of the above, then it is a function call
            for i in range(ctx.getChildCount()):
                ifblock.append(ctx.getChild(i).getText().split())

    import re

    def visitFunction(self, ctx):
        # Visit the expression and return the result
        function = ctx.getText()
        functions = []
        for func in function: # split the lines 
            fun = func.split(";")
            print(fun)
        
    def visitFunctionCall(self, ctx):
        # Visit the expression and return the result
        functionCall = ctx.getText()
        functionCalls = []
        func =functionCall.split(";") # split the lines 
        for fun in func:
            if fun.startswith("struct"):
                print("struct")
            
        print(func)

    def visitFunctionDeclaration(self, ctx):
        # Visit the expression and return the result
        functionDeclaration = ctx.getText()
        functionDeclarations = []
        if functionDeclaration.startswith("struct"):
            # function declaration
            functionDeclaration = (
                functionDeclaration[:6] + " " + functionDeclaration[6:]
            )
            functionDeclarations.append(functionDeclaration.split())
        else:
            # if the expression is not any of the above, then it is a function call
            for i in range(ctx.getChildCount()):
                functionDeclarations.append(ctx.getChild(i).getText().split())
        print(functionDeclarations)


# usinginternet; not good
# using internet; thats what we want
# using <IDENTIFER>; thats what we want


def main():
    # Create a visitor and visit the tree
    visitor = MyTranspiler()
    code = visitor.visit(tree)

    # Print the result
    print(code)


main()
