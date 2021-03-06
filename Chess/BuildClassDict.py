# -*- coding: utf-8 -*-
"""
Created on Thu May 25 15:15:27 2017

@author: Xinxin
"""
#funciton for define a CLass dictionary with id and key Class Object as valus
#output format: {key: class id, value: Class object}
              

# for class: get name and name and create a entity in dictionary with empty method and attrbute object.
# for attribute and class, create it as an dictionary and push it into the list of corresponding class

import re
import json
from defination import * # including the defination of Class Method and Attribute
from BuildSizeDict import *
    
def BuildClassDict(infile):        
    patternForType = r"^\(FAMIX\.(\w+) \(id\: (\d+)\)$"
    PFT = re.compile(patternForType)
    patternForAttr = r"^(\w+) \'(.*)\'$"
    PFA = re.compile(patternForAttr)
    patternForRef = r"^(\w+) ref: (\d+)$"
    PFR = re.compile(patternForRef)
    ClassDict = {} # with class id as key class object as value
    MethodDict = {} # with method id as key, method object as value
    AttrDict = {} # with attribut id as key, field object as value
    cnt = 0
    started = 0 # do not update the dictionary if it is the first loop
    #initialize variable, randomly initialize.
    ctype = "none"
    newTypObj = Class("0","",[],[],[])
    otherType = True
    print "Loading Data"
    with open(infile,"r") as f:
        for line in f.readlines():
            delta = len(line)-len(line.strip()) # use delta to distinguish if it is an entity name or the attributes in the entity.
            line = line.strip()
            if(delta == 2):
                # update the previous object
                if(started == 1):
                    if ctype == "Class" or ctype == "ParameterizableClass":
                        ClassDict[newTypObj.getID()] = newTypObj
                    elif ctype == "Method":
                        MethodDict[newTypObj.getID()] = newTypObj
                    elif ctype == "Attribute":
                        AttrDict[newTypObj.getID()] = newTypObj
                else:
                    started = 1
                # process the new object
                cmatch = PFT.match(line)
                if(cmatch):
                    ctype = cmatch.group(1)
                    cid = cmatch.group(2)
                    if ctype == "Class" or ctype == "ParameterizableClass":
                        newTypObj = Class(cid,"",[],[],[])
                        otherType = False
                    elif ctype == "Method":
                        newTypObj = Method(cid,"",[],"","")
                        otherType = False
                    elif ctype == "Attribute":
                        newTypObj = Attribute(cid,"",[],"")
                        otherType = False
                    else:
                        otherType = True # if not the type we need
                # genetate a new object to store entity 
                # get the entity name and id
            elif delta == 3 and not otherType:
                line = line.replace("(", "")
                line = line.replace(")", "")
                amatch = PFR.match(line)
                if(amatch): # if we find the match, it is a line for parentType information
                    aname = amatch.group(1)
                    if aname == "parentType":
                        newTypObj.updateParentType(amatch.group(2))
                else: # otherwise we try it with other attributes information
                    amatch = PFA.match(line)
                    if(amatch): 
                        aname = amatch.group(1)
                        if aname == "modifiers":
                            # for loop to get ever modifiers:
                            for i in range(2,len(amatch.groups())):
                                newTypObj.updateModifiers(amatch.group(i))
                        elif aname == "name":
                            newTypObj.updateName(amatch.group(2))
                        elif aname == "signature":
                            newTypObj.updateSignture(amatch.group(2))
            cnt+=1
            #if cnt%1000 == 0:
                #print "Processing Line: " + str(cnt)
            
    # we suppose to update the last processed object.
    # But, in our file, the last one is not within the three types we need, so we omit this step
    SizeDict = BuildSizeDict(infile)
    # after collect all information from file and build three dictionaries, update the class dictionary to match
    for mid in MethodDict:
        if(mid in SizeDict):
            MethodDict[mid].updateLOC(SizeDict[mid])
        cid =  MethodDict[mid].getParentType() # find the parent class id
        if cid not in ClassDict:
            continue
        classObj = ClassDict[cid] # get the class object
        classObj.updateMethods(MethodDict[mid]) # ipdate Methods list
        ClassDict[cid] = classObj #update the class dictionary
        
    for aid in AttrDict:
        if(aid in SizeDict):
            AttrDict[aid].updateLOC(SizeDict[aid])
        cid =  AttrDict[aid].getParentType() # find the parent class id
        if cid not in ClassDict:
            continue
        classObj = ClassDict[cid] # get the class object
        classObj.updateAttributes(AttrDict[aid]) # update Attributes list
        ClassDict[cid] = classObj #update the dictionary
    for cid in ClassDict:
        if(cid in SizeDict):
            ClassDict[cid].updateLOC(SizeDict[cid])
    print "Finished!"
    return ClassDict
        
        
        