# Generated from Maclaurin.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MaclaurinParser import MaclaurinParser
else:
    from MaclaurinParser import MaclaurinParser

# This class defines a complete generic visitor for a parse tree produced by MaclaurinParser.

class MaclaurinVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MaclaurinParser#inicio.
    def visitInicio(self, ctx:MaclaurinParser.InicioContext):
        return self.visitChildren(ctx)



del MaclaurinParser