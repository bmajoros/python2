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
from Bed3Record import Bed3Record
from Bed6Record import Bed6Record
import re
#=========================================================================
# Attributes:
#   fh : file handle
# Instance Methods:
#   reader=BedReader(filename)
#   record=reader.nextRecord() # Bed3Record or Bed6Record
#   reader.close()
#   list=BedReader.readAll(filename)
#   hash=BedReader.hashBySubstrate(filename) # chr -> list of records
# Class Methods:
#   
#=========================================================================
class BedReader:
    """BedReader reads bed3 and/or bed6 files"""
    def __init__(self,filename):
        self.fh=open(filename,"r")
    @classmethod
    def readAll(cls,filename):
        reader=BedReader(filename)
        array=[]
        while(True):
            record=reader.nextRecord()
            if(not record): break
            array.append(record)
        reader.close()
        return array
    @classmethod
    def hashBySubstrate(cls,filename):
        list=cls.readAll(filename)
        hash={}
        for rec in list:
            if(hash.get(rec.chr,None) is None):
                hash[rec.chr]=[]
            hash[rec.chr].append(rec)
        return hash
    def close(self):
        self.fh.close()
    def nextRecord(self):
        while(True):
            line=self.fh.readline()
            if(not line): return None
            if(not re.search("\S",line)): continue
            line=line.rstrip()
            line=line.lstrip()
            fields=line.split()
            n=len(fields)
            if(n==3):
                return Bed3Record(fields[0],int(fields[1]),int(fields[2]))
            if(n==4):
                return Bed6Record(fields[0],int(fields[1]),int(fields[2]),
                                  fields[3],0.0,".")
            if(n==5):
                return Bed6Record(fields[0],int(fields[1]),int(fields[2]),
                                  fields[3],float(fields[4]),".")
            if(n==6):
                return Bed6Record(fields[0],int(fields[1]),int(fields[2]),
                                  fields[3],float(fields[4]),fields[5])
            raise Exception("wrong number of fields in bed file: "+line)
