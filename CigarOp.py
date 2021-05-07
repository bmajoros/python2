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
from Interval import Interval
ADVANCE_QUERY=set(["M","I","S","H","=","X"])
ADVANCE_REF=set(["M","D","N","=","X"])
#=========================================================================
# Attributes:
#   length : integer
#   interval1 : Interval (in sequence 1 = query)
#   interval2 : Interval (in sequence 2 = reference)
#   op : M(or =/X)/I/D/S:
#                                                              consumes
#                                                              query ref
#     M 0 alignment match (can be a sequence match or mismatch) yes yes
#     I 1 insertion to the reference                            yes  no
#     D 2 deletion from the reference                            no yes
#     N 3 skipped region from the reference                      no yes
#     S 4 soft clipping (clipped sequences present in SEQ)      yes  no
#     H 5 hard clipping (clipped sequences NOT present in SEQ)   no  no
#     P 6 padding (silent deletion from padded reference)        no  no
#     = 7 sequence match                                        yes yes
#     X 8 sequence mismatch                                     yes yes
# Instance Methods:
#   op=CigarOp("M",135)
#   bool=op.advanceInQuery()   # matches, insertions, etc.
#   bool=op.advanceInRef() # matches, deletions, etc.
#   op=op.getOp()
#   L=op.getLength()
#   interval=op.getQueryInterval() # sequence 1
#   interval=op.getRefInterval() # sequence 2
#=========================================================================
class CigarOp:
    def __init__(self,op,L):
        self.op=op
        self.length=L
        self.interval1=None
        self.interval2=None
    def getQueryInterval(self):
        return self.interval1
    def getRefInterval(self):
        return self.interval2
    def getOp(self): 
        return self.op
    def getLength(self):
        return self.length
    def advanceInQuery(self):
        return self.op in ADVANCE_QUERY
    def advanceInRef(self):
        return self.op in ADVANCE_REF
