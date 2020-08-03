import sys
from io import StringIO

from antlr4 import *
from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("\u00f0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\13\5\13")
        buf.write("q\n\13\3\13\3\13\5\13u\n\13\3\13\5\13x\n\13\5\13z\n\13")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\r\6\r\u0083\n\r\r\r\16\r")
        buf.write("\u0084\3\16\3\16\3\16\3\16\3\16\5\16\u008c\n\16\3\16\3")
        buf.write("\16\5\16\u0090\n\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\5\23\u009f\n\23\3\23\3")
        buf.write("\23\3\24\3\24\3\24\7\24\u00a6\n\24\f\24\16\24\u00a9\13")
        buf.write("\24\3\24\3\24\3\24\3\24\7\24\u00af\n\24\f\24\16\24\u00b2")
        buf.write("\13\24\3\24\5\24\u00b5\n\24\3\25\3\25\3\25\3\25\3\25\7")
        buf.write("\25\u00bc\n\25\f\25\16\25\u00bf\13\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\7\25\u00c9\n\25\f\25\16\25\u00cc")
        buf.write("\13\25\3\25\3\25\3\25\5\25\u00d1\n\25\3\26\3\26\5\26\u00d5")
        buf.write("\n\26\3\27\3\27\3\30\3\30\3\30\3\30\5\30\u00dd\n\30\3")
        buf.write("\31\3\31\3\32\3\32\3\33\6\33\u00e4\n\33\r\33\16\33\u00e5")
        buf.write("\3\34\3\34\7\34\u00ea\n\34\f\34\16\34\u00ed\13\34\3\35")
        buf.write("\3\35\4\u00bd\u00ca\2\36\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\2)\2+\2-\2/\2\61\2\63\2\65\2\67\29\25\3\2\f\b\2")
        buf.write("HHTTWWhhttww\4\2HHhh\4\2TTtt\6\2\f\f\16\17))^^\6\2\f\f")
        buf.write("\16\17$$^^\3\2^^\3\2c|\3\2C\\\4\2\13\13\"\"\4\2\f\f\16")
        buf.write("\17\2\u00fe\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\29\3\2\2\2\3;\3\2\2\2\5A\3\2\2\2")
        buf.write("\7J\3\2\2\2\tR\3\2\2\2\13^\3\2\2\2\rb\3\2\2\2\17d\3\2")
        buf.write("\2\2\21f\3\2\2\2\23k\3\2\2\2\25y\3\2\2\2\27}\3\2\2\2\31")
        buf.write("\u0082\3\2\2\2\33\u008b\3\2\2\2\35\u0091\3\2\2\2\37\u0093")
        buf.write("\3\2\2\2!\u0095\3\2\2\2#\u0098\3\2\2\2%\u009e\3\2\2\2")
        buf.write("\'\u00b4\3\2\2\2)\u00d0\3\2\2\2+\u00d4\3\2\2\2-\u00d6")
        buf.write("\3\2\2\2/\u00dc\3\2\2\2\61\u00de\3\2\2\2\63\u00e0\3\2")
        buf.write("\2\2\65\u00e3\3\2\2\2\67\u00e7\3\2\2\29\u00ee\3\2\2\2")
        buf.write(";<\7c\2\2<=\7e\2\2=>\7v\2\2>?\7q\2\2?@\7t\2\2@\4\3\2\2")
        buf.write("\2AB\7t\2\2BC\7g\2\2CD\7u\2\2DE\7q\2\2EF\7w\2\2FG\7t\2")
        buf.write("\2GH\7e\2\2HI\7g\2\2I\6\3\2\2\2JK\7u\2\2KL\7v\2\2LM\7")
        buf.write("c\2\2MN\7v\2\2NO\7g\2\2OP\7u\2\2PQ\7<\2\2Q\b\3\2\2\2R")
        buf.write("S\7r\2\2ST\7c\2\2TU\7t\2\2UV\7c\2\2VW\7o\2\2WX\7g\2\2")
        buf.write("XY\7v\2\2YZ\7g\2\2Z[\7t\2\2[\\\7u\2\2\\]\7<\2\2]\n\3\2")
        buf.write("\2\2^_\7k\2\2_`\7p\2\2`a\7<\2\2a\f\3\2\2\2bc\7]\2\2c\16")
        buf.write("\3\2\2\2de\7_\2\2e\20\3\2\2\2fg\7q\2\2gh\7w\2\2hi\7v\2")
        buf.write("\2ij\7<\2\2j\22\3\2\2\2kl\5\33\16\2l\24\3\2\2\2mn\6\13")
        buf.write("\2\2nz\5\65\33\2oq\7\17\2\2po\3\2\2\2pq\3\2\2\2qr\3\2")
        buf.write("\2\2ru\7\f\2\2su\4\16\17\2tp\3\2\2\2ts\3\2\2\2uw\3\2\2")
        buf.write("\2vx\5\65\33\2wv\3\2\2\2wx\3\2\2\2xz\3\2\2\2ym\3\2\2\2")
        buf.write("yt\3\2\2\2z{\3\2\2\2{|\b\13\2\2|\26\3\2\2\2}~\5\31\r\2")
        buf.write("~\30\3\2\2\2\177\u0083\5\61\31\2\u0080\u0083\5\63\32\2")
        buf.write("\u0081\u0083\7a\2\2\u0082\177\3\2\2\2\u0082\u0080\3\2")
        buf.write("\2\2\u0082\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0082")
        buf.write("\3\2\2\2\u0084\u0085\3\2\2\2\u0085\32\3\2\2\2\u0086\u008c")
        buf.write("\t\2\2\2\u0087\u0088\t\3\2\2\u0088\u008c\t\4\2\2\u0089")
        buf.write("\u008a\t\4\2\2\u008a\u008c\t\3\2\2\u008b\u0086\3\2\2\2")
        buf.write("\u008b\u0087\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3")
        buf.write("\2\2\2\u008c\u008f\3\2\2\2\u008d\u0090\5\'\24\2\u008e")
        buf.write("\u0090\5)\25\2\u008f\u008d\3\2\2\2\u008f\u008e\3\2\2\2")
        buf.write("\u0090\34\3\2\2\2\u0091\u0092\7<\2\2\u0092\36\3\2\2\2")
        buf.write("\u0093\u0094\7?\2\2\u0094 \3\2\2\2\u0095\u0096\7/\2\2")
        buf.write("\u0096\u0097\7@\2\2\u0097\"\3\2\2\2\u0098\u0099\7/\2\2")
        buf.write("\u0099\u009a\7/\2\2\u009a\u009b\7@\2\2\u009b$\3\2\2\2")
        buf.write("\u009c\u009f\5\65\33\2\u009d\u009f\5\67\34\2\u009e\u009c")
        buf.write("\3\2\2\2\u009e\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0")
        buf.write("\u00a1\b\23\3\2\u00a1&\3\2\2\2\u00a2\u00a7\7)\2\2\u00a3")
        buf.write("\u00a6\5/\30\2\u00a4\u00a6\n\5\2\2\u00a5\u00a3\3\2\2\2")
        buf.write("\u00a5\u00a4\3\2\2\2\u00a6\u00a9\3\2\2\2\u00a7\u00a5\3")
        buf.write("\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00aa\3\2\2\2\u00a9\u00a7")
        buf.write("\3\2\2\2\u00aa\u00b5\7)\2\2\u00ab\u00b0\7$\2\2\u00ac\u00af")
        buf.write("\5/\30\2\u00ad\u00af\n\6\2\2\u00ae\u00ac\3\2\2\2\u00ae")
        buf.write("\u00ad\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0\u00ae\3\2\2\2")
        buf.write("\u00b0\u00b1\3\2\2\2\u00b1\u00b3\3\2\2\2\u00b2\u00b0\3")
        buf.write("\2\2\2\u00b3\u00b5\7$\2\2\u00b4\u00a2\3\2\2\2\u00b4\u00ab")
        buf.write("\3\2\2\2\u00b5(\3\2\2\2\u00b6\u00b7\7)\2\2\u00b7\u00b8")
        buf.write("\7)\2\2\u00b8\u00b9\7)\2\2\u00b9\u00bd\3\2\2\2\u00ba\u00bc")
        buf.write("\5+\26\2\u00bb\u00ba\3\2\2\2\u00bc\u00bf\3\2\2\2\u00bd")
        buf.write("\u00be\3\2\2\2\u00bd\u00bb\3\2\2\2\u00be\u00c0\3\2\2\2")
        buf.write("\u00bf\u00bd\3\2\2\2\u00c0\u00c1\7)\2\2\u00c1\u00c2\7")
        buf.write(")\2\2\u00c2\u00d1\7)\2\2\u00c3\u00c4\7$\2\2\u00c4\u00c5")
        buf.write("\7$\2\2\u00c5\u00c6\7$\2\2\u00c6\u00ca\3\2\2\2\u00c7\u00c9")
        buf.write("\5+\26\2\u00c8\u00c7\3\2\2\2\u00c9\u00cc\3\2\2\2\u00ca")
        buf.write("\u00cb\3\2\2\2\u00ca\u00c8\3\2\2\2\u00cb\u00cd\3\2\2\2")
        buf.write("\u00cc\u00ca\3\2\2\2\u00cd\u00ce\7$\2\2\u00ce\u00cf\7")
        buf.write("$\2\2\u00cf\u00d1\7$\2\2\u00d0\u00b6\3\2\2\2\u00d0\u00c3")
        buf.write("\3\2\2\2\u00d1*\3\2\2\2\u00d2\u00d5\5-\27\2\u00d3\u00d5")
        buf.write("\5/\30\2\u00d4\u00d2\3\2\2\2\u00d4\u00d3\3\2\2\2\u00d5")
        buf.write(",\3\2\2\2\u00d6\u00d7\n\7\2\2\u00d7.\3\2\2\2\u00d8\u00d9")
        buf.write("\7^\2\2\u00d9\u00dd\13\2\2\2\u00da\u00db\7^\2\2\u00db")
        buf.write("\u00dd\5\25\13\2\u00dc\u00d8\3\2\2\2\u00dc\u00da\3\2\2")
        buf.write("\2\u00dd\60\3\2\2\2\u00de\u00df\t\b\2\2\u00df\62\3\2\2")
        buf.write("\2\u00e0\u00e1\t\t\2\2\u00e1\64\3\2\2\2\u00e2\u00e4\t")
        buf.write("\n\2\2\u00e3\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e3")
        buf.write("\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\66\3\2\2\2\u00e7\u00eb")
        buf.write("\7%\2\2\u00e8\u00ea\n\13\2\2\u00e9\u00e8\3\2\2\2\u00ea")
        buf.write("\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2")
        buf.write("\u00ec8\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00ef\13\2\2")
        buf.write("\2\u00ef:\3\2\2\2\30\2ptwy\u0082\u0084\u008b\u008f\u009e")
        buf.write("\u00a5\u00a7\u00ae\u00b0\u00b4\u00bd\u00ca\u00d0\u00d4")
        buf.write("\u00dc\u00e5\u00eb\4\3\13\2\b\2\2")
        return buf.getvalue()


class drymlLexer(Lexer):
    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    STRING = 9
    NEWLINE = 10
    NAME = 11
    WORD = 12
    STRING_LITERAL = 13
    COLON = 14
    ASSIGN = 15
    CONTROL_FLOW_SYNC = 16
    CONTROL_FLOW_ASYNC = 17
    SKIP_ = 18
    ANY = 19

    channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = ["<INVALID>",
                    "'actor'", "'resource'", "'states:'", "'parameters:'", "'in:'",
                    "'['", "']'", "'out:'", "':'", "'='", "'->'", "'-->'"]

    symbolicNames = ["<INVALID>",
                     "STRING", "NEWLINE", "NAME", "WORD", "STRING_LITERAL", "COLON",
                     "ASSIGN", "CONTROL_FLOW_SYNC", "CONTROL_FLOW_ASYNC", "SKIP_",
                     "ANY"]

    ruleNames = ["T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6",
                 "T__7", "STRING", "NEWLINE", "NAME", "WORD", "STRING_LITERAL",
                 "COLON", "ASSIGN", "CONTROL_FLOW_SYNC", "CONTROL_FLOW_ASYNC",
                 "SKIP_", "SHORT_STRING", "LONG_STRING", "LONG_STRING_ITEM",
                 "LONG_STRING_CHAR", "STRING_ESCAPE_SEQ", "LOWERCASE",
                 "UPPERCASE", "SPACES", "COMMENT", "ANY"]

    grammarFileName = "dryml.g4"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

    def action(self, localctx: RuleContext, ruleIndex: int, actionIndex: int):
        if self._actions is None:
            actions = dict()
            actions[9] = self.NEWLINE_action
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def NEWLINE_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 0:

            String
            newLine = getText().replaceAll("[^\r\n\f]+", "");
            String
            spaces = getText().replaceAll("[\r\n\f]+", "");
            int
            next = _input.LA(1);
            if (next == '\r' | | next == '\n' | | next == '\f' | | next == '#') {
            // If we're inside a list or on a blank line, ignore all indents,
            // dedents and line breaks.
            skip();
            }
            else {
            emit(commonToken(NEWLINE, newLine));
            int indent = getIndentationCount(spaces);
            int previous = indents.isEmpty() ? 0: indents.peek();
            if
            (indent == previous)
            {
            // skip
            indents
            of
            the
            same
            size as the
            present
            indent - size
            skip();
            }
            else if (indent > previous) {
            indents.push(indent);
            emit(commonToken(Python3Parser.INDENT, spaces));
            }
            else {
            // Possibly emit more than 1 DEDENT token.
            while (!indents.isEmpty() & & indents.peek() > indent) {
            this.emit(createDedent());
            indents.pop();
            }
            }
            }

            def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):

    if self._predicates is None:
        preds = dict()
        preds[9] = self.NEWLINE_sempred
        self._predicates = preds
    pred = self._predicates.get(ruleIndex, None)
    if pred is not None:
        return pred(localctx, predIndex)
    else:
        raise Exception("No registered predicate for:" + str(ruleIndex))


def NEWLINE_sempred(self, localctx: RuleContext, predIndex: int):
    if predIndex == 0:
        return atStartOfInput()
