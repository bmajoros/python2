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
import os
#=========================================================================
# Attributes:
#   commands : array of string
#   niceValue : empty, or integer (nice value)
#   memValue : empty, or integer (mem value, in megabytes)
#   queue : partition name
#   threadsValue : number of CPUs requested
# Instance Methods:
#   SlurmWriter()
#   slurm.addCommand(cmd)
#   slurm.nice() # turns on "nice" (sets it to 100 by default)
#   slurm.mem(1500)
#   slurm.threads(16)
#   slurm.setQueue("new,all")
#   slurm.writeArrayScript(slurmDir,jobName,maxParallel,
#                           additional_SBATCH_lines)
#=========================================================================
class SlurmWriter:
    """SlurmWriter"""
    def __init__(self):
        self.commands=[]
        self.niceValue=0
        self.memValue=0
        self.threadsValue=0
        self.queue=None
    def addCommand(self,cmd):
        self.commands.append(cmd)
    def nice(self,value=100):
        self.niceValue=value
    def mem(self,value):
        self.memValue=value
    def threads(self,value):
        self.threadsValue=value
    def setQueue(self,value):
        self.queue=value
    def writeArrayScript(self,slurmDir,jobName,maxParallel,moreSBATCH=""):
        if(moreSBATCH is None): moreSBATCH=""
        if(int(maxParallel)<1): raise Exception("specify maxParallel parameter")
        moreSBATCH=moreSBATCH.rstrip()
        if(len(moreSBATCH)>0):
            moreSBATCH=moreSBATCH.rstrip()+"\n"
        #moreSBATCH=moreSBATCH+"\n"
        if(self.niceValue>0) :
            moreSBATCH+="#SBATCH --nice="+str(self.niceValue)+"\n"
        if(self.memValue>0):
            moreSBATCH+="#SBATCH --mem="+str(self.memValue)+"\n"
        if(self.threadsValue>0):
            moreSBATCH+="#SBATCH --cpus-per-task="+str(self.threadsValue)+"\n"
        queue=""
        if(len(self.queue)>0):
            queue="#SBATCH -p "+self.queue+"\n"
        if(os.path.exists(slurmDir)):
               os.system("rm -f "+slurmDir+"/*.slurm "+slurmDir+
                         "/outputs/*.output")
        os.system("mkdir -p "+slurmDir+"/outputs")
        commands=self.commands
        numCommands=len(commands)
        numJobs=numCommands
        for i in range(0,numCommands):
            command=commands[i]
            index=i+1
            filename=slurmDir+"/command"+str(index)+".sh"
            with open(filename,"w") as OUT:
                OUT.write("#!/bin/sh\n")
                OUT.write(command+"\n")
            os.system("chmod +x "+filename)
        filename=slurmDir+"/array.slurm"
        with open(filename,"w") as OUT:
            OUT.write("\n".join(
                    ["#!/bin/sh",
                     "#",
                     "#SBATCH --get-user-env",
                     "#SBATCH -J "+jobName,
                     "#SBATCH -A "+jobName,
                     "#SBATCH -o "+slurmDir+"/outputs/%a.output",
                     "#SBATCH -e "+slurmDir+"/outputs/%a.output",
                     "#SBATCH --array=1-"+str(numJobs)+"%"+str(maxParallel),
                     queue+moreSBATCH+"#",
                     slurmDir+"/command${SLURM_ARRAY_TASK_ID}.sh\n"
                     ]))
    def writeScript(self,slurmFile,outFile,jobName,command,moreSBATCH=""):
        if(moreSBATCH is None): moreSBATCH=""
        moreSBATCH=moreSBATCH.rstrip()
        if(len(moreSBATCH)>0):
            moreSBATCH=moreSBATCH.rstrip()+"\n"
        if(self.niceValue>0) :
            moreSBATCH+="#SBATCH --nice="+str(self.niceValue)+"\n"
        if(self.memValue>0):
            moreSBATCH+="#SBATCH --mem="+str(self.memValue)+"\n"
        if(self.threadsValue>0):
            moreSBATCH+="#SBATCH --cpus-per-task="+str(self.threadsValue)+"\n"
        queue=""
        if(len(self.queue)>0):
            queue="#SBATCH -p "+self.queue+"\n"
        with open(slurmFile,"w") as OUT:
            OUT.write("\n".join(
                    ["#!/bin/sh",
                     "#",
                     "#SBATCH --get-user-env",
                     "#SBATCH -J "+jobName,
                     "#SBATCH -A "+jobName,
                     "#SBATCH -o "+outFile,
                     "#SBATCH -e "+outFile,
                     queue+moreSBATCH+"#",
                     command
                     ]))
