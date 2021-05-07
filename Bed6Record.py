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
from Bed3Record import Bed3Record
#=========================================================================
# Inherited Attributes:
#   chr : string
#   interval : Interval
# Attributes:
#   name : string
#   score : float
#   strand : string
# Instance Methods:
#   record=Bed6Record(chr,begin,end,name,score,strand)
#   bool=isBed3()
#   bool=isBed6()
#   str=toString()
# Class Methods:
#   
#=========================================================================
class Bed6Record(Bed3Record):
    """Bed6Record represents a record in a BED6 file"""
    def __init__(self,chr,begin,end,name,score,strand):
        Bed3Record.__init__(self,chr,begin,end)
        self.name=name
        self.score=score
        self.strand=strand
    def isBed3(self):
        return False
    def isBed6(self):
        return True
    def toString(self):
        s=self.chr+"\t"+str(self.interval.begin)+"\t"+str(self.interval.end)\
            +"\t"+self.name
        if(self.score is not None): s+="\t"+str(self.score)
        if(self.strand is not None): s+="\t"+self.strand
        return s
