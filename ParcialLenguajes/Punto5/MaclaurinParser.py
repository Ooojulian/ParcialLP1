# Generated from Maclaurin.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("\r\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\2\2\3\2")
        buf.write("\2\2\2\13\2\4\3\2\2\2\4\5\7\3\2\2\5\6\7\4\2\2\6\7\7\7")
        buf.write("\2\2\7\b\7\5\2\2\b\t\7\7\2\2\t\n\7\6\2\2\n\13\7\2\2\3")
        buf.write("\13\3\3\2\2\2\2")
        return buf.getvalue()


class MaclaurinParser ( Parser ):

    grammarFileName = "Maclaurin.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'calcular'", "'('", "','", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUM", "WS" ]

    RULE_inicio = 0

    ruleNames =  [ "inicio" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    NUM=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class InicioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(MaclaurinParser.NUM)
            else:
                return self.getToken(MaclaurinParser.NUM, i)

        def EOF(self):
            return self.getToken(MaclaurinParser.EOF, 0)

        def getRuleIndex(self):
            return MaclaurinParser.RULE_inicio

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInicio" ):
                listener.enterInicio(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInicio" ):
                listener.exitInicio(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInicio" ):
                return visitor.visitInicio(self)
            else:
                return visitor.visitChildren(self)




    def inicio(self):

        localctx = MaclaurinParser.InicioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_inicio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(MaclaurinParser.T__0)
            self.state = 3
            self.match(MaclaurinParser.T__1)
            self.state = 4
            self.match(MaclaurinParser.NUM)
            self.state = 5
            self.match(MaclaurinParser.T__2)
            self.state = 6
            self.match(MaclaurinParser.NUM)
            self.state = 7
            self.match(MaclaurinParser.T__3)
            self.state = 8
            self.match(MaclaurinParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





