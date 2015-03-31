#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
DESCRIPTION

ARGUMENTS : 

USAGE : 

"""

__author__ = "Thibault TUBIANA"
__version__  = "1.0.0"
__copyright__ = "copyleft"
__date__ = "2015/14"


#==============================================================================
#                     MODULES                            
#==============================================================================
import argparse
import os
import re
#==============================================================================
# TOOL FONCTION
#==============================================================================
    


def parseArg():
    """
    This fonction will the list of pdb files and the distance
    @return: dictionnary of arguments
    """
    arguments=argparse.ArgumentParser(description="\
            Description\
            ")
    arguments.add_argument('-n', "--name", help="file base name", required=True)
    args = vars(arguments.parse_args())
    return(args)
    

def find_time(basename):
    step_time_lambda=re.compile("^ +Step +Time +Lambda")
    time_line=re.compile("^ +[0-9]* +([0-9]*)\.[0-9]* *[0-9]*\.[0-9]*")
    logfile=open(basename+".log", "r")
    flag=False
    time=0
    for line in logfile:
        if flag==True:
            time=int(time_line.match(line).group(1))
            flag=False
            
        if step_time_lambda.match(line):
            flag=True

    return time


###############################################################################
#####                               MAIN                                 ######
###############################################################################

if __name__ == "__main__":
    print "******************************************************************"
    print "************  LAST FRAME EXTRACTOR (PDB saver)  ******************"
    print "******************************************************************"
    print ""
    #We get all arguments
    myArgs=parseArg()
    basename=myArgs["name"]
    
    timeMD=find_time(basename)
    
    tpr=basename+".tpr"
    
    if os.path.isfile(basename+"_cleaned.xtc"):
        xtc=basename+"_cleaned.xtc"
    elif os.path.isfile(basename+".xtc"):
        xtc=basename+".xtc"
    elif os.path.isfile(basename+".trr"):
        xtc=basename+".trr"
    else :
        print "ERROR ==> no trajectory file found (.trr or .xtc)"
        exit(1)
    pdb=basename+"_LF.pdb"
    os.system("echo \"1\" | trjconv -s %s -f %s -b %i -o %s" %(tpr,xtc, timeMD,pdb))    
    
    
    
    
    
    
    
