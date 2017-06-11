# -*- coding: utf-8 -*-
"""
Created on Thu May 25 15:15:27 2017

@author: Jingyu
"""

import os, sys
import glob
from stat import *
import json
from ClassMseParser import *
import re
from defination import *
from BuildClassDict import *
from BuildFile2ClassDict import *
from BuildDependGraph import *
import time
# Recursively generate .json file by DFS
# Input: All the files under workingDir/src
# Ouptput: src.json (dict)
# Please run it under the directory above /src
    
@profile(precision=4)
def walktree(top, callback, dict):
    '''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''

    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname)[ST_MODE]
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            #callback(f)
            subdict = {"name": f, "children" :[], "size": 0, "type" : "Folder"}
            walktree(pathname, callback, subdict)
            dict["children"].append(subdict)
            dict["size"] = dict["size"] + subdict["size"]
        elif S_ISREG(mode):
            # It's a file, call the callback function (leaf node)
            if f.endswith(".java"):
                if (file2class.has_key(pathname)):
                    fileNode = parseFile(top, f)
                # fileNode = {"name": f, "size": 100}
                    dict["children"].append(fileNode)
                    dict["size"] = dict["size"] + fileNode["size"]
                    #callback(f)
        else:
            # Unknown file type, print a message
            print 'Skipping %s' % pathname
        

def parseFile(dir, filename):
    fileNode = {"name": filename, "children": [], "size" : 0, "type" : "File"}
    pathname = os.path.join(dir, filename)
    #filename = pathname.rsplit('/', 2)[1] + '/' + filename
    classIds = file2class[pathname]
    fileSize = 0
    for classId in classIds:
        classNode = ClassMseParser(classId,ClassDict)
        fileNode["children"].append(classNode)
        fileSize = fileSize + int(classNode["size"])
    fileNode["size"] = fileSize
    return fileNode
    
    
def visitfile(file):
    print 'visiting', file

@profile(precision=4)
def GenerateDependenceJson(curlevel, InverseList, RankedList, ClassDict, dict):
    for curele in curlevel:
        if (ClassDict.has_key(curele) == False or RankedList.has_key(curele) == False):
            continue
        if (InverseList.has_key(curele)):
            subdicts = {"name": ClassDict[curele].getName(), "children": [], "score": RankedList[curele]}
            GenerateDependenceJson(InverseList[curele], InverseList, RankedList, ClassDict, subdicts)
            dict["children"].append(subdicts)
        else: #leaf node, no descendents
            dict["children"].append({"name": ClassDict[curele].getName(), "score": RankedList[curele]})



if __name__ == '__main__':
 #   start_time = time.clock()
    
    
    # Preparations
    proj = 'cassandra-1.0'
#    top = './src/'
#    infile = top + 'src.mse'
    top = '/Users/shaojy11/Downloads/' + proj + '/'
    infile = top + proj + '.mse'
    
    ClassDict = BuildClassDict(infile)
    [FilteredClassDict, file2class] = BuildFile2ClassDict(infile, top)
    
    filtered = False
    AdjacentList = BuildAdjacentList(infile, FilteredClassDict, filtered)
    TopoList = list(toposort(AdjacentList))
    InverseList = BuildInverseList(infile, FilteredClassDict, filtered)
    EdgeList = BuildEdgeList(infile, FilteredClassDict, filtered)
    RankedList = cal_classrank(EdgeList)
    
    
    # Build 2 trees
    outfile1 = './Results/' + proj + '/' + proj + '_hierarchy.json'
    outfile2 = './Results/' + proj + '/' + proj + '_dependency.json'
    
    hieDict = {"name": "root", "children" :[], "size": 0}
    walktree(top, visitfile, hieDict)
    with open(outfile1, 'w') as outfile:
        json.dump(hieDict, outfile, ensure_ascii = False, sort_keys = False)
        
    dependDict = {"name": "root", "children": []}
    GenerateDependenceJson(TopoList[0], InverseList, RankedList, ClassDict, dependDict)
    with open(outfile2, 'w') as outfile:
        json.dump(dependDict, outfile, ensure_ascii = False, sort_keys = False)
        
        
   # print time.clock() - start_time, "seconds"
