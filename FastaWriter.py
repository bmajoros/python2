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
import re
import os
#=========================================================================
# Attributes:
#   width
# Methods:
#   FastaWriter()
# Instance Methods:
#   writer=FastaWriter(optionalWidth)
#   writer.writeFasta(defline,sequence,filename)
#   writer.appendToFasta(defline,sequence,filename)
#   writer.addToFasta(defline,sequence,filehandle)
#=========================================================================
class FastaWriter:
    """FastaWriter"""
    def __init__(self,width=60):
        self.width=width
    def writeFasta(self,defline,seq,filename):
        with open(filename,"w") as fh:
            self.addToFasta(defline,seq,fh)
    def addToFasta(self,defline,seq,fh):
        defline=defline.rstrip()
        if(not re.search("^\s*>",defline)): defline=">"+defline
        fh.write(defline+"\n");
        length=len(seq)
        numLines=length//self.width
        if(length%self.width>0): numLines+=1
        start=0
        for i in range(0,numLines):
            line=seq[start:start+self.width]
            fh.write(line+"\n")
            start+=self.width
        if(length==0): fh.write("\n")
    def appendToFasta(self,defline,seq,filename):
        if(not os.path.exists(filename)):
            self.writeFasta(defline,seq,filename)
            return
        with open(filename,"a") as fh:
            self.addToFasta(defline,seq,fh)
