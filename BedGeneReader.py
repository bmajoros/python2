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
from BedReader import BedReader
from BedGene import BedGene

#=========================================================================
# Attributes:
#   
# Instance Methods:
#   reader=BedGeneReader()
#   genes=reader.read(CDS_filename,UTR_filename=None)
# Class Methods:
#
# Private Methods:
#   genes=self.readCDS(filename)
#   self.addUTR(filename,genes)
#   hash=self.hashGenes(genes)
#=========================================================================
class BedGeneReader:
    """BedGeneReader reads BedGene objects from a BED file"""
    def __init__(self):
        pass

    def read(self,CDS_filename,UTR_filename=None):
        genes=self.readCDS(CDS_filename)
        if(UTR_filename): self.addUTR(UTR_filename,genes)
        return genes

    def readCDS(self,filename):
        reader=BedReader(filename)
        genes=[]
        genesByName={}
        while(True):
            record=reader.nextRecord()
            if(not record): break
            if(not record.isBed6()):
                raise Exception("BED file has too few fields")
            id=record.name
            gene=genesByName.get(id,None)
            if(not gene):
                gene=BedGene(id,record.chr,record.strand)
                genesByName[id]=gene
                genes.append(gene)
            gene.addCDS(record.interval)
        reader.close()
        return genes

    def hashGenes(self,genes):
        hash={}
        for gene in genes:
            hash[gene.ID]=gene
        return hash

    def addUTR(self,filename,genes):
        hash=self.hashGenes(genes)
        reader=BedReader(filename)
        while(True):
            record=reader.nextRecord()
            if(not record): break
            if(not record.isBed6()):
                raise Exception("BED file has too few fields")
            id=record.name
            gene=hash.get(id,None)
            if(not gene): 
                gene=BedGene(id,record.chr,record.strand)
                genes.append(gene)
                hash[id]=gene
            gene.addUTR(record.interval)
        for gene in genes:
            gene.coalesce()
