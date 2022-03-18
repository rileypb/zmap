# Generated from /Users/rileypb/dev/zmap/src/main/python/zmap.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from map import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35")
        buf.write("\u008e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\2\3\3\6\3+\n\3\r\3\16\3,\3\4\3\4\3\4\3\4\3")
        buf.write("\4\6\4\64\n\4\r\4\16\4\65\3\4\5\49\n\4\3\4\5\4<\n\4\3")
        buf.write("\5\3\5\3\5\6\5A\n\5\r\5\16\5B\3\6\3\6\3\6\3\6\5\6I\n\6")
        buf.write("\3\6\5\6L\n\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6T\n\6\3\6\3\6")
        buf.write("\5\6X\n\6\3\7\3\7\7\7\\\n\7\f\7\16\7_\13\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\5\13q\n\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13y\n")
        buf.write("\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21")
        buf.write("\3\21\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\2\2\24\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$\2\6\3\3\6\6")
        buf.write("\3\2\6\6\3\2\34\35\3\2\r\17\2\u008b\2&\3\2\2\2\4*\3\2")
        buf.write("\2\2\6.\3\2\2\2\b@\3\2\2\2\nW\3\2\2\2\fY\3\2\2\2\16b\3")
        buf.write("\2\2\2\20f\3\2\2\2\22h\3\2\2\2\24x\3\2\2\2\26z\3\2\2\2")
        buf.write("\30|\3\2\2\2\32~\3\2\2\2\34\u0080\3\2\2\2\36\u0082\3\2")
        buf.write("\2\2 \u0084\3\2\2\2\"\u0086\3\2\2\2$\u0088\3\2\2\2&\'")
        buf.write("\5\4\3\2\'(\7\2\2\3(\3\3\2\2\2)+\5\6\4\2*)\3\2\2\2+,\3")
        buf.write("\2\2\2,*\3\2\2\2,-\3\2\2\2-\5\3\2\2\2./\5\22\n\2/\60\7")
        buf.write("\t\2\2\60\61\5\b\5\2\61;\7\n\2\2\62\64\7\6\2\2\63\62\3")
        buf.write("\2\2\2\64\65\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\668\3")
        buf.write("\2\2\2\679\7\2\2\38\67\3\2\2\289\3\2\2\29<\3\2\2\2:<\7")
        buf.write("\2\2\3;\63\3\2\2\2;:\3\2\2\2<\7\3\2\2\2=A\5\n\6\2>A\5")
        buf.write("\f\7\2?A\7\6\2\2@=\3\2\2\2@>\3\2\2\2@?\3\2\2\2AB\3\2\2")
        buf.write("\2B@\3\2\2\2BC\3\2\2\2C\t\3\2\2\2DE\5\16\b\2EH\5\24\13")
        buf.write("\2FI\5\16\b\2GI\5\"\22\2HF\3\2\2\2HG\3\2\2\2IK\3\2\2\2")
        buf.write("JL\5\20\t\2KJ\3\2\2\2KL\3\2\2\2LM\3\2\2\2MN\t\2\2\2NX")
        buf.write("\3\2\2\2OP\5\16\b\2PQ\5\24\13\2QS\5$\23\2RT\5\20\t\2S")
        buf.write("R\3\2\2\2ST\3\2\2\2TU\3\2\2\2UV\t\2\2\2VX\3\2\2\2WD\3")
        buf.write("\2\2\2WO\3\2\2\2X\13\3\2\2\2Y]\7\3\2\2Z\\\n\3\2\2[Z\3")
        buf.write("\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^`\3\2\2\2_]\3\2")
        buf.write("\2\2`a\t\2\2\2a\r\3\2\2\2bc\7\20\2\2cd\5\22\n\2de\7\21")
        buf.write("\2\2e\17\3\2\2\2fg\t\4\2\2g\21\3\2\2\2hi\7\b\2\2i\23\3")
        buf.write("\2\2\2jk\5\34\17\2kl\5\26\f\2ly\3\2\2\2mn\5\34\17\2np")
        buf.write("\5\32\16\2oq\5\36\20\2po\3\2\2\2pq\3\2\2\2qy\3\2\2\2r")
        buf.write("s\5\32\16\2st\5\36\20\2ty\3\2\2\2uv\5\30\r\2vw\5\36\20")
        buf.write("\2wy\3\2\2\2xj\3\2\2\2xm\3\2\2\2xr\3\2\2\2xu\3\2\2\2y")
        buf.write("\25\3\2\2\2z{\7\r\2\2{\27\3\2\2\2|}\7\16\2\2}\31\3\2\2")
        buf.write("\2~\177\7\17\2\2\177\33\3\2\2\2\u0080\u0081\7\7\2\2\u0081")
        buf.write("\35\3\2\2\2\u0082\u0083\7\7\2\2\u0083\37\3\2\2\2\u0084")
        buf.write("\u0085\t\5\2\2\u0085!\3\2\2\2\u0086\u0087\7\13\2\2\u0087")
        buf.write("#\3\2\2\2\u0088\u0089\7\f\2\2\u0089\u008a\7\4\2\2\u008a")
        buf.write("\u008b\5\22\n\2\u008b\u008c\7\5\2\2\u008c%\3\2\2\2\17")
        buf.write(",\658;@BHKSW]px")
        return buf.getvalue()


class zmapParser ( Parser ):

    grammarFileName = "zmap.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#'", "'('", "')'", "'\n'", "<INVALID>", 
                     "<INVALID>", "'{'", "'}'", "'?'", "'*'", "'-->'", "'<--'", 
                     "'<->'", "'['", "']'", "'n'", "'ne'", "'e'", "'se'", 
                     "'s'", "'sw'", "'w'", "'nw'", "'u'", "'d'", "'<'", 
                     "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "LPAREN", "RPAREN", "NL", 
                      "DIRECTION", "NAME", "LBRACE", "RBRACE", "QUESTION", 
                      "STAR", "LARROW", "RARROW", "BARROW", "LBRACK", "RBRACK", 
                      "N", "NE", "E", "SE", "S", "SW", "W", "NW", "U", "D", 
                      "CLOSE", "FAR" ]

    RULE_parse = 0
    RULE_ifmaps = 1
    RULE_ifmapblock = 2
    RULE_ifmap = 3
    RULE_passage = 4
    RULE_comment = 5
    RULE_room = 6
    RULE_modifier = 7
    RULE_name = 8
    RULE_directed_arrow = 9
    RULE_larrow = 10
    RULE_rarrow = 11
    RULE_barrow = 12
    RULE_left_direction = 13
    RULE_right_direction = 14
    RULE_arrow = 15
    RULE_unknown = 16
    RULE_special = 17

    ruleNames =  [ "parse", "ifmaps", "ifmapblock", "ifmap", "passage", 
                   "comment", "room", "modifier", "name", "directed_arrow", 
                   "larrow", "rarrow", "barrow", "left_direction", "right_direction", 
                   "arrow", "unknown", "special" ]

    EOF = Token.EOF
    T__0=1
    LPAREN=2
    RPAREN=3
    NL=4
    DIRECTION=5
    NAME=6
    LBRACE=7
    RBRACE=8
    QUESTION=9
    STAR=10
    LARROW=11
    RARROW=12
    BARROW=13
    LBRACK=14
    RBRACK=15
    N=16
    NE=17
    E=18
    SE=19
    S=20
    SW=21
    W=22
    NW=23
    U=24
    D=25
    CLOSE=26
    FAR=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifmaps(self):
            return self.getTypedRuleContext(zmapParser.IfmapsContext,0)


        def EOF(self):
            return self.getToken(zmapParser.EOF, 0)

        def getRuleIndex(self):
            return zmapParser.RULE_parse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParse" ):
                listener.enterParse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParse" ):
                listener.exitParse(self)




    def parse(self):

        localctx = zmapParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.ifmaps()
            self.state = 37
            self.match(zmapParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfmapsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifmapblock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zmapParser.IfmapblockContext)
            else:
                return self.getTypedRuleContext(zmapParser.IfmapblockContext,i)


        def getRuleIndex(self):
            return zmapParser.RULE_ifmaps

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfmaps" ):
                listener.enterIfmaps(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfmaps" ):
                listener.exitIfmaps(self)




    def ifmaps(self):

        localctx = zmapParser.IfmapsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_ifmaps)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 39
                self.ifmapblock()
                self.state = 42 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==zmapParser.NAME):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfmapblockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(zmapParser.NameContext,0)


        def LBRACE(self):
            return self.getToken(zmapParser.LBRACE, 0)

        def ifmap(self):
            return self.getTypedRuleContext(zmapParser.IfmapContext,0)


        def RBRACE(self):
            return self.getToken(zmapParser.RBRACE, 0)

        def EOF(self):
            return self.getToken(zmapParser.EOF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(zmapParser.NL)
            else:
                return self.getToken(zmapParser.NL, i)

        def getRuleIndex(self):
            return zmapParser.RULE_ifmapblock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfmapblock" ):
                listener.enterIfmapblock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfmapblock" ):
                listener.exitIfmapblock(self)




    def ifmapblock(self):

        localctx = zmapParser.IfmapblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ifmapblock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.name()
            self.state = 45
            self.match(zmapParser.LBRACE)
            self.state = 46
            self.ifmap()
            self.state = 47
            self.match(zmapParser.RBRACE)
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [zmapParser.NL]:
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 48
                    self.match(zmapParser.NL)
                    self.state = 51 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==zmapParser.NL):
                        break

                self.state = 54
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 53
                    self.match(zmapParser.EOF)


                pass
            elif token in [zmapParser.EOF]:
                self.state = 56
                self.match(zmapParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfmapContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def passage(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zmapParser.PassageContext)
            else:
                return self.getTypedRuleContext(zmapParser.PassageContext,i)


        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zmapParser.CommentContext)
            else:
                return self.getTypedRuleContext(zmapParser.CommentContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(zmapParser.NL)
            else:
                return self.getToken(zmapParser.NL, i)

        def getRuleIndex(self):
            return zmapParser.RULE_ifmap

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfmap" ):
                listener.enterIfmap(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfmap" ):
                listener.exitIfmap(self)




    def ifmap(self):

        localctx = zmapParser.IfmapContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ifmap)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 62
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [zmapParser.LBRACK]:
                    self.state = 59
                    self.passage()
                    pass
                elif token in [zmapParser.T__0]:
                    self.state = 60
                    self.comment()
                    pass
                elif token in [zmapParser.NL]:
                    self.state = 61
                    self.match(zmapParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << zmapParser.T__0) | (1 << zmapParser.NL) | (1 << zmapParser.LBRACK))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PassageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def room(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zmapParser.RoomContext)
            else:
                return self.getTypedRuleContext(zmapParser.RoomContext,i)


        def directed_arrow(self):
            return self.getTypedRuleContext(zmapParser.Directed_arrowContext,0)


        def NL(self):
            return self.getToken(zmapParser.NL, 0)

        def EOF(self):
            return self.getToken(zmapParser.EOF, 0)

        def unknown(self):
            return self.getTypedRuleContext(zmapParser.UnknownContext,0)


        def modifier(self):
            return self.getTypedRuleContext(zmapParser.ModifierContext,0)


        def special(self):
            return self.getTypedRuleContext(zmapParser.SpecialContext,0)


        def getRuleIndex(self):
            return zmapParser.RULE_passage

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPassage" ):
                listener.enterPassage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPassage" ):
                listener.exitPassage(self)




    def passage(self):

        localctx = zmapParser.PassageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_passage)
        self._la = 0 # Token type
        try:
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.room()
                self.state = 67
                self.directed_arrow()
                self.state = 70
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [zmapParser.LBRACK]:
                    self.state = 68
                    self.room()
                    pass
                elif token in [zmapParser.QUESTION]:
                    self.state = 69
                    self.unknown()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==zmapParser.CLOSE or _la==zmapParser.FAR:
                    self.state = 72
                    self.modifier()


                self.state = 75
                _la = self._input.LA(1)
                if not(_la==zmapParser.EOF or _la==zmapParser.NL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.room()
                self.state = 78
                self.directed_arrow()
                self.state = 79
                self.special()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==zmapParser.CLOSE or _la==zmapParser.FAR:
                    self.state = 80
                    self.modifier()


                self.state = 83
                _la = self._input.LA(1)
                if not(_la==zmapParser.EOF or _la==zmapParser.NL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(zmapParser.NL)
            else:
                return self.getToken(zmapParser.NL, i)

        def EOF(self):
            return self.getToken(zmapParser.EOF, 0)

        def getRuleIndex(self):
            return zmapParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = zmapParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(zmapParser.T__0)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << zmapParser.T__0) | (1 << zmapParser.LPAREN) | (1 << zmapParser.RPAREN) | (1 << zmapParser.DIRECTION) | (1 << zmapParser.NAME) | (1 << zmapParser.LBRACE) | (1 << zmapParser.RBRACE) | (1 << zmapParser.QUESTION) | (1 << zmapParser.STAR) | (1 << zmapParser.LARROW) | (1 << zmapParser.RARROW) | (1 << zmapParser.BARROW) | (1 << zmapParser.LBRACK) | (1 << zmapParser.RBRACK) | (1 << zmapParser.N) | (1 << zmapParser.NE) | (1 << zmapParser.E) | (1 << zmapParser.SE) | (1 << zmapParser.S) | (1 << zmapParser.SW) | (1 << zmapParser.W) | (1 << zmapParser.NW) | (1 << zmapParser.U) | (1 << zmapParser.D) | (1 << zmapParser.CLOSE) | (1 << zmapParser.FAR))) != 0):
                self.state = 88
                _la = self._input.LA(1)
                if _la <= 0 or _la==zmapParser.NL:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
            _la = self._input.LA(1)
            if not(_la==zmapParser.EOF or _la==zmapParser.NL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RoomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(zmapParser.LBRACK, 0)

        def name(self):
            return self.getTypedRuleContext(zmapParser.NameContext,0)


        def RBRACK(self):
            return self.getToken(zmapParser.RBRACK, 0)

        def getRuleIndex(self):
            return zmapParser.RULE_room

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoom" ):
                listener.enterRoom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoom" ):
                listener.exitRoom(self)




    def room(self):

        localctx = zmapParser.RoomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_room)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(zmapParser.LBRACK)
            self.state = 97
            self.name()
            self.state = 98
            self.match(zmapParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLOSE(self):
            return self.getToken(zmapParser.CLOSE, 0)

        def FAR(self):
            return self.getToken(zmapParser.FAR, 0)

        def getRuleIndex(self):
            return zmapParser.RULE_modifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModifier" ):
                listener.enterModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModifier" ):
                listener.exitModifier(self)




    def modifier(self):

        localctx = zmapParser.ModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_modifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            _la = self._input.LA(1)
            if not(_la==zmapParser.CLOSE or _la==zmapParser.FAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(zmapParser.NAME, 0)

        def getRuleIndex(self):
            return zmapParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)




    def name(self):

        localctx = zmapParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(zmapParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Directed_arrowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def left_direction(self):
            return self.getTypedRuleContext(zmapParser.Left_directionContext,0)


        def larrow(self):
            return self.getTypedRuleContext(zmapParser.LarrowContext,0)


        def barrow(self):
            return self.getTypedRuleContext(zmapParser.BarrowContext,0)


        def right_direction(self):
            return self.getTypedRuleContext(zmapParser.Right_directionContext,0)


        def rarrow(self):
            return self.getTypedRuleContext(zmapParser.RarrowContext,0)


        def getRuleIndex(self):
            return zmapParser.RULE_directed_arrow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirected_arrow" ):
                listener.enterDirected_arrow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirected_arrow" ):
                listener.exitDirected_arrow(self)




    def directed_arrow(self):

        localctx = zmapParser.Directed_arrowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_directed_arrow)
        self._la = 0 # Token type
        try:
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.left_direction()
                self.state = 105
                self.larrow()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.left_direction()
                self.state = 108
                self.barrow()
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==zmapParser.DIRECTION:
                    self.state = 109
                    self.right_direction()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 112
                self.barrow()
                self.state = 113
                self.right_direction()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 115
                self.rarrow()
                self.state = 116
                self.right_direction()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LarrowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LARROW(self):
            return self.getToken(zmapParser.LARROW, 0)

        def getRuleIndex(self):
            return zmapParser.RULE_larrow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLarrow" ):
                listener.enterLarrow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLarrow" ):
                listener.exitLarrow(self)




    def larrow(self):

        localctx = zmapParser.LarrowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_larrow)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(zmapParser.LARROW)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RarrowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RARROW(self):
            return self.getToken(zmapParser.RARROW, 0)

        def getRuleIndex(self):
            return zmapParser.RULE_rarrow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRarrow" ):
                listener.enterRarrow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRarrow" ):
                listener.exitRarrow(self)




    def rarrow(self):

        localctx = zmapParser.RarrowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_rarrow)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(zmapParser.RARROW)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BarrowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BARROW(self):
            return self.getToken(zmapParser.BARROW, 0)

        def getRuleIndex(self):
            return zmapParser.RULE_barrow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBarrow" ):
                listener.enterBarrow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBarrow" ):
                listener.exitBarrow(self)




    def barrow(self):

        localctx = zmapParser.BarrowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_barrow)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(zmapParser.BARROW)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Left_directionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIRECTION(self):
            return self.getToken(zmapParser.DIRECTION, 0)

        def getRuleIndex(self):
            return zmapParser.RULE_left_direction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeft_direction" ):
                listener.enterLeft_direction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeft_direction" ):
                listener.exitLeft_direction(self)




    def left_direction(self):

        localctx = zmapParser.Left_directionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_left_direction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(zmapParser.DIRECTION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Right_directionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIRECTION(self):
            return self.getToken(zmapParser.DIRECTION, 0)

        def getRuleIndex(self):
            return zmapParser.RULE_right_direction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRight_direction" ):
                listener.enterRight_direction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRight_direction" ):
                listener.exitRight_direction(self)




    def right_direction(self):

        localctx = zmapParser.Right_directionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_right_direction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(zmapParser.DIRECTION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LARROW(self):
            return self.getToken(zmapParser.LARROW, 0)

        def RARROW(self):
            return self.getToken(zmapParser.RARROW, 0)

        def BARROW(self):
            return self.getToken(zmapParser.BARROW, 0)

        def getRuleIndex(self):
            return zmapParser.RULE_arrow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrow" ):
                listener.enterArrow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrow" ):
                listener.exitArrow(self)




    def arrow(self):

        localctx = zmapParser.ArrowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arrow)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << zmapParser.LARROW) | (1 << zmapParser.RARROW) | (1 << zmapParser.BARROW))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnknownContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUESTION(self):
            return self.getToken(zmapParser.QUESTION, 0)

        def getRuleIndex(self):
            return zmapParser.RULE_unknown

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnknown" ):
                listener.enterUnknown(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnknown" ):
                listener.exitUnknown(self)




    def unknown(self):

        localctx = zmapParser.UnknownContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_unknown)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(zmapParser.QUESTION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(zmapParser.STAR, 0)

        def LPAREN(self):
            return self.getToken(zmapParser.LPAREN, 0)

        def name(self):
            return self.getTypedRuleContext(zmapParser.NameContext,0)


        def RPAREN(self):
            return self.getToken(zmapParser.RPAREN, 0)

        def getRuleIndex(self):
            return zmapParser.RULE_special

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecial" ):
                listener.enterSpecial(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecial" ):
                listener.exitSpecial(self)




    def special(self):

        localctx = zmapParser.SpecialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_special)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(zmapParser.STAR)
            self.state = 135
            self.match(zmapParser.LPAREN)
            self.state = 136
            self.name()
            self.state = 137
            self.match(zmapParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





