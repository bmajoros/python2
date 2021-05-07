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
from SamRecord import SamRecord
from CigarString import CigarString

#=========================================================================
# Attributes:
#   fh : file handle
#   headerLines : array of header lines
# Instance Methods:
#   reader=SamReader(filename)
#   samRecord=reader.nextSequence() # returns None at EOF
#   (record,line)=reader.nextSeqAndText() # returns None at EOF
#   reader.close()
# Class Methods:
#=========================================================================
class SamReader:
    """SamReader"""
    def __init__(self,filename):
        self.headerLines=[]
        if(filename is not None):
            if(rex.find("\.gz$",filename)): self.fh=gzip.open(filename,"rt")
            else: self.fh=open(filename,"r")

    def close(self):
        self.fh.close()

    def nextSequence(self):
        pair=self.nextSeqAndText()
        if(pair is None): return None
        (rec,line)=pair
        return rec

    def nextSeqAndText(self):
        headerChars=set(["@","["])
        fh=self.fh
        line=fh.readline()
        if(line is None): return None
        while(line is not None and len(line)>0 and line[0] in headerChars):
            if(line[0]=="@"): self.headerLines.append(line)
            line=fh.readline()
        if(line is None or len(line)==0): return None
        fields=line.rstrip().split()
        if(len(fields)<11): raise Exception("can't parse sam line: "+line)
        (ID,flags,refName,refPos,mapQual,cigar,rnext,pnext,templateLen,
         seq,qual)=fields[:11]
        refPos=int(refPos)-1 # convert 1-based to 0-based
        flags=int(flags)
        CIGAR=CigarString(cigar)
        tags=fields[11:]
        rec=SamRecord(ID,refName,refPos,CIGAR,seq,flags,tags)
        return (rec,line)

# M03884:303:000000000-C4RM6:1:1101:1776:15706    99      chrX:31786371-31797409  6687    44      150M    =       6813    271     ATACTATTGCTGCGGTAATAACTGTAACTGCAGTTACTATTTAGTGATTTGTATGTAGATGTAGATGTAGTCTATGTCAGACACTATGCTGAGCATTTTATGGTTGCTATGTACTGATACATACAGAAACAAGAGGTACGTTCTTTTACA  BBBBFFFFFFFGGGGGEFGGFGHFHFFFHHHFFHHHFHFHHHGFHEDGGHFHBGFHGBDHFHFFFHHHHFHHHHHGHGFFBGGGHFHFFHHFFFFHHHHGHGFHHGFHGHHHGFHFFHHFHHFFGFFFFGGEHFFEHHFGHHHGHHHHFB  AS:i:300        XN:i:0  

