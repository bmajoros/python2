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
# Author: William H. Majoros (bmajoros@alumni.duke.edu)
#=========================================================================
from __future__ import (absolute_import, division, print_function, 
   unicode_literals, generators, nested_scopes, with_statement)
from builtins import (bytes, dict, int, list, object, range, str, ascii,
   chr, hex, input, next, oct, open, pow, round, super, filter, map, zip)
# The above imports should allow this program to run in both Python 2 and
# Python 3.  You might need to update your version of module "future".
import sys
import ProgramName
import gzip
from Rex import Rex
rex=Rex()

#=========================================================================
# Attributes:
#    FH : file handle
#    header : array of int
#    nextLine : string
# Instance Methods:
#    MatrixMarket(filename)
#    nextGroup(self,colIndex)
#    getHeader()
# Class Methods:
#    allGroups=loadFile(filename,colIndex)
#=========================================================================
class MatrixMarket:
    def __init__(self,filename):
        if(rex.find("\.gz$",filename)):
            self.FH=gzip.open(filename,"rt")
        else:
            self.FH=open(filename,"rt")
        self.header=None
        self.nextLine=None

    def getHeader(self):
        return self.header

    def nextGroup(self,colIndex):
        line=None
        # First, see if the header needs to be parsed
        while(True):
            line=self.nextLine
            if(line is None): line=self.FH.readline()
            if(line is None): return None
            L=len(line)
            if(L>0 and line[0]=="%"): continue
            break
        # The first non-comment line contains the totals
        if(self.header is None):
            self.header=line.rstrip().split()
            self.header=[int(x) for x in self.header]
            line=self.FH.readline()
        # Now we can read in the next group of lines
        prevID=None
        group=[]
        if(self.nextLine is not None): # buffered from previous call
            prevID=int(self.nextLine.rstrip().split()[colIndex])
        while(True):
            fields=line.rstrip().split()
            if(len(fields)==0): return None
            if(prevID is None): prevID=int(fields[colIndex])
            if(colIndex>len(fields)-1):
                raise Exception("colIndex=",colIndex,"len(fields)=",len(fields))
            thisID=int(fields[colIndex])
            if(thisID!=prevID):
                self.nextLine=line
                return group
            group.append(fields)
            line=self.FH.readline()
            if(line is None): return None

    @classmethod
    def loadFile(self,filename,colIndex):
        reader=MatrixMarket(filename)
        groups=[]
        while(True):
            group=reader.nextGroup(colIndex)
            if(group is None): break
            groups.append(group)
        return groups
