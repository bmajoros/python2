#====================================================================
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
#====================================================================
from __future__ import (absolute_import, division, print_function,     
   unicode_literals, generators, nested_scopes, with_statement)       
from builtins import (bytes, dict, int, list, object, range, str, ascii, 
   chr, hex, input, next, oct, open, pow, round, super, filter, map, zip)
import re
######################################################################
# Attributes:
#   hash
# Methods:
#   configFile=ConfigFile(filename)
#   value=configFile.lookup(key)
#   value=configFile.lookupOrDie(key)
# Private methods:
#   self.load(filename)
######################################################################
class ConfigFile:
    """ConfigFile stores variable assignments as key-value pairs
    in a hash
    """
    def __init__(self,filename):
        self.hash={}
        self.load(filename)
    def lookup(self,key):
        return self.hash[key]
    def lookupOrDie(self,key):
        if(self.hash[key] is None):
            raise Exception("$key not defined in config file\n")
        return self.hash[key]
    def load(self,filename):
        hash=self.hash
        with open(filename,"r") as fh:
            while(True):
                line=fh.readline()
                if(not line): break
                match=re.search("^(.*)#",line);
                if(match): line=match.group(1)
                match=re.search("^\s*(\S+)\s*=\s*(\S+)",line);
                if(match):
                    key=match.group(1)
                    value=match.group(2)
                    hash[key]=value
