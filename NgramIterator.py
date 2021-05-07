#!/usr/bin/env python
#=========================================================================
# Copyright (C)2021 William H. Majoros <bmajoros@alumni.duke.edu>
#
# Permission is hereby granted, free of charge, to any person obtaining 
# a copy of this software and associated documentation files (the 
# "Software"), to deal in the Software without restriction, including 
# without limitation the rights to use, copy, modify, merge, publish, 
# distribute, sublicense, and/or sell copies of the Software, and to 
# permit persons to whom the Software is furnished to do so, subject 
# to the following conditions:
#
# The above copyright notice and this permission notice shall be included 
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#=========================================================================
from __future__ import (absolute_import, division, print_function, 
   unicode_literals, generators, nested_scopes, with_statement)
from builtins import (bytes, dict, int, list, object, range, str, ascii,
   chr, hex, input, next, oct, open, pow, round, super, filter, map, zip)
# The above imports should allow this program to run in both Python 2 and
# Python 3.  You might need to update your version of module "future".
######################################################################
#
# NgramIterator.py bmajoros
#
# Attributes:
#   array ngram : array of integer indices into alphabet string
#   string alphabet
# Methods:
#   ngramIterator=NgramIterator("ATCG",N)
#   string=ngramIterator.nextString() # returns None if no more
#   ngramIterator.reset()
# Private methods:
#   self.ngramToString()
######################################################################
class NgramIterator:
#---------------------------------------------------------------------
#                           PUBLIC METHODS
#---------------------------------------------------------------------
# ngramIterator=NgramIterator("ATCG",N)
    def __init__(self,alphabet,N):
        ngram=[]
        alphaSize=len(alphabet)
        for i in range(N-1): ngram.append(0)
        if(N>0): ngram.append(-1)
        self.alphabet=alphabet
        self.ngram=ngram
#---------------------------------------------------------------------
# ngramIterator.reset()
    def reset(self):
        ngram=self.ngram
        L=len(ngram)
        for i in range(L-1): ngram[i]=0
        ngram[L-1]=-1
#---------------------------------------------------------------------
# string=ngramIterator.nextString() # returns undef if no more
    def nextString(self):
        alphabet=self.alphabet
        ngram=self.ngram
        if(ngram is None): return None
        L=len(ngram)
        if(L==0):
            self.ngram=None
            return ""
        alphaSize=len(alphabet)
        for i in range(L-1,-1,-1): # for($i=$len-1 ; $i>=0 ; --$i)
            ngram[i]+=1
            index=ngram[i]
            if(index<alphaSize): return self.ngramToString()
            ngram[i]=0
        return None
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#                         PRIVATE METHODS
#---------------------------------------------------------------------
# self.ngramToString()
    def ngramToString(self):
        ngram=self.ngram
        alphabet=self.alphabet
        length=len(ngram)
        string=""
        for i in range(length):
            index=ngram[i]
            string+=alphabet[index:index+1]
        return string
