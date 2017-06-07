#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 14:52:52 2017

@author: shaojy11
"""

def BuildDependGraph(filename):
    graph = []
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
            
            subClassId = subClassLine[(index1 + 4):]
            superClassId = superClassLine[(index2 + 4):]
            
            subClassId = subClassId.split(')')[0]
            superClassId = superClassId.split(')')[0]
            
            print superClassId + "->" + subClassId
            graph.append((subClassId, superClassId))
            
    return graph


if __name__ == '__main__':
    graph = BuildDependGraph('./src/src.mse')
    with open('sub2super.txt', 'w') as outfile:
        for line in graph:
            outfile.writelines(line)
            outfile.writelines('\n')