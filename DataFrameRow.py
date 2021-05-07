#=========================================================================
#Copyright (C)2021 William H. Majoros <bmajoros@alumni.duke.edu>
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 2018 William H. Majoros (bmajoros@alumni.duke.edu)
#=========================================================================
from __future__ import (absolute_import, division, print_function, 
   unicode_literals, generators, nested_scopes, with_statement)
from builtins import (bytes, dict, int, list, object, range, str, ascii,
   chr, hex, input, next, oct, open, pow, round, super, filter, map, zip)
import sys
#=========================================================================
# Attributes:
#   label : string
#   values : array of values
# Methods:
#   row=DataFrameRow()
#   elem=row[i] # first element is at 0 (the label is not counted)
#   label=row.getLabel()
#   raw=raw.getRaw()
#   row.rename(label)
#   n=row.length()
#   row.toInt()
#   row.toFloat()
#   row.append(value)
#   row.print(handle)
#   newRow=row.clone()
#   row.log()
#   row.log2()
#   row.log10()
#=========================================================================
class DataFrameRow:
   def __init__(self):
      self.label=""
      self.values=[]
   def log(self):
      values=self.values
      for i in range(len(values)):
         values[i]=log(values[i])
   def log2(self):
      values=self.values
      for i in range(len(values)):
         values[i]=log2(values[i])
   def log10(self):
      values=self.values
      for i in range(len(values)):
         values[i]=log10(values[i])
   def getRaw(self):
      return self.values
   def clone(self):
      r=DataFrameRow()
      r.label=self.label
      for x in self.values:
         r.values.append(x)
      return r
   def __getitem__(self,i):
      return self.values[i]
   def __setitem__(self,i,value):
      self.values[i]=value
   def print(self,handle):
      if(self.label!=""): print(self.label+"\t",end="",file=handle)
      print("\t".join([str(x) for x in self.values]),sep="",file=handle)
   def append(self,value):
      self.values.append(value)
   def length(self):
      return len(self.values)
   def getLabel(self):
      return self.label
   def rename(self,x):
      self.label=x
   def toInt(self):
      self.values=[int(x) for x in self.values]
   def toFloat(self):
      self.values=[float(x) for x in self.values]
