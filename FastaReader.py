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
import re

#=========================================================================
# Attributes:
#   fh : file handle
#   shouldUppercase : whether to uppercase all letters
#   save : buffered line
# Instance Methods:
#   reader=FastaReader(filename)
#   reader=readerFromFileHandle(fileHandle);
#   (defline,sequence)=reader.nextSequence() # returns None at eof
#   reader.close()
#   reader.dontUppercase()
#   reader.doUppercase()
# Class Methods:
#   size=FastaReader.getSize(filename)
#   num=FastaReader.countEntries(filename)
#   FastaReader.readAll(filename) # returns hash : id->sequence
#   FastaReader.readAllAndKeepDefs(filename) # returns hash : id->[def,seq]
#   FastaReader.readAllIntoArray(filename) # [def,seq]
#   (defline,seq)=FastaReader.firstSequence(filename)
#   (id,attribute_hash)=FastaReader.parseDefline(defline)
#=========================================================================
class FastaReader:
    """FastaReader"""
    def __init__(self,filename):
        self.shouldUppercase=True
        self.save=None
        if(filename is not None):
            self.fh=open(filename,"r")

    @classmethod
    def readerFromFileHandle(cls,fh):
        reader=FastaReader()
        reader.fh=fh

    def close(self):
        self.fh.close()

    def dontUppercase(self):
        self.shouldUppercase=False

    def doUppercase(self):
        self.shouldUppercase=True

    def nextSequence(self):
        defline=""
        seq=""
        fh=self.fh
        while(True):
            if(self.save):
                line=self.save
                self.save=None
            else:
                line=fh.readline()
                if(line): line=line.rstrip()
            if(not line): return None # [None,None]
            if(re.search("^\s*>",line)):
                defline=line
                while(True):
                    line=fh.readline()
                    if(not line): break;
                    line=line.rstrip()
                    if(re.search("^\s*>",line)):
                        self.save=line
                        break
                    "".join(line.split())
                    if(self.shouldUppercase): seq+=line.upper()
                    else: seq+=line
                return [defline,seq]

    @classmethod
    def getSize(cls,filename):
        reader=FastaReader(filename)
        size=0
        while(True):
            [defline,seq]=reader.nextSequence()
            if(not defline): break
            size+=len(seq)
        reader.close()
        return size

    @classmethod
    def firstSequence(cls,filename):
        reader=FastaReader(filename)
        [defline,seq]=reader.nextSequence()
        reader.close()
        return [defline,seq]

    @classmethod
    def countEntries(cls,filename):
        n=0
        reader=FastaReader(filename)
        while(True):
            (defline,seq)=reader.nextSequence()
            if(not defline): break
            n+=1
        return n

    @classmethod
    def readAll(cls,filename):
        hash={}
        reader=FastaReader(filename)
        while(True):
            rec=reader.nextSequence()
            if(rec is None): break
            (defline,seq)=rec
            if(not defline): break
            match=re.search("^\s*>(\S+)",defline)
            if(not match): raise Exception("can't parse defline: "+defline)
            id=match.group(1)
            hash[id]=seq
        reader.close()
        return hash

    @classmethod
    def readAllIntoArray(cls,filename):
        array=[]
        reader=FastaReader(filename)
        while(True):
            (defline,seq)=reader.nextSequence()
            if(not defline): break
            array.append([defline,seq])
        reader.close()
        return array

    @classmethod
    def readAllAndKeepDefs(cls,filename):
        hash={}
        reader=FastaReader(filename)
        while(True):
            [defline,seq]=reader.nextSequence()
            if(not defline): break
            match=re.search("^\s*>(\S+)",defline)
            if(not match): raise Exception("can't parse defline: "+defline)
            id=match.group(1)
            hash[id]=[defline,seq]
        reader.close()
        return hash
    
    @classmethod
    def parseDefline(cls,defline):
        match=re.search("^\s*>\s*(\S+)(.*)",defline)
        if(not match): raise Exception("can't parse defline: "+defline)
        id=match.group(1)
        rest=match.group(2)
        attributes={}
        if(re.search("\S+",rest)):
            fields=rest.split()
            for field in fields:
                match=re.search("/(\S+)=(\S+)",field);
                if(match):
                    key=match.group(1)
                    value=match.group(2)
                    attributes[key]=value
        return [id,attributes]
