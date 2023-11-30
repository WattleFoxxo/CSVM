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


    # Visit a parse tree produced by CubeScriptParser#assignmentexpr.
    def visitAssignmentexpr(self, ctx:CubeScriptParser.AssignmentexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#usingstatement.
    def visitUsingstatement(self, ctx:CubeScriptParser.UsingstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#namespacestatement.
    def visitNamespacestatement(self, ctx:CubeScriptParser.NamespacestatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#classstatement.
    def visitClassstatement(self, ctx:CubeScriptParser.ClassstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#functiondefine.
    def visitFunctiondefine(self, ctx:CubeScriptParser.FunctiondefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#forloop.
    def visitForloop(self, ctx:CubeScriptParser.ForloopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#variblecallexprs.
    def visitVariblecallexprs(self, ctx:CubeScriptParser.VariblecallexprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#functionCallexprrr.
    def visitFunctionCallexprrr(self, ctx:CubeScriptParser.FunctionCallexprrrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#switchblockexprs.
    def visitSwitchblockexprs(self, ctx:CubeScriptParser.SwitchblockexprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#varibleexpr.
    def visitVaribleexpr(self, ctx:CubeScriptParser.VaribleexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#variblecallexprz.
    def visitVariblecallexprz(self, ctx:CubeScriptParser.VariblecallexprzContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#arraydefinition.
    def visitArraydefinition(self, ctx:CubeScriptParser.ArraydefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#stringarray.
    def visitStringarray(self, ctx:CubeScriptParser.StringarrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#structstatement.
    def visitStructstatement(self, ctx:CubeScriptParser.StructstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#switchBlock.
    def visitSwitchBlock(self, ctx:CubeScriptParser.SwitchBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#defaultCase.
    def visitDefaultCase(self, ctx:CubeScriptParser.DefaultCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#switchCase.
    def visitSwitchCase(self, ctx:CubeScriptParser.SwitchCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#ifBlock.
    def visitIfBlock(self, ctx:CubeScriptParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#ifStatement.
    def visitIfStatement(self, ctx:CubeScriptParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#elseifBlock.
    def visitElseifBlock(self, ctx:CubeScriptParser.ElseifBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#forBlock.
    def visitForBlock(self, ctx:CubeScriptParser.ForBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#foreachBlock.
    def visitForeachBlock(self, ctx:CubeScriptParser.ForeachBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#incrementOp.
    def visitIncrementOp(self, ctx:CubeScriptParser.IncrementOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#decrementOp.
    def visitDecrementOp(self, ctx:CubeScriptParser.DecrementOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#modifier.
    def visitModifier(self, ctx:CubeScriptParser.ModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#funcdef.
    def visitFuncdef(self, ctx:CubeScriptParser.FuncdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#forInit.
    def visitForInit(self, ctx:CubeScriptParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#forUpdate.
    def visitForUpdate(self, ctx:CubeScriptParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#whileBlock.
    def visitWhileBlock(self, ctx:CubeScriptParser.WhileBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#functiondefinition.
    def visitFunctiondefinition(self, ctx:CubeScriptParser.FunctiondefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#param.
    def visitParam(self, ctx:CubeScriptParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#assignment.
    def visitAssignment(self, ctx:CubeScriptParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#usingStatement.
    def visitUsingStatement(self, ctx:CubeScriptParser.UsingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#functionCallexprr.
    def visitFunctionCallexprr(self, ctx:CubeScriptParser.FunctionCallexprrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#variblecallexpr.
    def visitVariblecallexpr(self, ctx:CubeScriptParser.VariblecallexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#block.
    def visitBlock(self, ctx:CubeScriptParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#functionCallexprs.
    def visitFunctionCallexprs(self, ctx:CubeScriptParser.FunctionCallexprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#statementexpr.
    def visitStatementexpr(self, ctx:CubeScriptParser.StatementexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#ternaryexpr.
    def visitTernaryexpr(self, ctx:CubeScriptParser.TernaryexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#ifstatementexpr.
    def visitIfstatementexpr(self, ctx:CubeScriptParser.IfstatementexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#dotfunctionCallexprs.
    def visitDotfunctionCallexprs(self, ctx:CubeScriptParser.DotfunctionCallexprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#functionCallexpr.
    def visitFunctionCallexpr(self, ctx:CubeScriptParser.FunctionCallexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#constantexpr.
    def visitConstantexpr(self, ctx:CubeScriptParser.ConstantexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#foreachblockexpr.
    def visitForeachblockexpr(self, ctx:CubeScriptParser.ForeachblockexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#parenthesisexpr.
    def visitParenthesisexpr(self, ctx:CubeScriptParser.ParenthesisexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#decrementexpr.
    def visitDecrementexpr(self, ctx:CubeScriptParser.DecrementexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#incrementexpr.
    def visitIncrementexpr(self, ctx:CubeScriptParser.IncrementexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#negationexpr.
    def visitNegationexpr(self, ctx:CubeScriptParser.NegationexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#functiondefineexpr.
    def visitFunctiondefineexpr(self, ctx:CubeScriptParser.FunctiondefineexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#identifiereexpr.
    def visitIdentifiereexpr(self, ctx:CubeScriptParser.IdentifiereexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#dotexpr.
    def visitDotexpr(self, ctx:CubeScriptParser.DotexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#arrayassignment.
    def visitArrayassignment(self, ctx:CubeScriptParser.ArrayassignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#forblockexpr.
    def visitForblockexpr(self, ctx:CubeScriptParser.ForblockexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#arrayexpr.
    def visitArrayexpr(self, ctx:CubeScriptParser.ArrayexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#switchblockexpr.
    def visitSwitchblockexpr(self, ctx:CubeScriptParser.SwitchblockexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#binaryexpr.
    def visitBinaryexpr(self, ctx:CubeScriptParser.BinaryexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CubeScriptParser#whileblockexpr.
    def visitWhileblockexpr(self, ctx:CubeScriptParser.WhileblockexprContext):
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



del CubeScriptParser