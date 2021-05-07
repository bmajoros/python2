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
import subprocess
import sys
#=========================================================================
# Attributes:
#   iter
# Instance Methods:
#   pipe=Pipe(command)
#   line=pipe.readline()
# Class Methods:
#   output=Pipe.run(command)
#=========================================================================
class Pipe:
    """Pipe reads output from a shell command"""
    def __init__(self,cmd):
        p=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True,
                           stderr=subprocess.STDOUT)
        self.iter=iter(p.stdout.readline, b'')
    def readline(self):
        line=next(self.iter,None)
        if(line is None): return None
        line=line.decode(sys.stdout.encoding).rstrip()
        return line
    @classmethod
    def run(cls,cmd):
        line=subprocess.check_output(cmd,stderr=subprocess.STDOUT,shell=True)
        line=line.decode(sys.stdout.encoding).rstrip()
        return line
