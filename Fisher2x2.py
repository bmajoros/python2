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
from Pipe import Pipe

#=========================================================================
# Attributes:
#   Matrix of the form:
#       x00  x01
#       x10  x11
# Instance Methods:
#   fisher=Fisher2x2(x00,x01,x10,x11)
#   P=fisher.getPvalue()
#   (exp00,exp01,exp10,exp11)=fisher.getExpectedCounts()
# Class Methods:
#   
#=========================================================================
class Fisher2x2:
    """Fisher2x2 performs Fisher's exact test for 2x2 contingency tables"""
    def __init__(self,x00,x01,x10,x11):
        self.x00=x00
        self.x01=x01
        self.x10=x10
        self.x11=x11

    def getPvalue(self):
        executable=Pipe.run("which fisher-exact-test.R")
        cmd=executable+" "+str(self.x00)+" "+str(self.x01)+" "+\
            str(self.x10)+" "+str(self.x11)
        P=float(Pipe.run(cmd))
        return P

    def getExpectedCounts(self):
        x00=float(self.x00); x01=float(self.x01)
        x10=float(self.x10); x11=float(self.x11)
        N=x00+x01+x10+x11
        pTop=(x00+x01)/N
        pBottom=1.0-pTop
        leftSum=x00+x10
        rightSum=x01+x11
        exp00=int(round(pTop*leftSum,0))
        exp01=int(round(pTop*rightSum,0))
        exp10=int(round(pBottom*leftSum,0))
        exp11=int(round(pBottom*rightSum,0))
        return (exp00,exp01,exp10,exp11)
        


