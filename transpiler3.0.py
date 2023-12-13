import re
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

        # Visit each statement in the program.0
        for i in range(ctx.getChildCount()):
            statement = self.visit(ctx.getChild(i))
            if statement:
                statements.append(statement)

        # Join the statements with newlines and return the result
        return '\n'.join(statements)

    def visitStatement(self, ctx):
        # Get the text of the statement
        statement = ctx.getText()
        # If the statement is not empty, return it
        if statement:
            return statement
        
    def visitAssignment(self, ctx):
        # Get the text of the assignment
        assignment = ctx.getText()
        # If the assignment is not empty, return it
        if assignment:
            return assignment
    
    def visitExpression(self, ctx):
        # Get the text of the expression
        expression = ctx.getText()
        # If the expression is not empty, return it
        if expression:
            # make sure the expression has a space depending on what it is.
            # if it is a function call, it should have a space before the open paren
            # if it is a function definition, it should have a space before the open curly brace
            # if it is a function parameter, it should have a space before the comma
            # if it is a using statement, it should have a space after the using keyword
            if ctx.getChild(0).getText() == "struct":
                return "public static void" + expression
            
            elif ctx.getChild(0).getText() == re.compile(r'\w+\('):
                return "using " + expression
            
            else :
                return expression
            
    def visitFunction(self, ctx):
        # Get the text of the function
        function = ctx.getText()
        # If the function is not empty, return it
        if function:
            return function
        
    def visitFunctionCall(self, ctx):
        # Get the text of the function call
        functionCall = ctx.getText()
        # If the function call is not empty, return it
        if functionCall:
            return functionCall
        
    def visitFunctionName(self, ctx):
        # Get the text of the function name
        functionName = ctx.getText()
        # If the function name is not empty, return it
        if functionName:
            return functionName
        
    def visitFunctionParameters(self, ctx):
        # Get the text of the function parameters
        functionParameters = ctx.getText()
        # If the function parameters is not empty, return it
        if functionParameters:
            return functionParameters
        
    def visitFunctionParameter(self, ctx):
        # Get the text of the function parameter
        functionParameter = ctx.getText()
        # If the function parameter is not empty, return it
        if functionParameter:
            return functionParameter


def main():
    # Create a visitor and visit the tree
    visitor = MyTranspiler()
    code = visitor.visit(tree)
    
    # Print the result
    print(code)


main()


