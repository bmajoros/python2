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
import math
NEGATIVE_INFINITY=float("-inf")
def sumLogProbs_ordered(largerValue,smallerValue):
    if(smallerValue==NEGATIVE_INFINITY): return largerValue
    return largerValue+math.log(1+math.exp(smallerValue-largerValue))
def sumLogProbs2(logP,logQ):
    if(logP>logQ): return sumLogProbs_ordered(logP,logQ)
    return sumLogProbs_ordered(logQ,logP)
def sumLogProbs(x):
    n=len(x)
    if(n==1): return x[0]
    if(n==0): return NEGATIVE_INFINITY
    # Pull out the largest value
    largestValue=x[0]
    for v in x:
        if(v>largestValue): largestValue=v
    # Handle the case of all zeros separately
    if(largestValue==NEGATIVE_INFINITY): return NEGATIVE_INFINITY
    # Apply the Kingsbury-Raynor formula
    sum=0.0;
    for v in x:
        if(v==NEGATIVE_INFINITY): continue
        sum+=math.exp(v-largestValue)
    return largestValue+math.log(sum)
#v=[math.log(0.0001),math.log(0.0002),math.log(0.0003)]
#print(math.exp(sumLogProbs2(math.log(0.1),math.log(0.2))))
#print(math.exp(sumLogProbs(v)))
