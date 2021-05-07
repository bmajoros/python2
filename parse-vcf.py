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
import os
import gzip

if(len(sys.argv)!=3):
   print(sys.argv[0]+" <in.vcf.gz> <indiv>")
   sys.exit(0)
(infile,indiv)=sys.argv[1:]

numIndiv=None
with gzip.open(infile,"rt") as IN:
   for line in IN:
      line.rstrip("\n")
      fields=line.split()
      if len(fields)<7: continue
      if fields[0]=="#CHROM":
         individuals=fields[9:]
         numIndiv=len(individuals)
         genotype={}
         for id in individuals: genotype[id]=[]
      elif fields[6]=="PASS":
         [chr,pos,id,ref,alt]=fields[:5]
         #print(id+":chr"+chr+":"+pos+":"+ref+":"+alt+"\t")
         genotypes=fields[9:]
         for i in range(0,numIndiv):
            id=individuals[i]
            gt=genotypes[i]
            genotype[id].append(gt)
print("\n")
for id in individuals:
   gt=genotype[id]
   print(id+"\t"+"\t".join(gt))

