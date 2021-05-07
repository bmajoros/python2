#!/usr/bin/env python
#=========================================================================
#Copyright (C)2021 William H. Majoros <bmajoros@alumni.duke.edu>
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
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
from Pipe import Pipe
import TempFilename
HEADERFILE=TempFilename.generate(".header")
SORTEDFILE=TempFilename.generate(".sorted")
#=========================================================================
# main()
#=========================================================================
if(len(sys.argv)!=4):
    exit(ProgramName.get()+" in.mtx.gz column out.mtx.gz\n    where column = 1-based field index\n")
(infile,index,outfile)=sys.argv[1:]
OUT=open(HEADERFILE,"wt")
numHeader=1
with gzip.open(infile,"rt") as IN:
    for line in IN:
        if(len(line)==0): raise Exception("unexpected empty line")
        if(line[0]=="%"): 
            numHeader+=1
            print(line,file=OUT,end="")
        else: 
            print(line,file=OUT,end="")
            break
IN.close(); OUT.close()
cmd="cat "+infile+" | gunzip | tail -n +"+str(numHeader+1)+\
    " | sort -g -k "+index+" > "+SORTEDFILE
Pipe.run(cmd)
cmd="cat "+HEADERFILE+" "+SORTEDFILE+" | gzip > "+outfile
Pipe.run(cmd)
Pipe.run("rm "+SORTEDFILE)
Pipe.run("rm "+HEADERFILE)
