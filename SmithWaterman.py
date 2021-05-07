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
import os
from Pipe import Pipe
from Rex import Rex
rex=Rex()
import TempFilename
from CigarString import CigarString
from FastaWriter import FastaWriter
#=========================================================================
# Attributes:
#   
# Instance Methods:
#   aligner=SmithWaterman(alignerDir,matrixFile,openPenalty,extrendPenalty)
#   cigarString=aligner.align(seq1,seq2)
#=========================================================================
class SmithWaterman:
    def __init__(self,alignerDir,matrixFile,gapOpenPenalty,gapExtendPenalty):
        self.alignerDir=alignerDir
        self.matrixFile=matrixFile
        self.gapOpen=gapOpenPenalty
        self.gapExtend=gapExtendPenalty
        self.fastaWriter=FastaWriter()
    def writeFile(self,defline,seq):
        filename=TempFilename.generate("fasta")
        self.fastaWriter.writeFasta(defline,seq,filename)
        return filename
    def swapInsDel(self,cigar):
        # This is done because my aligner defines insertions and deletions
        # opposite to how they're defined in the SAM specification
        newCigar=""
        for x in cigar:
            if(x=="I"): x="D"
            elif(x=="D"): x="I"
            newCigar+=x
        return newCigar
    def align(self,seq1,seq2):
        file1=self.writeFile("query",seq1)
        file2=self.writeFile("reference",seq2)
        cmd=self.alignerDir+"/smith-waterman -q "+self.matrixFile+" "+\
            str(self.gapOpen)+" "+str(self.gapExtend)+" "+file1+" "+file2+" DNA"
        output=Pipe.run(cmd)
        os.remove(file1)
        os.remove(file2)
        if(not rex.find("CIGAR=(\S+)",output)):
            raise Exception("Can't parse aligner output: "+output)
        cigar=rex[1]
        cigar=self.swapInsDel(cigar) # because I define cigars differently
        return CigarString(cigar)
