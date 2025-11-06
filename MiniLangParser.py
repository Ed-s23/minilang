# Generated from MiniLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,130,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,0,1,
        1,1,1,4,1,30,8,1,11,1,12,1,31,1,1,5,1,35,8,1,10,1,12,1,38,9,1,3,
        1,40,8,1,1,1,5,1,43,8,1,10,1,12,1,46,9,1,1,2,1,2,1,2,1,2,1,2,3,2,
        53,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,
        5,5,5,70,8,5,10,5,12,5,73,9,5,1,5,1,5,1,5,5,5,78,8,5,10,5,12,5,81,
        9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,93,8,6,10,6,12,6,
        96,9,6,1,6,1,6,1,6,5,6,101,8,6,10,6,12,6,104,9,6,1,7,1,7,1,7,1,7,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,117,8,8,1,8,1,8,1,8,1,8,1,8,1,8,
        5,8,125,8,8,10,8,12,8,128,9,8,1,8,0,1,16,9,0,2,4,6,8,10,12,14,16,
        0,3,1,0,10,15,1,0,16,17,1,0,18,19,137,0,21,1,0,0,0,2,39,1,0,0,0,
        4,52,1,0,0,0,6,54,1,0,0,0,8,58,1,0,0,0,10,63,1,0,0,0,12,82,1,0,0,
        0,14,105,1,0,0,0,16,116,1,0,0,0,18,20,5,22,0,0,19,18,1,0,0,0,20,
        23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,
        0,24,25,3,2,1,0,25,26,5,0,0,1,26,1,1,0,0,0,27,36,3,4,2,0,28,30,5,
        22,0,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,
        33,1,0,0,0,33,35,3,4,2,0,34,29,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,
        0,36,37,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,39,27,1,0,0,0,39,40,
        1,0,0,0,40,44,1,0,0,0,41,43,5,22,0,0,42,41,1,0,0,0,43,46,1,0,0,0,
        44,42,1,0,0,0,44,45,1,0,0,0,45,3,1,0,0,0,46,44,1,0,0,0,47,53,3,6,
        3,0,48,53,3,8,4,0,49,53,3,10,5,0,50,53,3,12,6,0,51,53,3,16,8,0,52,
        47,1,0,0,0,52,48,1,0,0,0,52,49,1,0,0,0,52,50,1,0,0,0,52,51,1,0,0,
        0,53,5,1,0,0,0,54,55,5,20,0,0,55,56,5,1,0,0,56,57,3,16,8,0,57,7,
        1,0,0,0,58,59,5,2,0,0,59,60,5,3,0,0,60,61,3,16,8,0,61,62,5,4,0,0,
        62,9,1,0,0,0,63,64,5,5,0,0,64,65,5,3,0,0,65,66,3,14,7,0,66,67,5,
        4,0,0,67,71,5,6,0,0,68,70,5,22,0,0,69,68,1,0,0,0,70,73,1,0,0,0,71,
        69,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,71,1,0,0,0,74,75,3,2,1,
        0,75,79,5,7,0,0,76,78,5,22,0,0,77,76,1,0,0,0,78,81,1,0,0,0,79,77,
        1,0,0,0,79,80,1,0,0,0,80,11,1,0,0,0,81,79,1,0,0,0,82,83,5,8,0,0,
        83,84,5,3,0,0,84,85,3,6,3,0,85,86,5,9,0,0,86,87,3,14,7,0,87,88,5,
        9,0,0,88,89,3,6,3,0,89,90,5,4,0,0,90,94,5,6,0,0,91,93,5,22,0,0,92,
        91,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,97,1,0,0,
        0,96,94,1,0,0,0,97,98,3,2,1,0,98,102,5,7,0,0,99,101,5,22,0,0,100,
        99,1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,13,
        1,0,0,0,104,102,1,0,0,0,105,106,3,16,8,0,106,107,7,0,0,0,107,108,
        3,16,8,0,108,15,1,0,0,0,109,110,6,8,-1,0,110,117,5,21,0,0,111,117,
        5,20,0,0,112,113,5,3,0,0,113,114,3,16,8,0,114,115,5,4,0,0,115,117,
        1,0,0,0,116,109,1,0,0,0,116,111,1,0,0,0,116,112,1,0,0,0,117,126,
        1,0,0,0,118,119,10,5,0,0,119,120,7,1,0,0,120,125,3,16,8,6,121,122,
        10,4,0,0,122,123,7,2,0,0,123,125,3,16,8,5,124,118,1,0,0,0,124,121,
        1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,17,1,
        0,0,0,128,126,1,0,0,0,13,21,31,36,39,44,52,71,79,94,102,116,124,
        126
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'print'", "'('", "')'", "'if'", 
                     "'{'", "'}'", "'for'", "';'", "'>'", "'<'", "'=='", 
                     "'!='", "'>='", "'<='", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "NEWLINE", "WS" ]

    RULE_program = 0
    RULE_statementList = 1
    RULE_statement = 2
    RULE_assign = 3
    RULE_print = 4
    RULE_ifStatement = 5
    RULE_forStatement = 6
    RULE_condition = 7
    RULE_expr = 8

    ruleNames =  [ "program", "statementList", "statement", "assign", "print", 
                   "ifStatement", "forStatement", "condition", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    ID=20
    INT=21
    NEWLINE=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(MiniLangParser.StatementListContext,0)


        def EOF(self):
            return self.getToken(MiniLangParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.NEWLINE)
            else:
                return self.getToken(MiniLangParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 18
                    self.match(MiniLangParser.NEWLINE) 
                self.state = 23
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 24
            self.statementList()
            self.state = 25
            self.match(MiniLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.NEWLINE)
            else:
                return self.getToken(MiniLangParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementList" ):
                return visitor.visitStatementList(self)
            else:
                return visitor.visitChildren(self)




    def statementList(self):

        localctx = MiniLangParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3146028) != 0):
                self.state = 27
                self.statement()
                self.state = 36
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 29 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 28
                            self.match(MiniLangParser.NEWLINE)
                            self.state = 31 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==22):
                                break

                        self.state = 33
                        self.statement() 
                    self.state = 38
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)



            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 41
                self.match(MiniLangParser.NEWLINE)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(MiniLangParser.AssignContext,0)


        def print_(self):
            return self.getTypedRuleContext(MiniLangParser.PrintContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MiniLangParser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(MiniLangParser.ForStatementContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.print_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.forStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 51
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = MiniLangParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(MiniLangParser.ID)
            self.state = 55
            self.match(MiniLangParser.T__0)
            self.state = 56
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = MiniLangParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(MiniLangParser.T__1)
            self.state = 59
            self.match(MiniLangParser.T__2)
            self.state = 60
            self.expr(0)
            self.state = 61
            self.match(MiniLangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(MiniLangParser.ConditionContext,0)


        def statementList(self):
            return self.getTypedRuleContext(MiniLangParser.StatementListContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.NEWLINE)
            else:
                return self.getToken(MiniLangParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MiniLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(MiniLangParser.T__4)
            self.state = 64
            self.match(MiniLangParser.T__2)
            self.state = 65
            self.condition()
            self.state = 66
            self.match(MiniLangParser.T__3)
            self.state = 67
            self.match(MiniLangParser.T__5)
            self.state = 71
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 68
                    self.match(MiniLangParser.NEWLINE) 
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 74
            self.statementList()
            self.state = 75
            self.match(MiniLangParser.T__6)
            self.state = 79
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 76
                    self.match(MiniLangParser.NEWLINE) 
                self.state = 81
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.AssignContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.AssignContext,i)


        def condition(self):
            return self.getTypedRuleContext(MiniLangParser.ConditionContext,0)


        def statementList(self):
            return self.getTypedRuleContext(MiniLangParser.StatementListContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.NEWLINE)
            else:
                return self.getToken(MiniLangParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = MiniLangParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(MiniLangParser.T__7)
            self.state = 83
            self.match(MiniLangParser.T__2)
            self.state = 84
            self.assign()
            self.state = 85
            self.match(MiniLangParser.T__8)
            self.state = 86
            self.condition()
            self.state = 87
            self.match(MiniLangParser.T__8)
            self.state = 88
            self.assign()
            self.state = 89
            self.match(MiniLangParser.T__3)
            self.state = 90
            self.match(MiniLangParser.T__5)
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 91
                    self.match(MiniLangParser.NEWLINE) 
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 97
            self.statementList()
            self.state = 98
            self.match(MiniLangParser.T__6)
            self.state = 102
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 99
                    self.match(MiniLangParser.NEWLINE) 
                self.state = 104
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = MiniLangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.expr(0)
            self.state = 106
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 64512) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 107
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def INT(self):
            return self.getToken(MiniLangParser.INT, 0)

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 110
                self.match(MiniLangParser.INT)
                pass
            elif token in [20]:
                self.state = 111
                self.match(MiniLangParser.ID)
                pass
            elif token in [3]:
                self.state = 112
                self.match(MiniLangParser.T__2)
                self.state = 113
                self.expr(0)
                self.state = 114
                self.match(MiniLangParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 126
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 124
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = MiniLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 118
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 119
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 120
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = MiniLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 121
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 122
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 123
                        self.expr(5)
                        pass

             
                self.state = 128
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




