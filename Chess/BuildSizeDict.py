# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 18:13:09 2017

@author: Xinxin
"""
import re

# with the FAMIX.FileAnchor element we can find the size (line of code of each element, whose element id is indicated in element)
infile = "./src/src.mse"

def BuildSizeDict(infile):
    started = 0
    otherType = True
    ctype = ""
    tmpdict = {}
    SizeDict = {}
    
    patternForType = r"^\(FAMIX\.(\w+) \(id\: (\d+)\)$"
    PFT = re.compile(patternForType)
    patternForAttr = r"^(\w+) (.*)$"
    PFA = re.compile(patternForAttr)
    patternForRef = r"^(\w+) ref: (.*)$"
    PFR = re.compile(patternForRef)
    with open(infile,"r") as f:
        for line in f.readlines():
            delta = len(line)-len(line.strip()) # use delta to distinguish if it is an entity name or the attributes in the entity.
            line = line.strip()
            if(delta == 2):
                # update the previous object
                if(started == 1):
                    if ctype == "FileAnchor": 
                        SizeDict[tmpdict["elementId"]] = tmpdict["endLine"] - tmpdict["startLine"]+1
                else:
                    started = 1
                # process the new object
                cmatch = PFT.match(line)
                if(cmatch):
                    ctype = cmatch.group(1)
                    if ctype == "FileAnchor":
                        tmpdict = {"elementId":"0", "endLine": 0,"startLine": 0}
                        otherType = False
            elif delta == 3 and not otherType:
                line = line.replace("(", "")
                line = line.replace(")", "")
                amatch = PFR.match(line)
                if(amatch): # if we find the match, it is a line for element Id information
                    aname = amatch.group(1)
                    if aname == "element":
                        tmpdict["elementId"] = amatch.group(2)
                else: # otherwise we try it with other attributes information
                    amatch = PFA.match(line)
                    if(amatch): 
                        aname = amatch.group(1)
                        if aname == "endLine":
                            tmpdict["endLine"] = int(amatch.group(2))
                        elif aname == "startLine":
                            tmpdict["startLine"] = int(amatch.group(2))
    return SizeDict
                