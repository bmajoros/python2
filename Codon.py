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

######################################################################
# bmajoros@duke.edu 10/15/2016
#
# Represents a single trinucleotide at a certain place within an exon.
# Stores its location both relative to the transcript and to the
# genomic axis.  All coordinates are zero-based and space-based.  On
# the forward strand, the absoluteCoord represents the position of the
# leftmost base in the codon, whereas on the reverse strand,
# the absoluteCoord points to the base immediately following the third
# base of the codon.  Thus, on the minus strand, a substring operation
# on the genomic axis should begin at absoluteCoord-3.  RelativeCoords
# are much simpler: a substring operation on the transcript always
# uses the relativeCoord as-is, regardless of strand.
#
# Attributes:
#   string triplet
#   int absoluteCoord : relative to genomic axis
#   int relativeCoord : relative to current exon
#   bool isInterrupted : exon ends before codon is complete
#   int basesInExon :  how many bases of this codon are in this exon (1-3)
#   Exon exon : which exon contains this codon
# Methods:
#   codon=Codon(exon,triplet,relative,absolute,isInterrupted)
######################################################################

class Codon:
    def __init__(self,exon,triplet,relative,absolute,isInterrupted):
        if(relative is None): raise Exception("relative is not set")
        self.triplet=triplet
        self.exon=exon
        self.relativeCoord=relative
        self.absoluteCoord=absolute
        self.isInterrupted=isInterrupted

        
