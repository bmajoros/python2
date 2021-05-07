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
# The above imports should allow this program to run in both Python 2 and
# Python 3.  You might need to update your version of module "future".
from GffTranscriptReader import GffTranscriptReader
#filename="/home/bmajoros/1000G/assembly/local-genes.gff"
#filename="/home/bmajoros/1000G/assembly/tmp.gff"
#filename="test/data/tmp.gff"
#filename="test/data/local-genes.gff"
filename="/home/bmajoros/ensembl/protein-coding.gff"
reader=GffTranscriptReader()
genes=reader.loadGenes(filename)
for gene in genes:
    exons=gene.getMergedExons()
    unmerged=0
    for transcript in gene.transcripts:
        unmerged+=len(transcript.getRawExons())
    print(unmerged,"exons merged to",len(exons))
    #for i in range(len(exons)):
    #    print("MERGED TO:",exons[i].begin,exons[i].end)
    #    print()
#transcripts=reader.loadGFF(filename)
#for transcript in transcripts:
    #print(transcript.getID())
    #gff=transcript.toGff()
    #print(gff)
#genes=reader.loadGenes(filename)
#for gene in genes:
#    print("gene",gene.getID())
#    n=gene.getNumTranscripts()
#    for i in range(n):
#        transcript=gene.getIthTranscript(i)
#        transID=transcript.getID()
#        print("\t"+transID+"\t"+str(transcript.getBegin())+"\t"
#              +str(transcript.getEnd()))
#hashTable=reader.hashBySubstrate(filename)
#keys=hashTable.keys()
#for key in keys:
#    print(key)
#hashTable=reader.hashGenesBySubstrate(filename)
#keys=hashTable.keys()
#for key in keys:
#    print(key)
#hashTable=reader.loadTranscriptIdHash(filename)
#keys=hashTable.keys()
#for key in keys:
#    print(key)
#hashTable=reader.loadGeneIdHash(filename)
#keys=hashTable.keys()
#for key in keys:
#    print(key)
