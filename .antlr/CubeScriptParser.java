// Generated from c:/Users/GAMER/source/repos/CSVM/cubescript.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class cubescriptParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39, T__39=40, T__40=41, T__41=42, T__42=43, T__43=44, T__44=45, 
		WHILE=46, ARRAY=47, Comment=48, BOOL_OPERATOR=49, INTEGER=50, FLOAT=51, 
		IMPORT=52, STRING=53, BOOL=54, TYPE=55, WS=56, IDENTIFIER=57;
	public static final int
		RULE_program = 0, RULE_line = 1, RULE_statement = 2, RULE_switchBlock = 3, 
		RULE_defaultCase = 4, RULE_switchCase = 5, RULE_ifBlock = 6, RULE_elseifBlock = 7, 
		RULE_whileBlock = 8, RULE_functiondefinition = 9, RULE_param = 10, RULE_assignment = 11, 
		RULE_functionCall = 12, RULE_block = 13, RULE_expression = 14, RULE_multOp = 15, 
		RULE_addOp = 16, RULE_cmpOp = 17, RULE_boolOp = 18, RULE_constant = 19;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "line", "statement", "switchBlock", "defaultCase", "switchCase", 
			"ifBlock", "elseifBlock", "whileBlock", "functiondefinition", "param", 
			"assignment", "functionCall", "block", "expression", "multOp", "addOp", 
			"cmpOp", "boolOp", "constant"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'.'", "'house'", "'{'", "'}'", "'for'", "'('", "'>'", "')'", 
			"'<'", "'='", "'['", "','", "']'", "'switch'", "'bland'", "':'", "'stop;'", 
			"'at'", "'if'", "'else'", "'struct'", "'-'", "'!'", "'?'", "'++'", "'--'", 
			"'*'", "'/'", "'%'", "'^'", "'<<'", "'>>'", "'&'", "'|'", "'&&'", "'||'", 
			"'+='", "'-='", "'*='", "'+'", "'<='", "'>='", "'=='", "'!='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, "WHILE", 
			"ARRAY", "Comment", "BOOL_OPERATOR", "INTEGER", "FLOAT", "IMPORT", "STRING", 
			"BOOL", "TYPE", "WS", "IDENTIFIER"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "cubescript.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public cubescriptParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(cubescriptParser.EOF, 0); }
		public List<LineContext> line() {
			return getRuleContexts(LineContext.class);
		}
		public LineContext line(int i) {
			return getRuleContext(LineContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(43);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 215539463421429832L) != 0)) {
				{
				{
				setState(40);
				line();
				}
				}
				setState(45);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(46);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LineContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public IfBlockContext ifBlock() {
			return getRuleContext(IfBlockContext.class,0);
		}
		public WhileBlockContext whileBlock() {
			return getRuleContext(WhileBlockContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode Comment() { return getToken(cubescriptParser.Comment, 0); }
		public LineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_line; }
	}

	public final LineContext line() throws RecognitionException {
		LineContext _localctx = new LineContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_line);
		try {
			setState(54);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__2:
			case T__5:
			case T__10:
			case T__21:
			case ARRAY:
			case INTEGER:
			case FLOAT:
			case IMPORT:
			case STRING:
			case BOOL:
			case TYPE:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(48);
				statement();
				}
				break;
			case T__19:
				enterOuterAlt(_localctx, 2);
				{
				setState(49);
				ifBlock();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 3);
				{
				setState(50);
				whileBlock();
				setState(51);
				expression(0);
				}
				break;
			case Comment:
				enterOuterAlt(_localctx, 4);
				{
				setState(53);
				match(Comment);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	 
		public StatementContext() { }
		public void copyFrom(StatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FunctiondefineContext extends StatementContext {
		public FunctiondefinitionContext functiondefinition() {
			return getRuleContext(FunctiondefinitionContext.class,0);
		}
		public FunctiondefineContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FunctioncallexprrContext extends StatementContext {
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public FunctioncallexprrContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentexprContext extends StatementContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public AssignmentexprContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ForloopContext extends StatementContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(cubescriptParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(cubescriptParser.IDENTIFIER, i);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ForloopContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ImportstatementContext extends StatementContext {
		public TerminalNode IMPORT() { return getToken(cubescriptParser.IMPORT, 0); }
		public List<TerminalNode> IDENTIFIER() { return getTokens(cubescriptParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(cubescriptParser.IDENTIFIER, i);
		}
		public ImportstatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NamespacestatementContext extends StatementContext {
		public TerminalNode IDENTIFIER() { return getToken(cubescriptParser.IDENTIFIER, 0); }
		public List<LineContext> line() {
			return getRuleContexts(LineContext.class);
		}
		public LineContext line(int i) {
			return getRuleContext(LineContext.class,i);
		}
		public NamespacestatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VariblecallexprContext extends StatementContext {
		public TerminalNode TYPE() { return getToken(cubescriptParser.TYPE, 0); }
		public TerminalNode IDENTIFIER() { return getToken(cubescriptParser.IDENTIFIER, 0); }
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public VariblecallexprContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StringarrayContext extends StatementContext {
		public TerminalNode TYPE() { return getToken(cubescriptParser.TYPE, 0); }
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public List<TerminalNode> IDENTIFIER() { return getTokens(cubescriptParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(cubescriptParser.IDENTIFIER, i);
		}
		public TerminalNode ARRAY() { return getToken(cubescriptParser.ARRAY, 0); }
		public StringarrayContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ArraydefinitionContext extends StatementContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(cubescriptParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(cubescriptParser.IDENTIFIER, i);
		}
		public ConstantContext constant() {
			return getRuleContext(ConstantContext.class,0);
		}
		public TerminalNode ARRAY() { return getToken(cubescriptParser.ARRAY, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ArraydefinitionContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VaribleexprContext extends StatementContext {
		public TerminalNode IDENTIFIER() { return getToken(cubescriptParser.IDENTIFIER, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode TYPE() { return getToken(cubescriptParser.TYPE, 0); }
		public VaribleexprContext(StatementContext ctx) { copyFrom(ctx); }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_statement);
		int _la;
		try {
			setState(150);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				_localctx = new AssignmentexprContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(56);
				assignment();
				}
				break;
			case 2:
				_localctx = new ImportstatementContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(57);
				match(IMPORT);
				setState(58);
				match(IDENTIFIER);
				setState(59);
				match(T__0);
				}
				break;
			case 3:
				_localctx = new ImportstatementContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(60);
				match(IMPORT);
				setState(61);
				match(IDENTIFIER);
				setState(62);
				match(T__1);
				setState(63);
				match(IDENTIFIER);
				setState(64);
				match(T__0);
				}
				break;
			case 4:
				_localctx = new NamespacestatementContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(65);
				match(T__2);
				setState(66);
				match(IDENTIFIER);
				setState(67);
				match(T__3);
				setState(71);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 215539463421429832L) != 0)) {
					{
					{
					setState(68);
					line();
					}
					}
					setState(73);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(74);
				match(T__4);
				}
				break;
			case 5:
				_localctx = new FunctiondefineContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(75);
				functiondefinition();
				}
				break;
			case 6:
				_localctx = new ForloopContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(76);
				match(T__5);
				setState(77);
				match(T__6);
				setState(78);
				match(IDENTIFIER);
				setState(79);
				match(T__7);
				setState(80);
				match(IDENTIFIER);
				setState(81);
				match(T__8);
				setState(82);
				block();
				}
				break;
			case 7:
				_localctx = new ForloopContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(83);
				match(T__5);
				setState(84);
				match(T__6);
				setState(85);
				match(IDENTIFIER);
				setState(86);
				match(T__9);
				setState(87);
				match(IDENTIFIER);
				setState(88);
				match(T__8);
				setState(89);
				block();
				}
				break;
			case 8:
				_localctx = new VariblecallexprContext(_localctx);
				enterOuterAlt(_localctx, 8);
				{
				setState(90);
				match(TYPE);
				setState(91);
				match(IDENTIFIER);
				setState(92);
				match(T__10);
				setState(93);
				functionCall();
				setState(94);
				match(T__0);
				}
				break;
			case 9:
				_localctx = new FunctioncallexprrContext(_localctx);
				enterOuterAlt(_localctx, 9);
				{
				setState(96);
				functionCall();
				setState(97);
				match(T__0);
				}
				break;
			case 10:
				_localctx = new VaribleexprContext(_localctx);
				enterOuterAlt(_localctx, 10);
				{
				setState(99);
				match(IDENTIFIER);
				setState(100);
				match(T__10);
				setState(101);
				expression(0);
				setState(102);
				match(T__0);
				}
				break;
			case 11:
				_localctx = new VaribleexprContext(_localctx);
				enterOuterAlt(_localctx, 11);
				{
				setState(104);
				match(TYPE);
				setState(105);
				match(IDENTIFIER);
				setState(106);
				match(T__10);
				setState(107);
				expression(0);
				setState(108);
				match(T__0);
				}
				break;
			case 12:
				_localctx = new StringarrayContext(_localctx);
				enterOuterAlt(_localctx, 12);
				{
				setState(111);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==IDENTIFIER) {
					{
					setState(110);
					match(IDENTIFIER);
					}
				}

				setState(113);
				match(TYPE);
				setState(115);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==IDENTIFIER) {
					{
					setState(114);
					match(IDENTIFIER);
					}
				}

				setState(118);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ARRAY) {
					{
					setState(117);
					match(ARRAY);
					}
				}

				setState(120);
				match(T__10);
				setState(121);
				functionCall();
				setState(122);
				match(T__0);
				}
				break;
			case 13:
				_localctx = new ArraydefinitionContext(_localctx);
				enterOuterAlt(_localctx, 13);
				{
				setState(125);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
				case 1:
					{
					setState(124);
					match(IDENTIFIER);
					}
					break;
				}
				setState(128);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
				case 1:
					{
					setState(127);
					constant();
					}
					break;
				}
				setState(131);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==IDENTIFIER) {
					{
					setState(130);
					match(IDENTIFIER);
					}
				}

				setState(134);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ARRAY) {
					{
					setState(133);
					match(ARRAY);
					}
				}

				setState(136);
				match(T__10);
				setState(137);
				match(T__11);
				setState(146);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 210543282604736640L) != 0)) {
					{
					setState(138);
					expression(0);
					setState(143);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__12) {
						{
						{
						setState(139);
						match(T__12);
						setState(140);
						expression(0);
						}
						}
						setState(145);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(148);
				match(T__13);
				setState(149);
				match(T__0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SwitchBlockContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<SwitchCaseContext> switchCase() {
			return getRuleContexts(SwitchCaseContext.class);
		}
		public SwitchCaseContext switchCase(int i) {
			return getRuleContext(SwitchCaseContext.class,i);
		}
		public DefaultCaseContext defaultCase() {
			return getRuleContext(DefaultCaseContext.class,0);
		}
		public SwitchBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_switchBlock; }
	}

	public final SwitchBlockContext switchBlock() throws RecognitionException {
		SwitchBlockContext _localctx = new SwitchBlockContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_switchBlock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(152);
			match(T__14);
			setState(153);
			match(T__6);
			setState(154);
			expression(0);
			setState(155);
			match(T__8);
			setState(156);
			match(T__3);
			setState(160);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__18) {
				{
				{
				setState(157);
				switchCase();
				}
				}
				setState(162);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(164);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__15) {
				{
				setState(163);
				defaultCase();
				}
			}

			setState(166);
			match(T__4);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DefaultCaseContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public DefaultCaseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_defaultCase; }
	}

	public final DefaultCaseContext defaultCase() throws RecognitionException {
		DefaultCaseContext _localctx = new DefaultCaseContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_defaultCase);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
			match(T__15);
			setState(169);
			match(T__16);
			setState(170);
			statement();
			setState(171);
			match(T__17);
			setState(172);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SwitchCaseContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public SwitchCaseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_switchCase; }
	}

	public final SwitchCaseContext switchCase() throws RecognitionException {
		SwitchCaseContext _localctx = new SwitchCaseContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_switchCase);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(174);
			match(T__18);
			setState(175);
			expression(0);
			setState(176);
			match(T__16);
			setState(177);
			statement();
			setState(178);
			match(T__17);
			setState(179);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfBlockContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ElseifBlockContext elseifBlock() {
			return getRuleContext(ElseifBlockContext.class,0);
		}
		public IfBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifBlock; }
	}

	public final IfBlockContext ifBlock() throws RecognitionException {
		IfBlockContext _localctx = new IfBlockContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_ifBlock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(181);
			match(T__19);
			setState(182);
			expression(0);
			setState(183);
			block();
			setState(186);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__20) {
				{
				setState(184);
				match(T__20);
				setState(185);
				elseifBlock();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ElseifBlockContext extends ParserRuleContext {
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public IfBlockContext ifBlock() {
			return getRuleContext(IfBlockContext.class,0);
		}
		public ElseifBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elseifBlock; }
	}

	public final ElseifBlockContext elseifBlock() throws RecognitionException {
		ElseifBlockContext _localctx = new ElseifBlockContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_elseifBlock);
		try {
			setState(190);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
				enterOuterAlt(_localctx, 1);
				{
				setState(188);
				block();
				}
				break;
			case T__19:
				enterOuterAlt(_localctx, 2);
				{
				setState(189);
				ifBlock();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileBlockContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(cubescriptParser.WHILE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ElseifBlockContext elseifBlock() {
			return getRuleContext(ElseifBlockContext.class,0);
		}
		public WhileBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileBlock; }
	}

	public final WhileBlockContext whileBlock() throws RecognitionException {
		WhileBlockContext _localctx = new WhileBlockContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_whileBlock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(192);
			match(WHILE);
			setState(193);
			expression(0);
			setState(194);
			block();
			setState(197);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__20) {
				{
				setState(195);
				match(T__20);
				setState(196);
				elseifBlock();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctiondefinitionContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(cubescriptParser.IDENTIFIER, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public List<ParamContext> param() {
			return getRuleContexts(ParamContext.class);
		}
		public ParamContext param(int i) {
			return getRuleContext(ParamContext.class,i);
		}
		public FunctiondefinitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functiondefinition; }
	}

	public final FunctiondefinitionContext functiondefinition() throws RecognitionException {
		FunctiondefinitionContext _localctx = new FunctiondefinitionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_functiondefinition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(199);
			match(T__21);
			setState(200);
			match(IDENTIFIER);
			setState(201);
			match(T__6);
			setState(210);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==TYPE) {
				{
				setState(202);
				param();
				setState(207);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__12) {
					{
					{
					setState(203);
					match(T__12);
					setState(204);
					param();
					}
					}
					setState(209);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(212);
			match(T__8);
			setState(213);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamContext extends ParserRuleContext {
		public TerminalNode TYPE() { return getToken(cubescriptParser.TYPE, 0); }
		public TerminalNode IDENTIFIER() { return getToken(cubescriptParser.IDENTIFIER, 0); }
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(215);
			match(TYPE);
			setState(216);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(cubescriptParser.IDENTIFIER, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(218);
			match(IDENTIFIER);
			setState(219);
			match(T__10);
			setState(220);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallContext extends ParserRuleContext {
		public FunctionCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCall; }
	 
		public FunctionCallContext() { }
		public void copyFrom(FunctionCallContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FunctioncallexprsContext extends FunctionCallContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(cubescriptParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(cubescriptParser.IDENTIFIER, i);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public FunctioncallexprsContext(FunctionCallContext ctx) { copyFrom(ctx); }
	}

	public final FunctionCallContext functionCall() throws RecognitionException {
		FunctionCallContext _localctx = new FunctionCallContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_functionCall);
		int _la;
		try {
			setState(250);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				_localctx = new FunctioncallexprsContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(222);
				match(IDENTIFIER);
				setState(223);
				match(T__6);
				setState(232);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 210543282604736640L) != 0)) {
					{
					setState(224);
					expression(0);
					setState(229);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__12) {
						{
						{
						setState(225);
						match(T__12);
						setState(226);
						expression(0);
						}
						}
						setState(231);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(234);
				match(T__8);
				}
				break;
			case 2:
				_localctx = new FunctioncallexprsContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(235);
				match(IDENTIFIER);
				setState(236);
				match(T__1);
				setState(237);
				match(IDENTIFIER);
				setState(238);
				match(T__6);
				setState(247);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 210543282604736640L) != 0)) {
					{
					setState(239);
					expression(0);
					setState(244);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__12) {
						{
						{
						setState(240);
						match(T__12);
						setState(241);
						expression(0);
						}
						}
						setState(246);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(249);
				match(T__8);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public List<LineContext> line() {
			return getRuleContexts(LineContext.class);
		}
		public LineContext line(int i) {
			return getRuleContext(LineContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(252);
			match(T__3);
			setState(256);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 215539463421429832L) != 0)) {
				{
				{
				setState(253);
				line();
				}
				}
				setState(258);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(259);
			match(T__4);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	 
		public ExpressionContext() { }
		public void copyFrom(ExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class TernaryexprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TernaryexprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ConstantexprContext extends ExpressionContext {
		public ConstantContext constant() {
			return getRuleContext(ConstantContext.class,0);
		}
		public ConstantexprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FunctioncallexprContext extends ExpressionContext {
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public FunctioncallexprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParenthesisexprContext extends ExpressionContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ParenthesisexprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DecrementexprContext extends ExpressionContext {
		public TerminalNode IDENTIFIER() { return getToken(cubescriptParser.IDENTIFIER, 0); }
		public ConstantContext constant() {
			return getRuleContext(ConstantContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public DecrementexprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IncrementexprContext extends ExpressionContext {
		public TerminalNode IDENTIFIER() { return getToken(cubescriptParser.IDENTIFIER, 0); }
		public ConstantContext constant() {
			return getRuleContext(ConstantContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public IncrementexprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NegationexprContext extends ExpressionContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public NegationexprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IdentifiereexprContext extends ExpressionContext {
		public TerminalNode IDENTIFIER() { return getToken(cubescriptParser.IDENTIFIER, 0); }
		public IdentifiereexprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DotexprContext extends ExpressionContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(cubescriptParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(cubescriptParser.IDENTIFIER, i);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public DotexprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ArrayassignmentContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public ArrayassignmentContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DotfunctioncallexprsContext extends ExpressionContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(cubescriptParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(cubescriptParser.IDENTIFIER, i);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public DotfunctioncallexprsContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ArrayexprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ArrayexprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class BinaryexprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public MultOpContext multOp() {
			return getRuleContext(MultOpContext.class,0);
		}
		public AddOpContext addOp() {
			return getRuleContext(AddOpContext.class,0);
		}
		public CmpOpContext cmpOp() {
			return getRuleContext(CmpOpContext.class,0);
		}
		public BoolOpContext boolOp() {
			return getRuleContext(BoolOpContext.class,0);
		}
		public BinaryexprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 28;
		enterRecursionRule(_localctx, 28, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(301);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
			case 1:
				{
				_localctx = new ConstantexprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(262);
				constant();
				}
				break;
			case 2:
				{
				_localctx = new FunctioncallexprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(263);
				functionCall();
				}
				break;
			case 3:
				{
				_localctx = new ParenthesisexprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(264);
				match(T__6);
				setState(265);
				expression(0);
				setState(266);
				match(T__8);
				}
				break;
			case 4:
				{
				_localctx = new IdentifiereexprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(268);
				match(IDENTIFIER);
				}
				break;
			case 5:
				{
				_localctx = new NegationexprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(269);
				match(T__22);
				setState(270);
				expression(19);
				}
				break;
			case 6:
				{
				_localctx = new NegationexprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(271);
				match(T__23);
				setState(272);
				expression(18);
				}
				break;
			case 7:
				{
				_localctx = new IncrementexprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(273);
				match(IDENTIFIER);
				setState(274);
				match(T__25);
				}
				break;
			case 8:
				{
				_localctx = new DecrementexprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(275);
				match(IDENTIFIER);
				setState(276);
				match(T__26);
				}
				break;
			case 9:
				{
				_localctx = new IncrementexprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(277);
				constant();
				setState(278);
				match(T__25);
				}
				break;
			case 10:
				{
				_localctx = new DecrementexprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(280);
				constant();
				setState(281);
				match(T__26);
				}
				break;
			case 11:
				{
				_localctx = new DotexprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(283);
				match(IDENTIFIER);
				setState(284);
				match(T__1);
				setState(285);
				match(IDENTIFIER);
				}
				break;
			case 12:
				{
				_localctx = new DotfunctioncallexprsContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(286);
				match(IDENTIFIER);
				setState(287);
				match(T__1);
				setState(288);
				match(IDENTIFIER);
				setState(289);
				match(T__6);
				setState(298);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 210543282604736640L) != 0)) {
					{
					setState(290);
					expression(0);
					setState(295);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__12) {
						{
						{
						setState(291);
						match(T__12);
						setState(292);
						expression(0);
						}
						}
						setState(297);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(300);
				match(T__8);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(396);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,38,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(394);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,37,_ctx) ) {
					case 1:
						{
						_localctx = new BinaryexprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(303);
						if (!(precpred(_ctx, 23))) throw new FailedPredicateException(this, "precpred(_ctx, 23)");
						setState(304);
						multOp();
						setState(305);
						expression(24);
						}
						break;
					case 2:
						{
						_localctx = new BinaryexprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(307);
						if (!(precpred(_ctx, 22))) throw new FailedPredicateException(this, "precpred(_ctx, 22)");
						setState(308);
						addOp();
						setState(309);
						expression(23);
						}
						break;
					case 3:
						{
						_localctx = new BinaryexprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(311);
						if (!(precpred(_ctx, 21))) throw new FailedPredicateException(this, "precpred(_ctx, 21)");
						setState(312);
						cmpOp();
						setState(313);
						expression(22);
						}
						break;
					case 4:
						{
						_localctx = new BinaryexprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(315);
						if (!(precpred(_ctx, 20))) throw new FailedPredicateException(this, "precpred(_ctx, 20)");
						setState(316);
						boolOp();
						setState(317);
						expression(21);
						}
						break;
					case 5:
						{
						_localctx = new TernaryexprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(319);
						if (!(precpred(_ctx, 17))) throw new FailedPredicateException(this, "precpred(_ctx, 17)");
						setState(320);
						match(T__24);
						setState(321);
						expression(0);
						setState(322);
						match(T__16);
						setState(323);
						expression(18);
						}
						break;
					case 6:
						{
						_localctx = new ArrayassignmentContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(325);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(326);
						match(T__11);
						setState(328);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 210543282604736640L) != 0)) {
							{
							setState(327);
							expression(0);
							}
						}

						setState(330);
						match(T__13);
						setState(331);
						match(T__10);
						setState(332);
						expression(7);
						}
						break;
					case 7:
						{
						_localctx = new ArrayassignmentContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(333);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(334);
						match(T__3);
						setState(336);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 210543282604736640L) != 0)) {
							{
							setState(335);
							expression(0);
							}
						}

						setState(338);
						match(T__4);
						setState(339);
						match(T__10);
						setState(340);
						expression(5);
						}
						break;
					case 8:
						{
						_localctx = new DotexprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(341);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(342);
						match(T__1);
						setState(343);
						match(IDENTIFIER);
						}
						break;
					case 9:
						{
						_localctx = new DotfunctioncallexprsContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(344);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(345);
						match(T__1);
						setState(346);
						match(IDENTIFIER);
						setState(347);
						match(T__6);
						setState(356);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 210543282604736640L) != 0)) {
							{
							setState(348);
							expression(0);
							setState(353);
							_errHandler.sync(this);
							_la = _input.LA(1);
							while (_la==T__12) {
								{
								{
								setState(349);
								match(T__12);
								setState(350);
								expression(0);
								}
								}
								setState(355);
								_errHandler.sync(this);
								_la = _input.LA(1);
							}
							}
						}

						setState(358);
						match(T__8);
						}
						break;
					case 10:
						{
						_localctx = new ArrayexprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(359);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(360);
						match(T__11);
						setState(362);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 210543282604736640L) != 0)) {
							{
							setState(361);
							expression(0);
							}
						}

						setState(364);
						match(T__13);
						}
						break;
					case 11:
						{
						_localctx = new ArrayexprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(365);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(366);
						match(T__3);
						setState(368);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 210543282604736640L) != 0)) {
							{
							setState(367);
							expression(0);
							}
						}

						setState(370);
						match(T__4);
						}
						break;
					case 12:
						{
						_localctx = new IncrementexprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(371);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(372);
						match(T__25);
						}
						break;
					case 13:
						{
						_localctx = new DecrementexprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(373);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(374);
						match(T__26);
						}
						break;
					case 14:
						{
						_localctx = new ArrayassignmentContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(375);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(376);
						match(T__11);
						setState(378);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 210543282604736640L) != 0)) {
							{
							setState(377);
							expression(0);
							}
						}

						setState(380);
						match(T__13);
						setState(381);
						match(T__10);
						setState(382);
						functionCall();
						}
						break;
					case 15:
						{
						_localctx = new ArrayassignmentContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(383);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(384);
						match(T__3);
						setState(388);
						_errHandler.sync(this);
						_alt = getInterpreter().adaptivePredict(_input,36,_ctx);
						while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
							if ( _alt==1+1 ) {
								{
								{
								setState(385);
								expression(0);
								}
								} 
							}
							setState(390);
							_errHandler.sync(this);
							_alt = getInterpreter().adaptivePredict(_input,36,_ctx);
						}
						setState(391);
						match(T__4);
						setState(392);
						match(T__10);
						setState(393);
						functionCall();
						}
						break;
					}
					} 
				}
				setState(398);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,38,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MultOpContext extends ParserRuleContext {
		public MultOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multOp; }
	}

	public final MultOpContext multOp() throws RecognitionException {
		MultOpContext _localctx = new MultOpContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_multOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(399);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 2198754822144L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AddOpContext extends ParserRuleContext {
		public AddOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_addOp; }
	}

	public final AddOpContext addOp() throws RecognitionException {
		AddOpContext _localctx = new AddOpContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_addOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(401);
			_la = _input.LA(1);
			if ( !(_la==T__22 || _la==T__40) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CmpOpContext extends ParserRuleContext {
		public CmpOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cmpOp; }
	}

	public final CmpOpContext cmpOp() throws RecognitionException {
		CmpOpContext _localctx = new CmpOpContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_cmpOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(403);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 65970697667840L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoolOpContext extends ParserRuleContext {
		public TerminalNode BOOL_OPERATOR() { return getToken(cubescriptParser.BOOL_OPERATOR, 0); }
		public BoolOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boolOp; }
	}

	public final BoolOpContext boolOp() throws RecognitionException {
		BoolOpContext _localctx = new BoolOpContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_boolOp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(405);
			match(BOOL_OPERATOR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstantContext extends ParserRuleContext {
		public TerminalNode INTEGER() { return getToken(cubescriptParser.INTEGER, 0); }
		public TerminalNode FLOAT() { return getToken(cubescriptParser.FLOAT, 0); }
		public TerminalNode STRING() { return getToken(cubescriptParser.STRING, 0); }
		public TerminalNode BOOL() { return getToken(cubescriptParser.BOOL, 0); }
		public TerminalNode IDENTIFIER() { return getToken(cubescriptParser.IDENTIFIER, 0); }
		public TerminalNode TYPE() { return getToken(cubescriptParser.TYPE, 0); }
		public ConstantContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constant; }
	}

	public final ConstantContext constant() throws RecognitionException {
		ConstantContext _localctx = new ConstantContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_constant);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(407);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 210543282579570688L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 14:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 23);
		case 1:
			return precpred(_ctx, 22);
		case 2:
			return precpred(_ctx, 21);
		case 3:
			return precpred(_ctx, 20);
		case 4:
			return precpred(_ctx, 17);
		case 5:
			return precpred(_ctx, 6);
		case 6:
			return precpred(_ctx, 4);
		case 7:
			return precpred(_ctx, 16);
		case 8:
			return precpred(_ctx, 15);
		case 9:
			return precpred(_ctx, 14);
		case 10:
			return precpred(_ctx, 13);
		case 11:
			return precpred(_ctx, 12);
		case 12:
			return precpred(_ctx, 11);
		case 13:
			return precpred(_ctx, 5);
		case 14:
			return precpred(_ctx, 3);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u00019\u019a\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0001\u0000\u0005\u0000*\b\u0000\n\u0000\f\u0000"+
		"-\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u00017\b\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0005\u0002F\b\u0002\n\u0002\f\u0002I\t\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002"+
		"p\b\u0002\u0001\u0002\u0001\u0002\u0003\u0002t\b\u0002\u0001\u0002\u0003"+
		"\u0002w\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0003\u0002~\b\u0002\u0001\u0002\u0003\u0002\u0081\b\u0002\u0001"+
		"\u0002\u0003\u0002\u0084\b\u0002\u0001\u0002\u0003\u0002\u0087\b\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0005\u0002"+
		"\u008e\b\u0002\n\u0002\f\u0002\u0091\t\u0002\u0003\u0002\u0093\b\u0002"+
		"\u0001\u0002\u0001\u0002\u0003\u0002\u0097\b\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0005\u0003\u009f\b\u0003"+
		"\n\u0003\f\u0003\u00a2\t\u0003\u0001\u0003\u0003\u0003\u00a5\b\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0003\u0006\u00bb\b\u0006\u0001\u0007\u0001\u0007\u0003"+
		"\u0007\u00bf\b\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\b\u00c6"+
		"\b\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0005\t\u00ce\b\t"+
		"\n\t\f\t\u00d1\t\t\u0003\t\u00d3\b\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001"+
		"\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0005\f\u00e4\b\f\n\f\f\f\u00e7\t\f\u0003\f"+
		"\u00e9\b\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\f\u0005\f\u00f3\b\f\n\f\f\f\u00f6\t\f\u0003\f\u00f8\b\f\u0001\f\u0003"+
		"\f\u00fb\b\f\u0001\r\u0001\r\u0005\r\u00ff\b\r\n\r\f\r\u0102\t\r\u0001"+
		"\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0005\u000e\u0126\b\u000e\n\u000e"+
		"\f\u000e\u0129\t\u000e\u0003\u000e\u012b\b\u000e\u0001\u000e\u0003\u000e"+
		"\u012e\b\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0003\u000e\u0149\b\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u0151\b\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0005\u000e\u0160\b\u000e\n\u000e\f\u000e\u0163\t\u000e\u0003"+
		"\u000e\u0165\b\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0003"+
		"\u000e\u016b\b\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0003"+
		"\u000e\u0171\b\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u017b\b\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0005"+
		"\u000e\u0183\b\u000e\n\u000e\f\u000e\u0186\t\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0005\u000e\u018b\b\u000e\n\u000e\f\u000e\u018e\t\u000e\u0001"+
		"\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001"+
		"\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0184\u0001"+
		"\u001c\u0014\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016"+
		"\u0018\u001a\u001c\u001e \"$&\u0000\u0004\u0002\u0000\u000b\u000b\u001c"+
		"(\u0002\u0000\u0017\u0017))\u0003\u0000\b\b\n\n*-\u0003\u0000235799\u01d0"+
		"\u0000+\u0001\u0000\u0000\u0000\u00026\u0001\u0000\u0000\u0000\u0004\u0096"+
		"\u0001\u0000\u0000\u0000\u0006\u0098\u0001\u0000\u0000\u0000\b\u00a8\u0001"+
		"\u0000\u0000\u0000\n\u00ae\u0001\u0000\u0000\u0000\f\u00b5\u0001\u0000"+
		"\u0000\u0000\u000e\u00be\u0001\u0000\u0000\u0000\u0010\u00c0\u0001\u0000"+
		"\u0000\u0000\u0012\u00c7\u0001\u0000\u0000\u0000\u0014\u00d7\u0001\u0000"+
		"\u0000\u0000\u0016\u00da\u0001\u0000\u0000\u0000\u0018\u00fa\u0001\u0000"+
		"\u0000\u0000\u001a\u00fc\u0001\u0000\u0000\u0000\u001c\u012d\u0001\u0000"+
		"\u0000\u0000\u001e\u018f\u0001\u0000\u0000\u0000 \u0191\u0001\u0000\u0000"+
		"\u0000\"\u0193\u0001\u0000\u0000\u0000$\u0195\u0001\u0000\u0000\u0000"+
		"&\u0197\u0001\u0000\u0000\u0000(*\u0003\u0002\u0001\u0000)(\u0001\u0000"+
		"\u0000\u0000*-\u0001\u0000\u0000\u0000+)\u0001\u0000\u0000\u0000+,\u0001"+
		"\u0000\u0000\u0000,.\u0001\u0000\u0000\u0000-+\u0001\u0000\u0000\u0000"+
		"./\u0005\u0000\u0000\u0001/\u0001\u0001\u0000\u0000\u000007\u0003\u0004"+
		"\u0002\u000017\u0003\f\u0006\u000023\u0003\u0010\b\u000034\u0003\u001c"+
		"\u000e\u000047\u0001\u0000\u0000\u000057\u00050\u0000\u000060\u0001\u0000"+
		"\u0000\u000061\u0001\u0000\u0000\u000062\u0001\u0000\u0000\u000065\u0001"+
		"\u0000\u0000\u00007\u0003\u0001\u0000\u0000\u00008\u0097\u0003\u0016\u000b"+
		"\u00009:\u00054\u0000\u0000:;\u00059\u0000\u0000;\u0097\u0005\u0001\u0000"+
		"\u0000<=\u00054\u0000\u0000=>\u00059\u0000\u0000>?\u0005\u0002\u0000\u0000"+
		"?@\u00059\u0000\u0000@\u0097\u0005\u0001\u0000\u0000AB\u0005\u0003\u0000"+
		"\u0000BC\u00059\u0000\u0000CG\u0005\u0004\u0000\u0000DF\u0003\u0002\u0001"+
		"\u0000ED\u0001\u0000\u0000\u0000FI\u0001\u0000\u0000\u0000GE\u0001\u0000"+
		"\u0000\u0000GH\u0001\u0000\u0000\u0000HJ\u0001\u0000\u0000\u0000IG\u0001"+
		"\u0000\u0000\u0000J\u0097\u0005\u0005\u0000\u0000K\u0097\u0003\u0012\t"+
		"\u0000LM\u0005\u0006\u0000\u0000MN\u0005\u0007\u0000\u0000NO\u00059\u0000"+
		"\u0000OP\u0005\b\u0000\u0000PQ\u00059\u0000\u0000QR\u0005\t\u0000\u0000"+
		"R\u0097\u0003\u001a\r\u0000ST\u0005\u0006\u0000\u0000TU\u0005\u0007\u0000"+
		"\u0000UV\u00059\u0000\u0000VW\u0005\n\u0000\u0000WX\u00059\u0000\u0000"+
		"XY\u0005\t\u0000\u0000Y\u0097\u0003\u001a\r\u0000Z[\u00057\u0000\u0000"+
		"[\\\u00059\u0000\u0000\\]\u0005\u000b\u0000\u0000]^\u0003\u0018\f\u0000"+
		"^_\u0005\u0001\u0000\u0000_\u0097\u0001\u0000\u0000\u0000`a\u0003\u0018"+
		"\f\u0000ab\u0005\u0001\u0000\u0000b\u0097\u0001\u0000\u0000\u0000cd\u0005"+
		"9\u0000\u0000de\u0005\u000b\u0000\u0000ef\u0003\u001c\u000e\u0000fg\u0005"+
		"\u0001\u0000\u0000g\u0097\u0001\u0000\u0000\u0000hi\u00057\u0000\u0000"+
		"ij\u00059\u0000\u0000jk\u0005\u000b\u0000\u0000kl\u0003\u001c\u000e\u0000"+
		"lm\u0005\u0001\u0000\u0000m\u0097\u0001\u0000\u0000\u0000np\u00059\u0000"+
		"\u0000on\u0001\u0000\u0000\u0000op\u0001\u0000\u0000\u0000pq\u0001\u0000"+
		"\u0000\u0000qs\u00057\u0000\u0000rt\u00059\u0000\u0000sr\u0001\u0000\u0000"+
		"\u0000st\u0001\u0000\u0000\u0000tv\u0001\u0000\u0000\u0000uw\u0005/\u0000"+
		"\u0000vu\u0001\u0000\u0000\u0000vw\u0001\u0000\u0000\u0000wx\u0001\u0000"+
		"\u0000\u0000xy\u0005\u000b\u0000\u0000yz\u0003\u0018\f\u0000z{\u0005\u0001"+
		"\u0000\u0000{\u0097\u0001\u0000\u0000\u0000|~\u00059\u0000\u0000}|\u0001"+
		"\u0000\u0000\u0000}~\u0001\u0000\u0000\u0000~\u0080\u0001\u0000\u0000"+
		"\u0000\u007f\u0081\u0003&\u0013\u0000\u0080\u007f\u0001\u0000\u0000\u0000"+
		"\u0080\u0081\u0001\u0000\u0000\u0000\u0081\u0083\u0001\u0000\u0000\u0000"+
		"\u0082\u0084\u00059\u0000\u0000\u0083\u0082\u0001\u0000\u0000\u0000\u0083"+
		"\u0084\u0001\u0000\u0000\u0000\u0084\u0086\u0001\u0000\u0000\u0000\u0085"+
		"\u0087\u0005/\u0000\u0000\u0086\u0085\u0001\u0000\u0000\u0000\u0086\u0087"+
		"\u0001\u0000\u0000\u0000\u0087\u0088\u0001\u0000\u0000\u0000\u0088\u0089"+
		"\u0005\u000b\u0000\u0000\u0089\u0092\u0005\f\u0000\u0000\u008a\u008f\u0003"+
		"\u001c\u000e\u0000\u008b\u008c\u0005\r\u0000\u0000\u008c\u008e\u0003\u001c"+
		"\u000e\u0000\u008d\u008b\u0001\u0000\u0000\u0000\u008e\u0091\u0001\u0000"+
		"\u0000\u0000\u008f\u008d\u0001\u0000\u0000\u0000\u008f\u0090\u0001\u0000"+
		"\u0000\u0000\u0090\u0093\u0001\u0000\u0000\u0000\u0091\u008f\u0001\u0000"+
		"\u0000\u0000\u0092\u008a\u0001\u0000\u0000\u0000\u0092\u0093\u0001\u0000"+
		"\u0000\u0000\u0093\u0094\u0001\u0000\u0000\u0000\u0094\u0095\u0005\u000e"+
		"\u0000\u0000\u0095\u0097\u0005\u0001\u0000\u0000\u00968\u0001\u0000\u0000"+
		"\u0000\u00969\u0001\u0000\u0000\u0000\u0096<\u0001\u0000\u0000\u0000\u0096"+
		"A\u0001\u0000\u0000\u0000\u0096K\u0001\u0000\u0000\u0000\u0096L\u0001"+
		"\u0000\u0000\u0000\u0096S\u0001\u0000\u0000\u0000\u0096Z\u0001\u0000\u0000"+
		"\u0000\u0096`\u0001\u0000\u0000\u0000\u0096c\u0001\u0000\u0000\u0000\u0096"+
		"h\u0001\u0000\u0000\u0000\u0096o\u0001\u0000\u0000\u0000\u0096}\u0001"+
		"\u0000\u0000\u0000\u0097\u0005\u0001\u0000\u0000\u0000\u0098\u0099\u0005"+
		"\u000f\u0000\u0000\u0099\u009a\u0005\u0007\u0000\u0000\u009a\u009b\u0003"+
		"\u001c\u000e\u0000\u009b\u009c\u0005\t\u0000\u0000\u009c\u00a0\u0005\u0004"+
		"\u0000\u0000\u009d\u009f\u0003\n\u0005\u0000\u009e\u009d\u0001\u0000\u0000"+
		"\u0000\u009f\u00a2\u0001\u0000\u0000\u0000\u00a0\u009e\u0001\u0000\u0000"+
		"\u0000\u00a0\u00a1\u0001\u0000\u0000\u0000\u00a1\u00a4\u0001\u0000\u0000"+
		"\u0000\u00a2\u00a0\u0001\u0000\u0000\u0000\u00a3\u00a5\u0003\b\u0004\u0000"+
		"\u00a4\u00a3\u0001\u0000\u0000\u0000\u00a4\u00a5\u0001\u0000\u0000\u0000"+
		"\u00a5\u00a6\u0001\u0000\u0000\u0000\u00a6\u00a7\u0005\u0005\u0000\u0000"+
		"\u00a7\u0007\u0001\u0000\u0000\u0000\u00a8\u00a9\u0005\u0010\u0000\u0000"+
		"\u00a9\u00aa\u0005\u0011\u0000\u0000\u00aa\u00ab\u0003\u0004\u0002\u0000"+
		"\u00ab\u00ac\u0005\u0012\u0000\u0000\u00ac\u00ad\u0005\u0001\u0000\u0000"+
		"\u00ad\t\u0001\u0000\u0000\u0000\u00ae\u00af\u0005\u0013\u0000\u0000\u00af"+
		"\u00b0\u0003\u001c\u000e\u0000\u00b0\u00b1\u0005\u0011\u0000\u0000\u00b1"+
		"\u00b2\u0003\u0004\u0002\u0000\u00b2\u00b3\u0005\u0012\u0000\u0000\u00b3"+
		"\u00b4\u0005\u0001\u0000\u0000\u00b4\u000b\u0001\u0000\u0000\u0000\u00b5"+
		"\u00b6\u0005\u0014\u0000\u0000\u00b6\u00b7\u0003\u001c\u000e\u0000\u00b7"+
		"\u00ba\u0003\u001a\r\u0000\u00b8\u00b9\u0005\u0015\u0000\u0000\u00b9\u00bb"+
		"\u0003\u000e\u0007\u0000\u00ba\u00b8\u0001\u0000\u0000\u0000\u00ba\u00bb"+
		"\u0001\u0000\u0000\u0000\u00bb\r\u0001\u0000\u0000\u0000\u00bc\u00bf\u0003"+
		"\u001a\r\u0000\u00bd\u00bf\u0003\f\u0006\u0000\u00be\u00bc\u0001\u0000"+
		"\u0000\u0000\u00be\u00bd\u0001\u0000\u0000\u0000\u00bf\u000f\u0001\u0000"+
		"\u0000\u0000\u00c0\u00c1\u0005.\u0000\u0000\u00c1\u00c2\u0003\u001c\u000e"+
		"\u0000\u00c2\u00c5\u0003\u001a\r\u0000\u00c3\u00c4\u0005\u0015\u0000\u0000"+
		"\u00c4\u00c6\u0003\u000e\u0007\u0000\u00c5\u00c3\u0001\u0000\u0000\u0000"+
		"\u00c5\u00c6\u0001\u0000\u0000\u0000\u00c6\u0011\u0001\u0000\u0000\u0000"+
		"\u00c7\u00c8\u0005\u0016\u0000\u0000\u00c8\u00c9\u00059\u0000\u0000\u00c9"+
		"\u00d2\u0005\u0007\u0000\u0000\u00ca\u00cf\u0003\u0014\n\u0000\u00cb\u00cc"+
		"\u0005\r\u0000\u0000\u00cc\u00ce\u0003\u0014\n\u0000\u00cd\u00cb\u0001"+
		"\u0000\u0000\u0000\u00ce\u00d1\u0001\u0000\u0000\u0000\u00cf\u00cd\u0001"+
		"\u0000\u0000\u0000\u00cf\u00d0\u0001\u0000\u0000\u0000\u00d0\u00d3\u0001"+
		"\u0000\u0000\u0000\u00d1\u00cf\u0001\u0000\u0000\u0000\u00d2\u00ca\u0001"+
		"\u0000\u0000\u0000\u00d2\u00d3\u0001\u0000\u0000\u0000\u00d3\u00d4\u0001"+
		"\u0000\u0000\u0000\u00d4\u00d5\u0005\t\u0000\u0000\u00d5\u00d6\u0003\u001a"+
		"\r\u0000\u00d6\u0013\u0001\u0000\u0000\u0000\u00d7\u00d8\u00057\u0000"+
		"\u0000\u00d8\u00d9\u00059\u0000\u0000\u00d9\u0015\u0001\u0000\u0000\u0000"+
		"\u00da\u00db\u00059\u0000\u0000\u00db\u00dc\u0005\u000b\u0000\u0000\u00dc"+
		"\u00dd\u0003\u001c\u000e\u0000\u00dd\u0017\u0001\u0000\u0000\u0000\u00de"+
		"\u00df\u00059\u0000\u0000\u00df\u00e8\u0005\u0007\u0000\u0000\u00e0\u00e5"+
		"\u0003\u001c\u000e\u0000\u00e1\u00e2\u0005\r\u0000\u0000\u00e2\u00e4\u0003"+
		"\u001c\u000e\u0000\u00e3\u00e1\u0001\u0000\u0000\u0000\u00e4\u00e7\u0001"+
		"\u0000\u0000\u0000\u00e5\u00e3\u0001\u0000\u0000\u0000\u00e5\u00e6\u0001"+
		"\u0000\u0000\u0000\u00e6\u00e9\u0001\u0000\u0000\u0000\u00e7\u00e5\u0001"+
		"\u0000\u0000\u0000\u00e8\u00e0\u0001\u0000\u0000\u0000\u00e8\u00e9\u0001"+
		"\u0000\u0000\u0000\u00e9\u00ea\u0001\u0000\u0000\u0000\u00ea\u00fb\u0005"+
		"\t\u0000\u0000\u00eb\u00ec\u00059\u0000\u0000\u00ec\u00ed\u0005\u0002"+
		"\u0000\u0000\u00ed\u00ee\u00059\u0000\u0000\u00ee\u00f7\u0005\u0007\u0000"+
		"\u0000\u00ef\u00f4\u0003\u001c\u000e\u0000\u00f0\u00f1\u0005\r\u0000\u0000"+
		"\u00f1\u00f3\u0003\u001c\u000e\u0000\u00f2\u00f0\u0001\u0000\u0000\u0000"+
		"\u00f3\u00f6\u0001\u0000\u0000\u0000\u00f4\u00f2\u0001\u0000\u0000\u0000"+
		"\u00f4\u00f5\u0001\u0000\u0000\u0000\u00f5\u00f8\u0001\u0000\u0000\u0000"+
		"\u00f6\u00f4\u0001\u0000\u0000\u0000\u00f7\u00ef\u0001\u0000\u0000\u0000"+
		"\u00f7\u00f8\u0001\u0000\u0000\u0000\u00f8\u00f9\u0001\u0000\u0000\u0000"+
		"\u00f9\u00fb\u0005\t\u0000\u0000\u00fa\u00de\u0001\u0000\u0000\u0000\u00fa"+
		"\u00eb\u0001\u0000\u0000\u0000\u00fb\u0019\u0001\u0000\u0000\u0000\u00fc"+
		"\u0100\u0005\u0004\u0000\u0000\u00fd\u00ff\u0003\u0002\u0001\u0000\u00fe"+
		"\u00fd\u0001\u0000\u0000\u0000\u00ff\u0102\u0001\u0000\u0000\u0000\u0100"+
		"\u00fe\u0001\u0000\u0000\u0000\u0100\u0101\u0001\u0000\u0000\u0000\u0101"+
		"\u0103\u0001\u0000\u0000\u0000\u0102\u0100\u0001\u0000\u0000\u0000\u0103"+
		"\u0104\u0005\u0005\u0000\u0000\u0104\u001b\u0001\u0000\u0000\u0000\u0105"+
		"\u0106\u0006\u000e\uffff\uffff\u0000\u0106\u012e\u0003&\u0013\u0000\u0107"+
		"\u012e\u0003\u0018\f\u0000\u0108\u0109\u0005\u0007\u0000\u0000\u0109\u010a"+
		"\u0003\u001c\u000e\u0000\u010a\u010b\u0005\t\u0000\u0000\u010b\u012e\u0001"+
		"\u0000\u0000\u0000\u010c\u012e\u00059\u0000\u0000\u010d\u010e\u0005\u0017"+
		"\u0000\u0000\u010e\u012e\u0003\u001c\u000e\u0013\u010f\u0110\u0005\u0018"+
		"\u0000\u0000\u0110\u012e\u0003\u001c\u000e\u0012\u0111\u0112\u00059\u0000"+
		"\u0000\u0112\u012e\u0005\u001a\u0000\u0000\u0113\u0114\u00059\u0000\u0000"+
		"\u0114\u012e\u0005\u001b\u0000\u0000\u0115\u0116\u0003&\u0013\u0000\u0116"+
		"\u0117\u0005\u001a\u0000\u0000\u0117\u012e\u0001\u0000\u0000\u0000\u0118"+
		"\u0119\u0003&\u0013\u0000\u0119\u011a\u0005\u001b\u0000\u0000\u011a\u012e"+
		"\u0001\u0000\u0000\u0000\u011b\u011c\u00059\u0000\u0000\u011c\u011d\u0005"+
		"\u0002\u0000\u0000\u011d\u012e\u00059\u0000\u0000\u011e\u011f\u00059\u0000"+
		"\u0000\u011f\u0120\u0005\u0002\u0000\u0000\u0120\u0121\u00059\u0000\u0000"+
		"\u0121\u012a\u0005\u0007\u0000\u0000\u0122\u0127\u0003\u001c\u000e\u0000"+
		"\u0123\u0124\u0005\r\u0000\u0000\u0124\u0126\u0003\u001c\u000e\u0000\u0125"+
		"\u0123\u0001\u0000\u0000\u0000\u0126\u0129\u0001\u0000\u0000\u0000\u0127"+
		"\u0125\u0001\u0000\u0000\u0000\u0127\u0128\u0001\u0000\u0000\u0000\u0128"+
		"\u012b\u0001\u0000\u0000\u0000\u0129\u0127\u0001\u0000\u0000\u0000\u012a"+
		"\u0122\u0001\u0000\u0000\u0000\u012a\u012b\u0001\u0000\u0000\u0000\u012b"+
		"\u012c\u0001\u0000\u0000\u0000\u012c\u012e\u0005\t\u0000\u0000\u012d\u0105"+
		"\u0001\u0000\u0000\u0000\u012d\u0107\u0001\u0000\u0000\u0000\u012d\u0108"+
		"\u0001\u0000\u0000\u0000\u012d\u010c\u0001\u0000\u0000\u0000\u012d\u010d"+
		"\u0001\u0000\u0000\u0000\u012d\u010f\u0001\u0000\u0000\u0000\u012d\u0111"+
		"\u0001\u0000\u0000\u0000\u012d\u0113\u0001\u0000\u0000\u0000\u012d\u0115"+
		"\u0001\u0000\u0000\u0000\u012d\u0118\u0001\u0000\u0000\u0000\u012d\u011b"+
		"\u0001\u0000\u0000\u0000\u012d\u011e\u0001\u0000\u0000\u0000\u012e\u018c"+
		"\u0001\u0000\u0000\u0000\u012f\u0130\n\u0017\u0000\u0000\u0130\u0131\u0003"+
		"\u001e\u000f\u0000\u0131\u0132\u0003\u001c\u000e\u0018\u0132\u018b\u0001"+
		"\u0000\u0000\u0000\u0133\u0134\n\u0016\u0000\u0000\u0134\u0135\u0003 "+
		"\u0010\u0000\u0135\u0136\u0003\u001c\u000e\u0017\u0136\u018b\u0001\u0000"+
		"\u0000\u0000\u0137\u0138\n\u0015\u0000\u0000\u0138\u0139\u0003\"\u0011"+
		"\u0000\u0139\u013a\u0003\u001c\u000e\u0016\u013a\u018b\u0001\u0000\u0000"+
		"\u0000\u013b\u013c\n\u0014\u0000\u0000\u013c\u013d\u0003$\u0012\u0000"+
		"\u013d\u013e\u0003\u001c\u000e\u0015\u013e\u018b\u0001\u0000\u0000\u0000"+
		"\u013f\u0140\n\u0011\u0000\u0000\u0140\u0141\u0005\u0019\u0000\u0000\u0141"+
		"\u0142\u0003\u001c\u000e\u0000\u0142\u0143\u0005\u0011\u0000\u0000\u0143"+
		"\u0144\u0003\u001c\u000e\u0012\u0144\u018b\u0001\u0000\u0000\u0000\u0145"+
		"\u0146\n\u0006\u0000\u0000\u0146\u0148\u0005\f\u0000\u0000\u0147\u0149"+
		"\u0003\u001c\u000e\u0000\u0148\u0147\u0001\u0000\u0000\u0000\u0148\u0149"+
		"\u0001\u0000\u0000\u0000\u0149\u014a\u0001\u0000\u0000\u0000\u014a\u014b"+
		"\u0005\u000e\u0000\u0000\u014b\u014c\u0005\u000b\u0000\u0000\u014c\u018b"+
		"\u0003\u001c\u000e\u0007\u014d\u014e\n\u0004\u0000\u0000\u014e\u0150\u0005"+
		"\u0004\u0000\u0000\u014f\u0151\u0003\u001c\u000e\u0000\u0150\u014f\u0001"+
		"\u0000\u0000\u0000\u0150\u0151\u0001\u0000\u0000\u0000\u0151\u0152\u0001"+
		"\u0000\u0000\u0000\u0152\u0153\u0005\u0005\u0000\u0000\u0153\u0154\u0005"+
		"\u000b\u0000\u0000\u0154\u018b\u0003\u001c\u000e\u0005\u0155\u0156\n\u0010"+
		"\u0000\u0000\u0156\u0157\u0005\u0002\u0000\u0000\u0157\u018b\u00059\u0000"+
		"\u0000\u0158\u0159\n\u000f\u0000\u0000\u0159\u015a\u0005\u0002\u0000\u0000"+
		"\u015a\u015b\u00059\u0000\u0000\u015b\u0164\u0005\u0007\u0000\u0000\u015c"+
		"\u0161\u0003\u001c\u000e\u0000\u015d\u015e\u0005\r\u0000\u0000\u015e\u0160"+
		"\u0003\u001c\u000e\u0000\u015f\u015d\u0001\u0000\u0000\u0000\u0160\u0163"+
		"\u0001\u0000\u0000\u0000\u0161\u015f\u0001\u0000\u0000\u0000\u0161\u0162"+
		"\u0001\u0000\u0000\u0000\u0162\u0165\u0001\u0000\u0000\u0000\u0163\u0161"+
		"\u0001\u0000\u0000\u0000\u0164\u015c\u0001\u0000\u0000\u0000\u0164\u0165"+
		"\u0001\u0000\u0000\u0000\u0165\u0166\u0001\u0000\u0000\u0000\u0166\u018b"+
		"\u0005\t\u0000\u0000\u0167\u0168\n\u000e\u0000\u0000\u0168\u016a\u0005"+
		"\f\u0000\u0000\u0169\u016b\u0003\u001c\u000e\u0000\u016a\u0169\u0001\u0000"+
		"\u0000\u0000\u016a\u016b\u0001\u0000\u0000\u0000\u016b\u016c\u0001\u0000"+
		"\u0000\u0000\u016c\u018b\u0005\u000e\u0000\u0000\u016d\u016e\n\r\u0000"+
		"\u0000\u016e\u0170\u0005\u0004\u0000\u0000\u016f\u0171\u0003\u001c\u000e"+
		"\u0000\u0170\u016f\u0001\u0000\u0000\u0000\u0170\u0171\u0001\u0000\u0000"+
		"\u0000\u0171\u0172\u0001\u0000\u0000\u0000\u0172\u018b\u0005\u0005\u0000"+
		"\u0000\u0173\u0174\n\f\u0000\u0000\u0174\u018b\u0005\u001a\u0000\u0000"+
		"\u0175\u0176\n\u000b\u0000\u0000\u0176\u018b\u0005\u001b\u0000\u0000\u0177"+
		"\u0178\n\u0005\u0000\u0000\u0178\u017a\u0005\f\u0000\u0000\u0179\u017b"+
		"\u0003\u001c\u000e\u0000\u017a\u0179\u0001\u0000\u0000\u0000\u017a\u017b"+
		"\u0001\u0000\u0000\u0000\u017b\u017c\u0001\u0000\u0000\u0000\u017c\u017d"+
		"\u0005\u000e\u0000\u0000\u017d\u017e\u0005\u000b\u0000\u0000\u017e\u018b"+
		"\u0003\u0018\f\u0000\u017f\u0180\n\u0003\u0000\u0000\u0180\u0184\u0005"+
		"\u0004\u0000\u0000\u0181\u0183\u0003\u001c\u000e\u0000\u0182\u0181\u0001"+
		"\u0000\u0000\u0000\u0183\u0186\u0001\u0000\u0000\u0000\u0184\u0185\u0001"+
		"\u0000\u0000\u0000\u0184\u0182\u0001\u0000\u0000\u0000\u0185\u0187\u0001"+
		"\u0000\u0000\u0000\u0186\u0184\u0001\u0000\u0000\u0000\u0187\u0188\u0005"+
		"\u0005\u0000\u0000\u0188\u0189\u0005\u000b\u0000\u0000\u0189\u018b\u0003"+
		"\u0018\f\u0000\u018a\u012f\u0001\u0000\u0000\u0000\u018a\u0133\u0001\u0000"+
		"\u0000\u0000\u018a\u0137\u0001\u0000\u0000\u0000\u018a\u013b\u0001\u0000"+
		"\u0000\u0000\u018a\u013f\u0001\u0000\u0000\u0000\u018a\u0145\u0001\u0000"+
		"\u0000\u0000\u018a\u014d\u0001\u0000\u0000\u0000\u018a\u0155\u0001\u0000"+
		"\u0000\u0000\u018a\u0158\u0001\u0000\u0000\u0000\u018a\u0167\u0001\u0000"+
		"\u0000\u0000\u018a\u016d\u0001\u0000\u0000\u0000\u018a\u0173\u0001\u0000"+
		"\u0000\u0000\u018a\u0175\u0001\u0000\u0000\u0000\u018a\u0177\u0001\u0000"+
		"\u0000\u0000\u018a\u017f\u0001\u0000\u0000\u0000\u018b\u018e\u0001\u0000"+
		"\u0000\u0000\u018c\u018a\u0001\u0000\u0000\u0000\u018c\u018d\u0001\u0000"+
		"\u0000\u0000\u018d\u001d\u0001\u0000\u0000\u0000\u018e\u018c\u0001\u0000"+
		"\u0000\u0000\u018f\u0190\u0007\u0000\u0000\u0000\u0190\u001f\u0001\u0000"+
		"\u0000\u0000\u0191\u0192\u0007\u0001\u0000\u0000\u0192!\u0001\u0000\u0000"+
		"\u0000\u0193\u0194\u0007\u0002\u0000\u0000\u0194#\u0001\u0000\u0000\u0000"+
		"\u0195\u0196\u00051\u0000\u0000\u0196%\u0001\u0000\u0000\u0000\u0197\u0198"+
		"\u0007\u0003\u0000\u0000\u0198\'\u0001\u0000\u0000\u0000\'+6Gosv}\u0080"+
		"\u0083\u0086\u008f\u0092\u0096\u00a0\u00a4\u00ba\u00be\u00c5\u00cf\u00d2"+
		"\u00e5\u00e8\u00f4\u00f7\u00fa\u0100\u0127\u012a\u012d\u0148\u0150\u0161"+
		"\u0164\u016a\u0170\u017a\u0184\u018a\u018c";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}