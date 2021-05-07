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
import random
#=========================================================================
# Attributes:
#   
# Instance Methods:
#   shuffler=Shuffler()
# Class Methods:
#   Shuffler.shuffleArray(array)
#   s=Shuffler.shuffleString(s)
#=========================================================================
class Shuffler:
    """Shuffler shuffles arrays and strings"""
    def __init__(self):
        pass
    @classmethod
    def shuffleArray(cls,array):
        L=len(array)
        for i in range(L):
            j=random.randint(0,L-1)
            temp=array[i]
            array[i]=array[j]
            array[j]=temp
    @classmethod
    def shuffleString(cls,string):
        L=len(string)
        ret=string
        for i in range(L):
            j=random.randint(0,L-1)
            if(j==i): continue
            if(j>i):
                ret=ret[0:i]+ret[j]+ret[i+1:j]+ret[i]+ret[j+1:L]
            else:
                ret=ret[0:j]+ret[i]+ret[j+1:i]+ret[j]+ret[i+1:L]
        return ret
