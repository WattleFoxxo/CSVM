//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     ANTLR Version: 4.13.1
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

// Generated from C:/Users/GAMER/source/repos/ProtoGram/CubeScript.g4 by ANTLR 4.13.1

// Unreachable code detected
#pragma warning disable 0162
// The variable '...' is assigned but its value is never used
#pragma warning disable 0219
// Missing XML comment for publicly visible type or member '...'
#pragma warning disable 1591
// Ambiguous reference in cref attribute
#pragma warning disable 419

using Antlr4.Runtime.Misc;
using IParseTreeListener = Antlr4.Runtime.Tree.IParseTreeListener;
using IToken = Antlr4.Runtime.IToken;

/// <summary>
/// This interface defines a complete listener for a parse tree produced by
/// <see cref="CubeScriptParser"/>.
/// </summary>
[System.CodeDom.Compiler.GeneratedCode("ANTLR", "4.13.1")]
[System.CLSCompliant(false)]
public interface ICubeScriptListener : IParseTreeListener {
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
	/// Enter a parse tree produced by the <c>assignmentexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterAssignmentexpr([NotNull] CubeScriptParser.AssignmentexprContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>assignmentexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitAssignmentexpr([NotNull] CubeScriptParser.AssignmentexprContext context);
	/// <summary>
	/// Enter a parse tree produced by the <c>importstatement</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterImportstatement([NotNull] CubeScriptParser.ImportstatementContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>importstatement</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitImportstatement([NotNull] CubeScriptParser.ImportstatementContext context);
	/// <summary>
	/// Enter a parse tree produced by the <c>forstatement</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterForstatement([NotNull] CubeScriptParser.ForstatementContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>forstatement</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitForstatement([NotNull] CubeScriptParser.ForstatementContext context);
	/// <summary>
	/// Enter a parse tree produced by the <c>functioncallstatment</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterFunctioncallstatment([NotNull] CubeScriptParser.FunctioncallstatmentContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>functioncallstatment</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitFunctioncallstatment([NotNull] CubeScriptParser.FunctioncallstatmentContext context);
	/// <summary>
	/// Enter a parse tree produced by the <c>functioncallstatement</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterFunctioncallstatement([NotNull] CubeScriptParser.FunctioncallstatementContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>functioncallstatement</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitFunctioncallstatement([NotNull] CubeScriptParser.FunctioncallstatementContext context);
	/// <summary>
	/// Enter a parse tree produced by the <c>foreachstatement</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterForeachstatement([NotNull] CubeScriptParser.ForeachstatementContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>foreachstatement</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitForeachstatement([NotNull] CubeScriptParser.ForeachstatementContext context);
	/// <summary>
	/// Enter a parse tree produced by the <c>varibledeclaration</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterVaribledeclaration([NotNull] CubeScriptParser.VaribledeclarationContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>varibledeclaration</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitVaribledeclaration([NotNull] CubeScriptParser.VaribledeclarationContext context);
	/// <summary>
	/// Enter a parse tree produced by the <c>stringarray</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterStringarray([NotNull] CubeScriptParser.StringarrayContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>stringarray</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitStringarray([NotNull] CubeScriptParser.StringarrayContext context);
	/// <summary>
	/// Enter a parse tree produced by the <c>returnstatement</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterReturnstatement([NotNull] CubeScriptParser.ReturnstatementContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>returnstatement</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitReturnstatement([NotNull] CubeScriptParser.ReturnstatementContext context);
	/// <summary>
	/// Enter a parse tree produced by the <c>breakstatement</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterBreakstatement([NotNull] CubeScriptParser.BreakstatementContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>breakstatement</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitBreakstatement([NotNull] CubeScriptParser.BreakstatementContext context);
	/// <summary>
	/// Enter a parse tree produced by the <c>continuestatement</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterContinuestatement([NotNull] CubeScriptParser.ContinuestatementContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>continuestatement</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitContinuestatement([NotNull] CubeScriptParser.ContinuestatementContext context);
	/// <summary>
	/// Enter a parse tree produced by the <c>housestatement</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterHousestatement([NotNull] CubeScriptParser.HousestatementContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>housestatement</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitHousestatement([NotNull] CubeScriptParser.HousestatementContext context);
	/// <summary>
	/// Enter a parse tree produced by the <c>arraydefinition</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterArraydefinition([NotNull] CubeScriptParser.ArraydefinitionContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>arraydefinition</c>
	/// labeled alternative in <see cref="CubeScriptParser.statement"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitArraydefinition([NotNull] CubeScriptParser.ArraydefinitionContext context);
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
	/// Enter a parse tree produced by the <c>functioncallexprs</c>
	/// labeled alternative in <see cref="CubeScriptParser.functionCall"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterFunctioncallexprs([NotNull] CubeScriptParser.FunctioncallexprsContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>functioncallexprs</c>
	/// labeled alternative in <see cref="CubeScriptParser.functionCall"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitFunctioncallexprs([NotNull] CubeScriptParser.FunctioncallexprsContext context);
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
	/// Enter a parse tree produced by the <c>ternaryexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterTernaryexpr([NotNull] CubeScriptParser.TernaryexprContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>ternaryexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitTernaryexpr([NotNull] CubeScriptParser.TernaryexprContext context);
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
	/// Enter a parse tree produced by the <c>decrementexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterDecrementexpr([NotNull] CubeScriptParser.DecrementexprContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>decrementexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitDecrementexpr([NotNull] CubeScriptParser.DecrementexprContext context);
	/// <summary>
	/// Enter a parse tree produced by the <c>incrementexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterIncrementexpr([NotNull] CubeScriptParser.IncrementexprContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>incrementexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitIncrementexpr([NotNull] CubeScriptParser.IncrementexprContext context);
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
	/// Enter a parse tree produced by the <c>dotexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterDotexpr([NotNull] CubeScriptParser.DotexprContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>dotexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitDotexpr([NotNull] CubeScriptParser.DotexprContext context);
	/// <summary>
	/// Enter a parse tree produced by the <c>arrayassignment</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterArrayassignment([NotNull] CubeScriptParser.ArrayassignmentContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>arrayassignment</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitArrayassignment([NotNull] CubeScriptParser.ArrayassignmentContext context);
	/// <summary>
	/// Enter a parse tree produced by the <c>identifierexpression</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterIdentifierexpression([NotNull] CubeScriptParser.IdentifierexpressionContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>identifierexpression</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitIdentifierexpression([NotNull] CubeScriptParser.IdentifierexpressionContext context);
	/// <summary>
	/// Enter a parse tree produced by the <c>dotfunctioncallexprs</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterDotfunctioncallexprs([NotNull] CubeScriptParser.DotfunctioncallexprsContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>dotfunctioncallexprs</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitDotfunctioncallexprs([NotNull] CubeScriptParser.DotfunctioncallexprsContext context);
	/// <summary>
	/// Enter a parse tree produced by the <c>arrayexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterArrayexpr([NotNull] CubeScriptParser.ArrayexprContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>arrayexpr</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitArrayexpr([NotNull] CubeScriptParser.ArrayexprContext context);
	/// <summary>
	/// Enter a parse tree produced by the <c>varibleassignment</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void EnterVaribleassignment([NotNull] CubeScriptParser.VaribleassignmentContext context);
	/// <summary>
	/// Exit a parse tree produced by the <c>varibleassignment</c>
	/// labeled alternative in <see cref="CubeScriptParser.expression"/>.
	/// </summary>
	/// <param name="context">The parse tree.</param>
	void ExitVaribleassignment([NotNull] CubeScriptParser.VaribleassignmentContext context);
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
}
