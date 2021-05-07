#!/usr/bin/env python
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
from FastaReader import FastaReader
from FastaWriter import FastaWriter
from Translation import Translation
#filename="/home/bmajoros/1000G/assembly/combined/HG00096/1.fasta"
#reader=FastaReader("/home/bmajoros/1000G/assembly/combined/HG00096/1.fasta")
#while(True):
#    [defline,seq]=reader.nextSequence()
#    if(not defline): break
#    print("defline="+defline);
#    L=len(seq)
#    print("length="+str(L))
#filename="/home/bmajoros/1000G/assembly/BRCA1-NA19782.fasta";
filename="/Users/bmajoros/python/test/data/subset.fasta"
print(FastaReader.getSize(filename))
[defline,seq]=FastaReader.firstSequence(filename)
print(len(seq))
#filename="/home/bmajoros/1000G/assembly/test.fasta"
filename="/Users/bmajoros/python/test/data/subset.fasta"
hash=FastaReader.readAllAndKeepDefs(filename)
for key in hash.keys():
    [defline,seq]=hash[key]
    print(defline)
    [id,attrs]=FastaReader.parseDefline(defline)
    print("id="+id)
    for key,value in attrs.items():
        print(key+"="+value)
writer=FastaWriter()
writer.writeFasta(">ABCD","ATCGATCGTAGCTAGTCTGCGCGTATCGTCAGTCTCTATCGATCGTACTGCGATCTAGCTAGCTGATCGTAGCTTCTATGACTGCTAGTCATCTAGCTAGCTGATCGTAGCTGCGCGCGATATATTGCATCTATGCTATCATTGCATGCTAGCTCTAGCTAGTCGATGCTATCTTAGCTAC","test1.fasta")
writer.appendToFasta(">XYZ","GATTACA","test1.fasta")
print(Translation.translate(seq))
print("forward:",seq)
print("revcomp: ",Translation.reverseComplement(seq))
