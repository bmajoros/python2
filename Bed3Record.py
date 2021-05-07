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
from Interval import Interval

#=========================================================================
# Attributes:
#   chr : string
#   interval : Interval
# Instance Methods:
#   record=Bed3Record(chr,begin,end)
#   bool=record.isBed3()
#   bool=record.isBed6()
#   begin=record.getBegin()
#   end=record.getEnd()
#   line=record.toString()
# Class Methods:
#   
#=========================================================================
class Bed3Record:
    """Bed3Record represents a record in a BED3 file"""
    def __init__(self,chr,begin,end):
        self.chr=chr
        self.interval=Interval(begin,end)

    def isBed3(self):
        return True

    def isBed6(self):
        return False

    def getBegin(self):
        return self.interval.begin

    def getEnd(self):
        return self.interval.end

    def toString(self):
        return self.chr+"\t"+str(self.interval.begin)+"\t"+\
            str(self.interval.end)
