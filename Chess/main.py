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

# Recursively generate .json file by DFS
# Input: All the files under workingDir/src
# Ouptput: src.json (dict)
# Please run it under the directory above /src
    
def walktree(top, callback, dict):
    '''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''

    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname)[ST_MODE]
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            callback(f)
            subdict = {"name": f, "children" :[], "size": 0, "type" : "folder"}
            walktree(pathname, callback, subdict)
            dict["children"].append(subdict)
            dict["size"] = dict["size"] + subdict["size"]
        elif S_ISREG(mode):
            # It's a file, call the callback function (leaf node)
            if f.endswith(".java"):
                fileNode = parseFile(top, f)
                # fileNode = {"name": f, "size": 100}
                dict["children"].append(fileNode)
                dict["size"] = dict["size"] + fileNode["size"]
                callback(f)
        else:
            # Unknown file type, print a message
            print 'Skipping %s' % pathname
        

def parseFile(dir, filename):
    fileNode = {"name": filename, "children": [], "size" : 0, "type" : "file"}
    pathname = os.path.join(dir, filename)
    filename = pathname.rsplit('/', 2)[1] + '/' + filename
    classIds = file2class[filename]
    fileSize = 0
    for classId in classIds:
        classNode = ClassMseParser(classId,ClassDict)
        fileNode["children"].append(classNode)
        fileSize = fileSize + int(classNode["size"])
    fileNode["size"] = fileSize
    return fileNode
    
    
def visitfile(file):
    print 'visiting', file


def GenerateDependenceJson(curlevel, InverseList, ClassDict, dict):
    for curele in curlevel:
        if (ClassDict.has_key(curele) == False):
            continue
        if (InverseList.has_key(curele)):
            subdicts = {"name": ClassDict[curele].getName(), "children": [], "score": 0}
            GenerateDependenceJson(InverseList[curele], InverseList, ClassDict, subdicts)
            dict["children"].append(subdicts)
        else: #leaf node, no descendents
            dict["children"].append({"name": ClassDict[curele].getName(), "score": 0})

if __name__ == '__main__':
    
    hieDict = {"name": "root", "children" :[], "size": 0}
    walktree(os.getcwd() + "/src", visitfile, hieDict)
    with open('src_withChildType.json', 'w') as outfile:
        json.dump(hieDict, outfile, ensure_ascii=False, sort_keys = False)
        
    dependDict = {"name": "root", "children": []}
    GenerateDependenceJson(TopoList[0], InverseList, ClassDict, dependDict)
    with open('dependence.json', 'w') as outfile:
        json.dump(dependDict, outfile, ensure_ascii=False, sort_keys = False)