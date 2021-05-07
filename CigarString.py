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
# 2018 William H. Majoros (bmajoros@alumni.duke.edu)
#=========================================================================
from __future__ import (absolute_import, division, print_function,
   unicode_literals, generators, nested_scopes, with_statement)
from builtins import (bytes, dict, int, list, object, range, str, ascii,
   chr, hex, input, next, oct, open, pow, round, super, filter, map, zip)
from Rex import Rex
rex=Rex()
from CigarOp import CigarOp
from Interval import Interval
#=========================================================================
# Attributes:
#   ops : array of CigarOp
# Instance Methods:
#   cigar=CigarString(string)
#   bool=cigar.completeMatch()
#   numOps=cigar.length()
#   cigarOp=cigar[i] # returns a CigarOp object
#   str=cigar.toString()
#   cigar.computeIntervals(refPos)
#   ops=cigar.matchesByLength() # sorted by decreasing length
#   op=cigar.longestMatch() # returns a CigarOp object (or None)
#   L=cigar.longestMatchLen() # returns integer
#   (numMatches,numMismatches)=cigar.longestMatchStats(seq1,seq2) 
#       # ^ Returns none if no match; must call computeIntervals() first!
#   L=cigar.totalAlignmentLength()
#   cigar.setOps(ops)
#=========================================================================
class CigarString:
    """CigarString parses CIGAR strings (alignments)"""
    def __init__(self,cigar):
        self.ops=self.parse(cigar)
    def setOps(self,ops):
        self.ops=ops
    def matchesByLength(self):
        matches=[]
        for op in self.ops:
            if(op.getOp() in ("M","=","X")): matches.append(op)
        matches.sort(key=lambda x: -x.getLength())
        return matches
    def countIndelBases(self):
        N=0
        for op in self.ops:
            c=op.getOp()
            if(c=="I" or c=="D"): N+=1
        return N
    def totalAlignmentLength(self):
        L=0
        for op in self.ops:
            if(op.getOp() in ("M","=","X")): L+=op.getLength()
        return L
    def computeIntervals(self,refPos):
        ops=self.ops
        n=len(ops)
        begin1=0; begin2=refPos
        for i in range(n):
            op=ops[i]
            L=op.getLength()
            end1=begin1; end2=begin2
            if(op.advanceInQuery()): end1+=L
            if(op.advanceInRef()): end2+=L
            op.interval1=Interval(begin1,end1)
            op.interval2=Interval(begin2,end2)
            begin1=end1; begin2=end2
    def length(self):
        return len(self.ops)
    def __getitem__(self,i):
        return self.ops[i]
    def completeMatch(self):
        ops=self.ops
        return len(ops)==1 and ops[0].op in ("M","=","X")
    def longestMatchStats(self,query,ref):
        m=self.longestMatch()
        if(m is None): return None
        sub1=query[m.interval1.getBegin():m.interval1.getEnd()]
        sub2=ref[m.interval2.getBegin():m.interval2.getEnd()]
        matches=0; mismatches=0
        for i in range(len(sub1)):
            if(sub1[i]==sub2[i]): matches+=1
            else: mismatches+=1
        return (matches,mismatches)
    def longestMatchLen(self):
        m=self.longestMatch()
        if(m is None): return 0
        return m.getLength()
    def longestMatch(self):
        longest=None
        longestLength=0
        for op in self.ops:
            if(op.getOp()in ("M","=","X")):
                L=op.getLength()
                if(L>longestLength):
                    longest=op
                    longestLength=L
        return longest
    def toString(self):
        ops=self.ops
        s=""
        for op in ops:
            s+=str(op.length)
            s+=op.op
        return s
    def parse(self,cigar):
        array=[]
        if(cigar=="*"): return array
        while(len(cigar)>0):
            if(not rex.find("(\d+)(.)",cigar)):
                raise Exception("Can't parse CIGAR string: "+cigar)
            L=int(rex[1])
            op=rex[2]
            rec=CigarOp(op,L)
            array.append(rec)
            rex.find("\d+.(.*)",cigar)
            cigar=rex[1]
        return array
