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
            subdict = {"name": f, "children" :[], "size": 0}
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
    fileNode = {"name": filename, "children": [], "size" : 0}
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
    
def parseClass(className, classId):
    classNode = {"name": className, "children": [], "size": 0}
    return classNode
    
def visitfile(file):
    print 'visiting', file


if __name__ == '__main__':
    dict = {"name": "root", "children" :[], "size":0}
    walktree(os.getcwd() + "/src", visitfile, dict)
    with open('src.json', 'w') as outfile:
        json.dump(dict, outfile, ensure_ascii=False, sort_keys = False)