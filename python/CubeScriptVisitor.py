# Generated from CubeScript.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CubeScriptParser import CubeScriptParser
else:
    from CubeScriptParser import CubeScriptParser

# This class defines a complete generic visitor for a parse tree produced by CubeScriptParser.

class CubeScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CubeScriptParser#program.
    def visitProgram(self, ctx:CubeScriptParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#line.
    def visitLine(self, ctx:CubeScriptParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#assignmentexp.
    def visitAssignmentexp(self, ctx:CubeScriptParser.AssignmentexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#functionCallExp.
    def visitFunctionCallExp(self, ctx:CubeScriptParser.FunctionCallExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#ifblockexp.
    def visitIfblockexp(self, ctx:CubeScriptParser.IfblockexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#whileblockexp.
    def visitWhileblockexp(self, ctx:CubeScriptParser.WhileblockexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#forblockexp.
    def visitForblockexp(self, ctx:CubeScriptParser.ForblockexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#breakexp.
    def visitBreakexp(self, ctx:CubeScriptParser.BreakexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#returnstatementexp.
    def visitReturnstatementexp(self, ctx:CubeScriptParser.ReturnstatementexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#expressionexp.
    def visitExpressionexp(self, ctx:CubeScriptParser.ExpressionexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#commentexp.
    def visitCommentexp(self, ctx:CubeScriptParser.CommentexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#usingStatementexp.
    def visitUsingStatementexp(self, ctx:CubeScriptParser.UsingStatementexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#importStatementexp.
    def visitImportStatementexp(self, ctx:CubeScriptParser.ImportStatementexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#includeStatementexp.
    def visitIncludeStatementexp(self, ctx:CubeScriptParser.IncludeStatementexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#arrayDeclarationexp.
    def visitArrayDeclarationexp(self, ctx:CubeScriptParser.ArrayDeclarationexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#switchBlockexp.
    def visitSwitchBlockexp(self, ctx:CubeScriptParser.SwitchBlockexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#functionblockexp.
    def visitFunctionblockexp(self, ctx:CubeScriptParser.FunctionblockexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#assignment.
    def visitAssignment(self, ctx:CubeScriptParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#ifBlock.
    def visitIfBlock(self, ctx:CubeScriptParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#whileBlock.
    def visitWhileBlock(self, ctx:CubeScriptParser.WhileBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#parameterList.
    def visitParameterList(self, ctx:CubeScriptParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#functionBody.
    def visitFunctionBody(self, ctx:CubeScriptParser.FunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#functionCall.
    def visitFunctionCall(self, ctx:CubeScriptParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#forBlock.
    def visitForBlock(self, ctx:CubeScriptParser.ForBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#codeBlock.
    def visitCodeBlock(self, ctx:CubeScriptParser.CodeBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#functionblock.
    def visitFunctionblock(self, ctx:CubeScriptParser.FunctionblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#returnstatement.
    def visitReturnstatement(self, ctx:CubeScriptParser.ReturnstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#importStatement.
    def visitImportStatement(self, ctx:CubeScriptParser.ImportStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#includeStatement.
    def visitIncludeStatement(self, ctx:CubeScriptParser.IncludeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#arrayDeclaration.
    def visitArrayDeclaration(self, ctx:CubeScriptParser.ArrayDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#usingStatement.
    def visitUsingStatement(self, ctx:CubeScriptParser.UsingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#expression.
    def visitExpression(self, ctx:CubeScriptParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#multOp.
    def visitMultOp(self, ctx:CubeScriptParser.MultOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#addOp.
    def visitAddOp(self, ctx:CubeScriptParser.AddOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#cmpOp.
    def visitCmpOp(self, ctx:CubeScriptParser.CmpOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#boolOp.
    def visitBoolOp(self, ctx:CubeScriptParser.BoolOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#constant.
    def visitConstant(self, ctx:CubeScriptParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#break.
    def visitBreak(self, ctx:CubeScriptParser.BreakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#switchBlock.
    def visitSwitchBlock(self, ctx:CubeScriptParser.SwitchBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#switchCase.
    def visitSwitchCase(self, ctx:CubeScriptParser.SwitchCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#defaultCase.
    def visitDefaultCase(self, ctx:CubeScriptParser.DefaultCaseContext):
        return self.visitChildren(ctx)



del CubeScriptParser