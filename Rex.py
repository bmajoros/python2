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
#=========================================================================
# Attributes:
#   match : returned from re.search()
# Instance Methods:
#   rex=Rex()
#   bool=rex.find("abc(\d+)def(\d+)ghi(\d+)",line)
#   rex.findOrDie("abc(\d+)def(\d+)ghi(\d+)",line)
#   x=rex[1]; y=rex[2]; z=rex[3]
#=========================================================================
class Rex:
    """Rex -- more compact regular expression matching similar to Perl"""
    def __init__(self):
        match=None
    def find(self,pattern,line):
        self.match=re.search(pattern,line)
        return self.match is not None
    def split(self,pattern,line):
        fields=re.split(pattern,line)
        nonEmpty=[]
        for x in fields:
            if(x!=""): nonEmpty.append(x)
        return nonEmpty
    def findOrDie(self,pattern,line):
        if(not self.find(pattern,line)): raise Exception("can't parse: "+line)
    def __getitem__(self,index):
        return self.match.group(index)
def test_regex():
    rex=Rex()
    line="chr1 HAVANA  initial-exon    34384   34457   .       -       0       transcript_id=ENST00000361813.5;gene_id=ENSG00000198952.7;\n"
    result=rex.find('transcript_id[:=]?\s*"?([^\s";]+)"?',line)
    #result=rex.find('transcript_id=([^\s";]+)',line)
    print(result)
    #x=y=z=None
    #if(rex.find("abc(\d+)abc(\d+)abc","ab123abc456abc789")):
    #    x=rex[1]; y=rex[2]
    #elif(rex.find("dog(\d+)cat(\d+)cow(\d+)chicken(\d+)",
    #              "dog1cat2cow8chicken100")):
    #    x=rex[1]; y=rex[4]
    #print(x,y)
