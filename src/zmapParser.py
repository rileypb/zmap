# Generated from /Users/rileypb/dev/zmap/src/zmap.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\32")
        buf.write("v\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\6\3)\n\3\r\3\16\3*\3\4\3\4\3\4\3\4\5\4\61\n\4\3\4")
        buf.write("\5\4\64\n\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4<\n\4\3\4\3\4\5")
        buf.write("\4@\n\4\3\5\3\5\7\5D\n\5\f\5\16\5G\13\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t")
        buf.write("Y\n\t\3\t\3\t\3\t\3\t\3\t\3\t\5\ta\n\t\3\n\3\n\3\13\3")
        buf.write("\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\2\2\22\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \2\5\3\3\6\6\3\2\6\6\3\2\13\r\2q\2")
        buf.write("\"\3\2\2\2\4(\3\2\2\2\6?\3\2\2\2\bA\3\2\2\2\nJ\3\2\2\2")
        buf.write("\fN\3\2\2\2\16P\3\2\2\2\20`\3\2\2\2\22b\3\2\2\2\24d\3")
        buf.write("\2\2\2\26f\3\2\2\2\30h\3\2\2\2\32j\3\2\2\2\34l\3\2\2\2")
        buf.write("\36n\3\2\2\2 p\3\2\2\2\"#\5\4\3\2#$\7\2\2\3$\3\3\2\2\2")
        buf.write("%)\5\6\4\2&)\5\b\5\2\')\7\6\2\2(%\3\2\2\2(&\3\2\2\2(\'")
        buf.write("\3\2\2\2)*\3\2\2\2*(\3\2\2\2*+\3\2\2\2+\5\3\2\2\2,-\5")
        buf.write("\n\6\2-\60\5\20\t\2.\61\5\n\6\2/\61\5\36\20\2\60.\3\2")
        buf.write("\2\2\60/\3\2\2\2\61\63\3\2\2\2\62\64\5\f\7\2\63\62\3\2")
        buf.write("\2\2\63\64\3\2\2\2\64\65\3\2\2\2\65\66\t\2\2\2\66@\3\2")
        buf.write("\2\2\678\5\n\6\289\5\20\t\29;\5 \21\2:<\5\f\7\2;:\3\2")
        buf.write("\2\2;<\3\2\2\2<=\3\2\2\2=>\t\2\2\2>@\3\2\2\2?,\3\2\2\2")
        buf.write("?\67\3\2\2\2@\7\3\2\2\2AE\7\3\2\2BD\n\3\2\2CB\3\2\2\2")
        buf.write("DG\3\2\2\2EC\3\2\2\2EF\3\2\2\2FH\3\2\2\2GE\3\2\2\2HI\t")
        buf.write("\2\2\2I\t\3\2\2\2JK\7\16\2\2KL\5\16\b\2LM\7\17\2\2M\13")
        buf.write("\3\2\2\2NO\7\32\2\2O\r\3\2\2\2PQ\7\b\2\2Q\17\3\2\2\2R")
        buf.write("S\5\30\r\2ST\5\22\n\2Ta\3\2\2\2UV\5\30\r\2VX\5\26\f\2")
        buf.write("WY\5\32\16\2XW\3\2\2\2XY\3\2\2\2Ya\3\2\2\2Z[\5\26\f\2")
        buf.write("[\\\5\32\16\2\\a\3\2\2\2]^\5\24\13\2^_\5\32\16\2_a\3\2")
        buf.write("\2\2`R\3\2\2\2`U\3\2\2\2`Z\3\2\2\2`]\3\2\2\2a\21\3\2\2")
        buf.write("\2bc\7\13\2\2c\23\3\2\2\2de\7\f\2\2e\25\3\2\2\2fg\7\r")
        buf.write("\2\2g\27\3\2\2\2hi\7\7\2\2i\31\3\2\2\2jk\7\7\2\2k\33\3")
        buf.write("\2\2\2lm\t\4\2\2m\35\3\2\2\2no\7\t\2\2o\37\3\2\2\2pq\7")
        buf.write("\n\2\2qr\7\4\2\2rs\5\16\b\2st\7\5\2\2t!\3\2\2\2\13(*\60")
        buf.write("\63;?EX`")
        return buf.getvalue()


class zmapParser ( Parser ):

    grammarFileName = "zmap.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#'", "'('", "')'", "'\n'", "<INVALID>", 
                     "<INVALID>", "'?'", "'*'", "'-->'", "'<--'", "'<->'", 
                     "'['", "']'", "'n'", "'ne'", "'e'", "'se'", "'s'", 
                     "'sw'", "'w'", "'nw'", "'u'", "'d'", "'<'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "LPAREN", "RPAREN", "NL", 
                      "DIRECTION", "NAME", "QUESTION", "STAR", "LARROW", 
                      "RARROW", "BARROW", "LBRACK", "RBRACK", "N", "NE", 
                      "E", "SE", "S", "SW", "W", "NW", "U", "D", "CLOSE" ]

    RULE_parse = 0
    RULE_ifmap = 1
    RULE_passage = 2
    RULE_comment = 3
    RULE_room = 4
    RULE_modifier = 5
    RULE_name = 6
    RULE_directed_arrow = 7
    RULE_larrow = 8
    RULE_rarrow = 9
    RULE_barrow = 10
    RULE_left_direction = 11
    RULE_right_direction = 12
    RULE_arrow = 13
    RULE_unknown = 14
    RULE_special = 15

    ruleNames =  [ "parse", "ifmap", "passage", "comment", "room", "modifier", 
                   "name", "directed_arrow", "larrow", "rarrow", "barrow", 
                   "left_direction", "right_direction", "arrow", "unknown", 
                   "special" ]

    EOF = Token.EOF
    T__0=1
    LPAREN=2
    RPAREN=3
    NL=4
    DIRECTION=5
    NAME=6
    QUESTION=7
    STAR=8
    LARROW=9
    RARROW=10
    BARROW=11
    LBRACK=12
    RBRACK=13
    N=14
    NE=15
    E=16
    SE=17
    S=18
    SW=19
    W=20
    NW=21
    U=22
    D=23
    CLOSE=24

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

        def ifmap(self):
            return self.getTypedRuleContext(zmapParser.IfmapContext,0)


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
            self.state = 32
            self.ifmap()
            self.state = 33
            self.match(zmapParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_ifmap)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [zmapParser.LBRACK]:
                    self.state = 35
                    self.passage()
                    pass
                elif token in [zmapParser.T__0]:
                    self.state = 36
                    self.comment()
                    pass
                elif token in [zmapParser.NL]:
                    self.state = 37
                    self.match(zmapParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 40 
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
        self.enterRule(localctx, 4, self.RULE_passage)
        self._la = 0 # Token type
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.room()
                self.state = 43
                self.directed_arrow()
                self.state = 46
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [zmapParser.LBRACK]:
                    self.state = 44
                    self.room()
                    pass
                elif token in [zmapParser.QUESTION]:
                    self.state = 45
                    self.unknown()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==zmapParser.CLOSE:
                    self.state = 48
                    self.modifier()


                self.state = 51
                _la = self._input.LA(1)
                if not(_la==zmapParser.EOF or _la==zmapParser.NL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.room()
                self.state = 54
                self.directed_arrow()
                self.state = 55
                self.special()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==zmapParser.CLOSE:
                    self.state = 56
                    self.modifier()


                self.state = 59
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
        self.enterRule(localctx, 6, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(zmapParser.T__0)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << zmapParser.T__0) | (1 << zmapParser.LPAREN) | (1 << zmapParser.RPAREN) | (1 << zmapParser.DIRECTION) | (1 << zmapParser.NAME) | (1 << zmapParser.QUESTION) | (1 << zmapParser.STAR) | (1 << zmapParser.LARROW) | (1 << zmapParser.RARROW) | (1 << zmapParser.BARROW) | (1 << zmapParser.LBRACK) | (1 << zmapParser.RBRACK) | (1 << zmapParser.N) | (1 << zmapParser.NE) | (1 << zmapParser.E) | (1 << zmapParser.SE) | (1 << zmapParser.S) | (1 << zmapParser.SW) | (1 << zmapParser.W) | (1 << zmapParser.NW) | (1 << zmapParser.U) | (1 << zmapParser.D) | (1 << zmapParser.CLOSE))) != 0):
                self.state = 64
                _la = self._input.LA(1)
                if _la <= 0 or _la==zmapParser.NL:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
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
        self.enterRule(localctx, 8, self.RULE_room)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(zmapParser.LBRACK)
            self.state = 73
            self.name()
            self.state = 74
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
        self.enterRule(localctx, 10, self.RULE_modifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(zmapParser.CLOSE)
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
        self.enterRule(localctx, 12, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
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
        self.enterRule(localctx, 14, self.RULE_directed_arrow)
        self._la = 0 # Token type
        try:
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.left_direction()
                self.state = 81
                self.larrow()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.left_direction()
                self.state = 84
                self.barrow()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==zmapParser.DIRECTION:
                    self.state = 85
                    self.right_direction()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.barrow()
                self.state = 89
                self.right_direction()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.rarrow()
                self.state = 92
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
        self.enterRule(localctx, 16, self.RULE_larrow)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
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
        self.enterRule(localctx, 18, self.RULE_rarrow)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
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
        self.enterRule(localctx, 20, self.RULE_barrow)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
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
        self.enterRule(localctx, 22, self.RULE_left_direction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
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
        self.enterRule(localctx, 24, self.RULE_right_direction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
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
        self.enterRule(localctx, 26, self.RULE_arrow)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
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
        self.enterRule(localctx, 28, self.RULE_unknown)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
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
        self.enterRule(localctx, 30, self.RULE_special)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(zmapParser.STAR)
            self.state = 111
            self.match(zmapParser.LPAREN)
            self.state = 112
            self.name()
            self.state = 113
            self.match(zmapParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





