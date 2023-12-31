# Generated from CubeScript.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CubeScriptParser import CubeScriptParser
else:
    from CubeScriptParser import CubeScriptParser

# This class defines a complete listener for a parse tree produced by CubeScriptParser.
class CubeScriptListener(ParseTreeListener):

    # Enter a parse tree produced by CubeScriptParser#program.
    def enterProgram(self, ctx:CubeScriptParser.ProgramContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#program.
    def exitProgram(self, ctx:CubeScriptParser.ProgramContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#line.
    def enterLine(self, ctx:CubeScriptParser.LineContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#line.
    def exitLine(self, ctx:CubeScriptParser.LineContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#assignmentexp.
    def enterAssignmentexp(self, ctx:CubeScriptParser.AssignmentexpContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#assignmentexp.
    def exitAssignmentexp(self, ctx:CubeScriptParser.AssignmentexpContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#functionCallExp.
    def enterFunctionCallExp(self, ctx:CubeScriptParser.FunctionCallExpContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#functionCallExp.
    def exitFunctionCallExp(self, ctx:CubeScriptParser.FunctionCallExpContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#ifblockexp.
    def enterIfblockexp(self, ctx:CubeScriptParser.IfblockexpContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#ifblockexp.
    def exitIfblockexp(self, ctx:CubeScriptParser.IfblockexpContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#whileblockexp.
    def enterWhileblockexp(self, ctx:CubeScriptParser.WhileblockexpContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#whileblockexp.
    def exitWhileblockexp(self, ctx:CubeScriptParser.WhileblockexpContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#forblockexp.
    def enterForblockexp(self, ctx:CubeScriptParser.ForblockexpContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#forblockexp.
    def exitForblockexp(self, ctx:CubeScriptParser.ForblockexpContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#breakexp.
    def enterBreakexp(self, ctx:CubeScriptParser.BreakexpContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#breakexp.
    def exitBreakexp(self, ctx:CubeScriptParser.BreakexpContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#returnstatementexp.
    def enterReturnstatementexp(self, ctx:CubeScriptParser.ReturnstatementexpContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#returnstatementexp.
    def exitReturnstatementexp(self, ctx:CubeScriptParser.ReturnstatementexpContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#expressionexp.
    def enterExpressionexp(self, ctx:CubeScriptParser.ExpressionexpContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#expressionexp.
    def exitExpressionexp(self, ctx:CubeScriptParser.ExpressionexpContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#commentexp.
    def enterCommentexp(self, ctx:CubeScriptParser.CommentexpContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#commentexp.
    def exitCommentexp(self, ctx:CubeScriptParser.CommentexpContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#usingStatementexp.
    def enterUsingStatementexp(self, ctx:CubeScriptParser.UsingStatementexpContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#usingStatementexp.
    def exitUsingStatementexp(self, ctx:CubeScriptParser.UsingStatementexpContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#importStatementexp.
    def enterImportStatementexp(self, ctx:CubeScriptParser.ImportStatementexpContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#importStatementexp.
    def exitImportStatementexp(self, ctx:CubeScriptParser.ImportStatementexpContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#includeStatementexp.
    def enterIncludeStatementexp(self, ctx:CubeScriptParser.IncludeStatementexpContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#includeStatementexp.
    def exitIncludeStatementexp(self, ctx:CubeScriptParser.IncludeStatementexpContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#arrayDeclarationexp.
    def enterArrayDeclarationexp(self, ctx:CubeScriptParser.ArrayDeclarationexpContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#arrayDeclarationexp.
    def exitArrayDeclarationexp(self, ctx:CubeScriptParser.ArrayDeclarationexpContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#switchBlockexp.
    def enterSwitchBlockexp(self, ctx:CubeScriptParser.SwitchBlockexpContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#switchBlockexp.
    def exitSwitchBlockexp(self, ctx:CubeScriptParser.SwitchBlockexpContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#functionblockexp.
    def enterFunctionblockexp(self, ctx:CubeScriptParser.FunctionblockexpContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#functionblockexp.
    def exitFunctionblockexp(self, ctx:CubeScriptParser.FunctionblockexpContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#assignment.
    def enterAssignment(self, ctx:CubeScriptParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#assignment.
    def exitAssignment(self, ctx:CubeScriptParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#ifBlock.
    def enterIfBlock(self, ctx:CubeScriptParser.IfBlockContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#ifBlock.
    def exitIfBlock(self, ctx:CubeScriptParser.IfBlockContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#whileBlock.
    def enterWhileBlock(self, ctx:CubeScriptParser.WhileBlockContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#whileBlock.
    def exitWhileBlock(self, ctx:CubeScriptParser.WhileBlockContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#parameterList.
    def enterParameterList(self, ctx:CubeScriptParser.ParameterListContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#parameterList.
    def exitParameterList(self, ctx:CubeScriptParser.ParameterListContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#functionBody.
    def enterFunctionBody(self, ctx:CubeScriptParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#functionBody.
    def exitFunctionBody(self, ctx:CubeScriptParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#functionCall.
    def enterFunctionCall(self, ctx:CubeScriptParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#functionCall.
    def exitFunctionCall(self, ctx:CubeScriptParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#forBlock.
    def enterForBlock(self, ctx:CubeScriptParser.ForBlockContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#forBlock.
    def exitForBlock(self, ctx:CubeScriptParser.ForBlockContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#codeBlock.
    def enterCodeBlock(self, ctx:CubeScriptParser.CodeBlockContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#codeBlock.
    def exitCodeBlock(self, ctx:CubeScriptParser.CodeBlockContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#functionblock.
    def enterFunctionblock(self, ctx:CubeScriptParser.FunctionblockContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#functionblock.
    def exitFunctionblock(self, ctx:CubeScriptParser.FunctionblockContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#returnstatement.
    def enterReturnstatement(self, ctx:CubeScriptParser.ReturnstatementContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#returnstatement.
    def exitReturnstatement(self, ctx:CubeScriptParser.ReturnstatementContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#importStatement.
    def enterImportStatement(self, ctx:CubeScriptParser.ImportStatementContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#importStatement.
    def exitImportStatement(self, ctx:CubeScriptParser.ImportStatementContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#includeStatement.
    def enterIncludeStatement(self, ctx:CubeScriptParser.IncludeStatementContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#includeStatement.
    def exitIncludeStatement(self, ctx:CubeScriptParser.IncludeStatementContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#arrayDeclaration.
    def enterArrayDeclaration(self, ctx:CubeScriptParser.ArrayDeclarationContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#arrayDeclaration.
    def exitArrayDeclaration(self, ctx:CubeScriptParser.ArrayDeclarationContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#usingStatement.
    def enterUsingStatement(self, ctx:CubeScriptParser.UsingStatementContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#usingStatement.
    def exitUsingStatement(self, ctx:CubeScriptParser.UsingStatementContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#expression.
    def enterExpression(self, ctx:CubeScriptParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#expression.
    def exitExpression(self, ctx:CubeScriptParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#multOp.
    def enterMultOp(self, ctx:CubeScriptParser.MultOpContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#multOp.
    def exitMultOp(self, ctx:CubeScriptParser.MultOpContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#addOp.
    def enterAddOp(self, ctx:CubeScriptParser.AddOpContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#addOp.
    def exitAddOp(self, ctx:CubeScriptParser.AddOpContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#cmpOp.
    def enterCmpOp(self, ctx:CubeScriptParser.CmpOpContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#cmpOp.
    def exitCmpOp(self, ctx:CubeScriptParser.CmpOpContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#boolOp.
    def enterBoolOp(self, ctx:CubeScriptParser.BoolOpContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#boolOp.
    def exitBoolOp(self, ctx:CubeScriptParser.BoolOpContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#constant.
    def enterConstant(self, ctx:CubeScriptParser.ConstantContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#constant.
    def exitConstant(self, ctx:CubeScriptParser.ConstantContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#break.
    def enterBreak(self, ctx:CubeScriptParser.BreakContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#break.
    def exitBreak(self, ctx:CubeScriptParser.BreakContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#switchBlock.
    def enterSwitchBlock(self, ctx:CubeScriptParser.SwitchBlockContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#switchBlock.
    def exitSwitchBlock(self, ctx:CubeScriptParser.SwitchBlockContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#switchCase.
    def enterSwitchCase(self, ctx:CubeScriptParser.SwitchCaseContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#switchCase.
    def exitSwitchCase(self, ctx:CubeScriptParser.SwitchCaseContext):
        pass


    # Enter a parse tree produced by CubeScriptParser#defaultCase.
    def enterDefaultCase(self, ctx:CubeScriptParser.DefaultCaseContext):
        pass

    # Exit a parse tree produced by CubeScriptParser#defaultCase.
    def exitDefaultCase(self, ctx:CubeScriptParser.DefaultCaseContext):
        pass



del CubeScriptParser