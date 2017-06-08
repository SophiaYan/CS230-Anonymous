#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 14:52:52 2017

@author: shaojy11
"""

from toposort import *

def BuildEdgeList(filename, FilteredClassDict, filtered):
    EdgeList = []
    toMatch = 'FAMIX.Inheritance'
    with open(filename) as f:
        content = f.readlines()
    lines = [x.strip('\n') for x in content]
    
    for i, line in enumerate(lines):
        index = line.find(toMatch, 2)
        if (index != -1):
            subClassLine = lines[lines.index(line) + 1]
            superClassLine = lines[lines.index(line) + 2]
            
            index1 = subClassLine.find("ref: ", 2)
            index2 = superClassLine.find("ref: ", 2)
            
            subClassId = subClassLine[(index1 + 5):]
            superClassId = superClassLine[(index2 + 5):]
            
            subClassId = subClassId.split(')')[0]
            superClassId = superClassId.split(')')[0]
            if (filtered):
                if (FilteredClassDict.has_key(subClassId) and FilteredClassDict.has_key(superClassId)):
                    print superClassId + "->" + subClassId
                    EdgeList.append((subClassId + ' ', superClassId))
            else:
                EdgeList.append((subClassId + ' ', superClassId))
            
    return EdgeList

def BuildAdjacentList(filename,FilteredClassDict, filtered):
    AdjacentList = {}
    toMatch = 'FAMIX.Inheritance'
    with open(filename) as f:
        content = f.readlines()
    lines = [x.strip('\n') for x in content]
    
    for i, line in enumerate(lines):
        index = line.find(toMatch, 2)
        if (index != -1):
            subClassLine = lines[lines.index(line) + 1]
            superClassLine = lines[lines.index(line) + 2]
            
            index1 = subClassLine.find("ref: ", 2)
            index2 = superClassLine.find("ref: ", 2)
            
            subClassId = subClassLine[(index1 + 5):]
            superClassId = superClassLine[(index2 + 5):]
            
            subClassId = subClassId.split(')')[0]
            superClassId = superClassId.split(')')[0]
            if (filtered):
                if (FilteredClassDict.has_key(subClassId) and FilteredClassDict.has_key(superClassId)):
                    print superClassId + "->" + subClassId
                    if (AdjacentList.has_key(subClassId)):
                        AdjacentList[subClassId].add(superClassId)
                    else:
                        AdjacentList.update({subClassId: {superClassId}})
            else:
                if (AdjacentList.has_key(subClassId)):
                    AdjacentList[subClassId].add(superClassId)
                else:
                    AdjacentList.update({subClassId: {superClassId}})
            
    return AdjacentList
    
    
def BuildInverseList(filename,FilteredClassDict, filtered):
    InverseList = {}
    toMatch = 'FAMIX.Inheritance'
    with open(filename) as f:
        content = f.readlines()
    lines = [x.strip('\n') for x in content]
    
    for i, line in enumerate(lines):
        index = line.find(toMatch, 2)
        if (index != -1):
            subClassLine = lines[lines.index(line) + 1]
            superClassLine = lines[lines.index(line) + 2]
            
            index1 = subClassLine.find("ref: ", 2)
            index2 = superClassLine.find("ref: ", 2)
            
            subClassId = subClassLine[(index1 + 5):]
            superClassId = superClassLine[(index2 + 5):]
            
            subClassId = subClassId.split(')')[0]
            superClassId = superClassId.split(')')[0]
            if (filtered):
                if (FilteredClassDict.has_key(subClassId) and FilteredClassDict.has_key(superClassId)):
                    print superClassId + "->" + subClassId
                    if (InverseList.has_key(superClassId)):
                        InverseList[superClassId].add(subClassId)
                    else:
                        InverseList.update({superClassId: {subClassId}})
            else:
                if (InverseList.has_key(superClassId)):
                    InverseList[superClassId].add(subClassId)
                else:
                    InverseList.update({superClassId: {subClassId}})
            
    return InverseList
 
#if __name__ == '__main__':
#    EdgeList = BuildEdgeList('./src/src.mse', False)
#    with open('sub2super.txt', 'w') as outfile:
#        for line in EdgeList:
#            outfile.writelines(line)
#            outfile.writelines('\n')
    
