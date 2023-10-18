//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     ANTLR Version: 4.6.6
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

// Generated from C:\Users\GAMER\source\repos\ProtoGram\CubeScript.g4 by ANTLR 4.6.6

// Unreachable code detected
#pragma warning disable 0162
// The variable '...' is assigned but its value is never used
#pragma warning disable 0219
// Missing XML comment for publicly visible type or member '...'
#pragma warning disable 1591
// Ambiguous reference in cref attribute
#pragma warning disable 419

namespace ProtoGram {
using Antlr4.Runtime.Misc;
using IParseTreeListener = Antlr4.Runtime.Tree.IParseTreeListener;
using IToken = Antlr4.Runtime.IToken;

/// <summary>
/// This interface defines a complete listener for a parse tree produced by
/// <see cref="CubeScriptParser"/>.
/// </summary>
[System.CodeDom.Compiler.GeneratedCode("ANTLR", "4.6.6")]
[System.CLSCompliant(false)]
public interface ICubeScriptListener : IParseTreeListener {
	/// <summary>
	/// Enter a parse tree produced by the <c>identifierexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterIdentifierexpr([NotNull] CubeScriptParser.IdentifierexprContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>identifierexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitIdentifierexpr([NotNull] CubeScriptParser.IdentifierexprContext context);

	/// <summary>
	/// Enter a parse tree produced by the <c>notexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterNotexpr([NotNull] CubeScriptParser.NotexprContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>notexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitNotexpr([NotNull] CubeScriptParser.NotexprContext context);

	/// <summary>
	/// Enter a parse tree produced by the <c>multexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterMultexpr([NotNull] CubeScriptParser.MultexprContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>multexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitMultexpr([NotNull] CubeScriptParser.MultexprContext context);

	/// <summary>
	/// Enter a parse tree produced by the <c>addexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterAddexpr([NotNull] CubeScriptParser.AddexprContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>addexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitAddexpr([NotNull] CubeScriptParser.AddexprContext context);

	/// <summary>
	/// Enter a parse tree produced by the <c>cmpexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterCmpexpr([NotNull] CubeScriptParser.CmpexprContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>cmpexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitCmpexpr([NotNull] CubeScriptParser.CmpexprContext context);

	/// <summary>
	/// Enter a parse tree produced by the <c>constantexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterConstantexpr([NotNull] CubeScriptParser.ConstantexprContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>constantexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitConstantexpr([NotNull] CubeScriptParser.ConstantexprContext context);

	/// <summary>
	/// Enter a parse tree produced by the <c>functioncallexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterFunctioncallexpr([NotNull] CubeScriptParser.FunctioncallexprContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>functioncallexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitFunctioncallexpr([NotNull] CubeScriptParser.FunctioncallexprContext context);

	/// <summary>
	/// Enter a parse tree produced by the <c>boolexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterBoolexpr([NotNull] CubeScriptParser.BoolexprContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>boolexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitBoolexpr([NotNull] CubeScriptParser.BoolexprContext context);

	/// <summary>
	/// Enter a parse tree produced by the <c>parenthesisexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterParenthesisexpr([NotNull] CubeScriptParser.ParenthesisexprContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>parenthesisexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitParenthesisexpr([NotNull] CubeScriptParser.ParenthesisexprContext context);

	/// <summary>
	/// Enter a parse tree produced by <see cref="CubeScriptParser.program"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterProgram([NotNull] CubeScriptParser.ProgramContext context);
	/// <summary>
	/// Exit a parse tree produced by <see cref="CubeScriptParser.program"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitProgram([NotNull] CubeScriptParser.ProgramContext context);

	/// <summary>
	/// Enter a parse tree produced by <see cref="CubeScriptParser.line"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterLine([NotNull] CubeScriptParser.LineContext context);
	/// <summary>
	/// Exit a parse tree produced by <see cref="CubeScriptParser.line"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitLine([NotNull] CubeScriptParser.LineContext context);

	/// <summary>
	/// Enter a parse tree produced by <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterStatement([NotNull] CubeScriptParser.StatementContext context);
	/// <summary>
	/// Exit a parse tree produced by <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitStatement([NotNull] CubeScriptParser.StatementContext context);

	/// <summary>
	/// Enter a parse tree produced by <see cref="CubeScriptParser.ifBlock"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterIfBlock([NotNull] CubeScriptParser.IfBlockContext context);
	/// <summary>
	/// Exit a parse tree produced by <see cref="CubeScriptParser.ifBlock"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitIfBlock([NotNull] CubeScriptParser.IfBlockContext context);

	/// <summary>
	/// Enter a parse tree produced by <see cref="CubeScriptParser.elseifBlock"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterElseifBlock([NotNull] CubeScriptParser.ElseifBlockContext context);
	/// <summary>
	/// Exit a parse tree produced by <see cref="CubeScriptParser.elseifBlock"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitElseifBlock([NotNull] CubeScriptParser.ElseifBlockContext context);

	/// <summary>
	/// Enter a parse tree produced by <see cref="CubeScriptParser.whileBlock"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterWhileBlock([NotNull] CubeScriptParser.WhileBlockContext context);
	/// <summary>
	/// Exit a parse tree produced by <see cref="CubeScriptParser.whileBlock"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitWhileBlock([NotNull] CubeScriptParser.WhileBlockContext context);

	/// <summary>
	/// Enter a parse tree produced by <see cref="CubeScriptParser.assignment"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterAssignment([NotNull] CubeScriptParser.AssignmentContext context);
	/// <summary>
	/// Exit a parse tree produced by <see cref="CubeScriptParser.assignment"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitAssignment([NotNull] CubeScriptParser.AssignmentContext context);

	/// <summary>
	/// Enter a parse tree produced by <see cref="CubeScriptParser.functionCall"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterFunctionCall([NotNull] CubeScriptParser.FunctionCallContext context);
	/// <summary>
	/// Exit a parse tree produced by <see cref="CubeScriptParser.functionCall"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitFunctionCall([NotNull] CubeScriptParser.FunctionCallContext context);

	/// <summary>
	/// Enter a parse tree produced by <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterExpression([NotNull] CubeScriptParser.ExpressionContext context);
	/// <summary>
	/// Exit a parse tree produced by <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitExpression([NotNull] CubeScriptParser.ExpressionContext context);

	/// <summary>
	/// Enter a parse tree produced by <see cref="CubeScriptParser.multOp"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterMultOp([NotNull] CubeScriptParser.MultOpContext context);
	/// <summary>
	/// Exit a parse tree produced by <see cref="CubeScriptParser.multOp"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitMultOp([NotNull] CubeScriptParser.MultOpContext context);

	/// <summary>
	/// Enter a parse tree produced by <see cref="CubeScriptParser.addOp"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterAddOp([NotNull] CubeScriptParser.AddOpContext context);
	/// <summary>
	/// Exit a parse tree produced by <see cref="CubeScriptParser.addOp"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitAddOp([NotNull] CubeScriptParser.AddOpContext context);

	/// <summary>
	/// Enter a parse tree produced by <see cref="CubeScriptParser.cmpOp"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterCmpOp([NotNull] CubeScriptParser.CmpOpContext context);
	/// <summary>
	/// Exit a parse tree produced by <see cref="CubeScriptParser.cmpOp"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitCmpOp([NotNull] CubeScriptParser.CmpOpContext context);

	/// <summary>
	/// Enter a parse tree produced by <see cref="CubeScriptParser.boolOp"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterBoolOp([NotNull] CubeScriptParser.BoolOpContext context);
	/// <summary>
	/// Exit a parse tree produced by <see cref="CubeScriptParser.boolOp"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitBoolOp([NotNull] CubeScriptParser.BoolOpContext context);

	/// <summary>
	/// Enter a parse tree produced by <see cref="CubeScriptParser.constant"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterConstant([NotNull] CubeScriptParser.ConstantContext context);
	/// <summary>
	/// Exit a parse tree produced by <see cref="CubeScriptParser.constant"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitConstant([NotNull] CubeScriptParser.ConstantContext context);

	/// <summary>
	/// Enter a parse tree produced by <see cref="CubeScriptParser.block"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterBlock([NotNull] CubeScriptParser.BlockContext context);
	/// <summary>
	/// Exit a parse tree produced by <see cref="CubeScriptParser.block"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitBlock([NotNull] CubeScriptParser.BlockContext context);
}
} // namespace ProtoGram
