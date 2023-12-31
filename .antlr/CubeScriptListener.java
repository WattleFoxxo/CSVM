// Generated from d://postreset//repos//CSVM//CubeScript.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CubeScriptParser}.
 */
public interface CubeScriptListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(CubeScriptParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(CubeScriptParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#line}.
	 * @param ctx the parse tree
	 */
	void enterLine(CubeScriptParser.LineContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#line}.
	 * @param ctx the parse tree
	 */
	void exitLine(CubeScriptParser.LineContext ctx);
	/**
	 * Enter a parse tree produced by the {@code assignmentexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentexp(CubeScriptParser.AssignmentexpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code assignmentexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentexp(CubeScriptParser.AssignmentexpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code functionCallExp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCallExp(CubeScriptParser.FunctionCallExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code functionCallExp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCallExp(CubeScriptParser.FunctionCallExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ifblockexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterIfblockexp(CubeScriptParser.IfblockexpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ifblockexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitIfblockexp(CubeScriptParser.IfblockexpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code whileblockexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterWhileblockexp(CubeScriptParser.WhileblockexpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code whileblockexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitWhileblockexp(CubeScriptParser.WhileblockexpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code forblockexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterForblockexp(CubeScriptParser.ForblockexpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code forblockexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitForblockexp(CubeScriptParser.ForblockexpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code breakexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterBreakexp(CubeScriptParser.BreakexpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code breakexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitBreakexp(CubeScriptParser.BreakexpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code returnstatementexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterReturnstatementexp(CubeScriptParser.ReturnstatementexpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code returnstatementexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitReturnstatementexp(CubeScriptParser.ReturnstatementexpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code expressionexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterExpressionexp(CubeScriptParser.ExpressionexpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code expressionexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitExpressionexp(CubeScriptParser.ExpressionexpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code commentexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterCommentexp(CubeScriptParser.CommentexpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code commentexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitCommentexp(CubeScriptParser.CommentexpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code usingStatementexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterUsingStatementexp(CubeScriptParser.UsingStatementexpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code usingStatementexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitUsingStatementexp(CubeScriptParser.UsingStatementexpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code importStatementexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterImportStatementexp(CubeScriptParser.ImportStatementexpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code importStatementexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitImportStatementexp(CubeScriptParser.ImportStatementexpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code includeStatementexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterIncludeStatementexp(CubeScriptParser.IncludeStatementexpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code includeStatementexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitIncludeStatementexp(CubeScriptParser.IncludeStatementexpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code arrayDeclarationexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterArrayDeclarationexp(CubeScriptParser.ArrayDeclarationexpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code arrayDeclarationexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitArrayDeclarationexp(CubeScriptParser.ArrayDeclarationexpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code switchBlockexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterSwitchBlockexp(CubeScriptParser.SwitchBlockexpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code switchBlockexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitSwitchBlockexp(CubeScriptParser.SwitchBlockexpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code functionblockexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterFunctionblockexp(CubeScriptParser.FunctionblockexpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code functionblockexp}
	 * labeled alternative in {@link CubeScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitFunctionblockexp(CubeScriptParser.FunctionblockexpContext ctx);
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(CubeScriptParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(CubeScriptParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#ifBlock}.
	 * @param ctx the parse tree
	 */
	void enterIfBlock(CubeScriptParser.IfBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#ifBlock}.
	 * @param ctx the parse tree
	 */
	void exitIfBlock(CubeScriptParser.IfBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#whileBlock}.
	 * @param ctx the parse tree
	 */
	void enterWhileBlock(CubeScriptParser.WhileBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#whileBlock}.
	 * @param ctx the parse tree
	 */
	void exitWhileBlock(CubeScriptParser.WhileBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCall(CubeScriptParser.FunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCall(CubeScriptParser.FunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#forBlock}.
	 * @param ctx the parse tree
	 */
	void enterForBlock(CubeScriptParser.ForBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#forBlock}.
	 * @param ctx the parse tree
	 */
	void exitForBlock(CubeScriptParser.ForBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#codeBlock}.
	 * @param ctx the parse tree
	 */
	void enterCodeBlock(CubeScriptParser.CodeBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#codeBlock}.
	 * @param ctx the parse tree
	 */
	void exitCodeBlock(CubeScriptParser.CodeBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#functionblock}.
	 * @param ctx the parse tree
	 */
	void enterFunctionblock(CubeScriptParser.FunctionblockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#functionblock}.
	 * @param ctx the parse tree
	 */
	void exitFunctionblock(CubeScriptParser.FunctionblockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#returnstatement}.
	 * @param ctx the parse tree
	 */
	void enterReturnstatement(CubeScriptParser.ReturnstatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#returnstatement}.
	 * @param ctx the parse tree
	 */
	void exitReturnstatement(CubeScriptParser.ReturnstatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#importStatement}.
	 * @param ctx the parse tree
	 */
	void enterImportStatement(CubeScriptParser.ImportStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#importStatement}.
	 * @param ctx the parse tree
	 */
	void exitImportStatement(CubeScriptParser.ImportStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#includeStatement}.
	 * @param ctx the parse tree
	 */
	void enterIncludeStatement(CubeScriptParser.IncludeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#includeStatement}.
	 * @param ctx the parse tree
	 */
	void exitIncludeStatement(CubeScriptParser.IncludeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#arrayDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterArrayDeclaration(CubeScriptParser.ArrayDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#arrayDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitArrayDeclaration(CubeScriptParser.ArrayDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#usingStatement}.
	 * @param ctx the parse tree
	 */
	void enterUsingStatement(CubeScriptParser.UsingStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#usingStatement}.
	 * @param ctx the parse tree
	 */
	void exitUsingStatement(CubeScriptParser.UsingStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(CubeScriptParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(CubeScriptParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#multOp}.
	 * @param ctx the parse tree
	 */
	void enterMultOp(CubeScriptParser.MultOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#multOp}.
	 * @param ctx the parse tree
	 */
	void exitMultOp(CubeScriptParser.MultOpContext ctx);
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#addOp}.
	 * @param ctx the parse tree
	 */
	void enterAddOp(CubeScriptParser.AddOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#addOp}.
	 * @param ctx the parse tree
	 */
	void exitAddOp(CubeScriptParser.AddOpContext ctx);
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#cmpOp}.
	 * @param ctx the parse tree
	 */
	void enterCmpOp(CubeScriptParser.CmpOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#cmpOp}.
	 * @param ctx the parse tree
	 */
	void exitCmpOp(CubeScriptParser.CmpOpContext ctx);
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#boolOp}.
	 * @param ctx the parse tree
	 */
	void enterBoolOp(CubeScriptParser.BoolOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#boolOp}.
	 * @param ctx the parse tree
	 */
	void exitBoolOp(CubeScriptParser.BoolOpContext ctx);
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#constant}.
	 * @param ctx the parse tree
	 */
	void enterConstant(CubeScriptParser.ConstantContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#constant}.
	 * @param ctx the parse tree
	 */
	void exitConstant(CubeScriptParser.ConstantContext ctx);
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#break}.
	 * @param ctx the parse tree
	 */
	void enterBreak(CubeScriptParser.BreakContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#break}.
	 * @param ctx the parse tree
	 */
	void exitBreak(CubeScriptParser.BreakContext ctx);
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#switchBlock}.
	 * @param ctx the parse tree
	 */
	void enterSwitchBlock(CubeScriptParser.SwitchBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#switchBlock}.
	 * @param ctx the parse tree
	 */
	void exitSwitchBlock(CubeScriptParser.SwitchBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#switchCase}.
	 * @param ctx the parse tree
	 */
	void enterSwitchCase(CubeScriptParser.SwitchCaseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#switchCase}.
	 * @param ctx the parse tree
	 */
	void exitSwitchCase(CubeScriptParser.SwitchCaseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CubeScriptParser#defaultCase}.
	 * @param ctx the parse tree
	 */
	void enterDefaultCase(CubeScriptParser.DefaultCaseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CubeScriptParser#defaultCase}.
	 * @param ctx the parse tree
	 */
	void exitDefaultCase(CubeScriptParser.DefaultCaseContext ctx);
}