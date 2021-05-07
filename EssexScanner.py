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
from EssexToken import EssexToken
import re
######################################################################
#
# A token scanner for the EssexParser.
#
# Attributes:
#   file : file handle
#   ungot : char
#   nextTok : EssexToken
# Public Methods:
#   scanner=EssexScanner(filehandle)
#   scanner.close()
#   token=scanner.nextToken()
#   token=scanner.match(tokenType)
#   token=scanner.peek()
# Private Methods:
#   getChar
#   unGetChar
#   skipWhitespace
######################################################################
class EssexScanner:
    def __init__(self,file):
        self.file=file
        self.nextTok=None
        self.ungot=None
    def close(self):
        self.file.close()
    def nextToken(self):
        token=self.peek()
        self.nextTok=None
        return token
    def match(self,tokenType):
        token=self.nextToken()
        if(token.getType()!=tokenType):
            lexeme=token.getLexeme()
            raise Exception("Syntax error near \""+lexeme+"\"")
    def peek(self):
        if(not self.nextTok):
            file=self.file
            self.skipWhitespace()
            c=self.getChar()
            if(c is None): return None
            tokenType=None
            lexeme=""
            if(c=="(" or c==")"): tokenType=c
            else:
                tokenType="L"
                lexeme=c
                while(True):
                    c=self.getChar()
                    if(not c): break
                    if(re.search("[\s\(\)]",c)): break
                    lexeme+=c
                self.unGetChar(c)
            lexeme=lexeme.replace("&lparen;","(")
            lexeme=lexeme.replace("&rparen;",")")
            lexeme=lexeme.replace("&tab;","\t")
            lexeme=lexeme.replace("&space;"," ")
            self.nextTok=EssexToken(tokenType,lexeme)
        return self.nextTok
    def getChar(self):
        c=None
        if(self.ungot):
            c=self.ungot
            self.ungot=None
        else:
            c=self.file.read(1)
            if(len(c)==0): c=None
        return c
    def unGetChar(self,c):
        self.ungot=c
    def skipWhitespace(self):
        while(True):
            c=self.getChar()
            if(c is None): break
            if(c=="#"):
                while(True):
                    c=self.getChar()
                    if(c is None or c=="\n"): break
                continue
            if(not re.search("\s",c)):
                self.unGetChar(c)
                return
