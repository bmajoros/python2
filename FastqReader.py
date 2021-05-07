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
# 2018 William H. Majoros (bmajoros@allumni.duke.edu)
#=========================================================================
from __future__ import (absolute_import, division, print_function,
   unicode_literals, generators, nested_scopes, with_statement)
from builtins import (bytes, dict, int, list, object, range, str, ascii,
   chr, hex, input, next, oct, open, pow, round, super, filter, map, zip)
from Rex import Rex
rex=Rex()
import gzip

#=========================================================================
# Attributes:
#   fh : file handle
# Instance Methods:
#   reader=FastqReader(filename) # can be gzipped!
#   (ID,seq,qual,qualSeq,pair)=reader.nextSequence() # returns None at EOF
#        * pair indicates which read of the pair: 1 or 2
#        * qual is an array of integer quality values
#        * qualSeq is the raw quality string
#   reader.close()
# Class Methods:
#=========================================================================
class FastqReader:
    """FastqReader"""
    def __init__(self,filename):
        if(filename is not None):
            if(rex.find("\.gz$",filename)): self.fh=gzip.open(filename,"rt")
            else: self.fh=open(filename,"r")

    def close(self):
        self.fh.close()

    def nextSequence(self):
        fh=self.fh
        line=fh.readline()
        if(line is None): return None
        if(len(line)==0): return None
        if(not rex.find("^(\S+)",line)):
            return None
            #raise Exception("Cannot parse fastq line: "+ID)
        ID=rex[1]
        pair=1
        if(rex.find("\s+(\d)",line)): pair=int(rex[1])
        seq=fh.readline().rstrip()
        junk=fh.readline()
        qualSeq=fh.readline().rstrip()
        qual=[ord(x)-33 for x in qualSeq]
        return (ID,seq,qual,qualSeq,pair)
        


