#=========================================================================
#Copyright (C)2021 William H. Majoros <bmajoros@alumni.duke.edu>
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#=========================================================================
from __future__ import (absolute_import, division, print_function, 
   unicode_literals, generators, nested_scopes, with_statement)
from builtins import (bytes, dict, int, list, object, range, str, ascii,
   chr, hex, input, next, oct, open, pow, round, super, filter, map, zip)
######################################################################
# Represents a token in a Essex file --- either a parenthesis or a
# literal (a literal is anything other than a parenthesis: a tag/ident-
# ifier, number, or string).  Note that the scanner can't differentiate
# between a tag and a datum, so the parser must do this.
#
# Attributes:
#   tokenType : one of "(", ")", or "L" (literal)
#   lexeme : string
# Methods:
#   token=EssexToken(type,lexeme)
#   type=token.getType()
#   string=token.getLexeme()
#   bool=token.sOpenParen()
#   bool=token.isCloseParen()
#   bool=token.isLiteral()
######################################################################
class EssexToken:
    def __init__(self,type,lexeme=None):
        self.type=type
        if(lexeme is not None and len(lexeme)>0):
            self.lexeme=lexeme
    def getType(self):
        return self.type
    def getLexeme(self):
        return self.lexeme
    def isOpenParen(self):
        return self.type=="("
    def isCloseParen(self):
        return self.type==")"
    def isLiteral(self):
        return self.type=="L"
