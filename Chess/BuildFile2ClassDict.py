# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 18:38:56 2017

@author: Jingyu
"""

def BuildFile2ClassDict(filename):
    toMatch = 'FAMIX.Class'
    dict = {}
    with open(filename) as f:
        content = f.readlines()
    lines = [x.strip('\n') for x in content]
    
    for i, line in enumerate(lines):
        index = line.find(toMatch, 2)
        if (index != -1):
            sourceAnchorLine = lines[lines.index(line) + 4]
            classNameLine = lines[lines.index(line) + 1]
            index1 = sourceAnchorLine.find('(sourceAnchor', 2)
            index2 = classNameLine.find('(name ')
            if (index1 == -1):
                continue
            if (index2 == -1):
                continue
            
            # find class name
            className = classNameLine[(index2 + 7):]
            className = className.split('\'')[0]
            classId = line[(index + 17):]
            classId = classId.split(')')[0]
            
            # find class file id
            sourceAnchorId = sourceAnchorLine[(index1 + 20):]
            sourceAnchorId = sourceAnchorId.split(')')[0]
            sourceAnchorString = '\t(FAMIX.FileAnchor (id: ' + sourceAnchorId + ')'
            
            # find file name
            fileNameLine = lines[lines.index(sourceAnchorString) + 3]
            fileName = fileNameLine[(fileNameLine.find('(fileName ', 2) + 11):]
            fileName = fileName.split('\'')[0]
    
            if (dict.has_key(fileName) == True):
                dict[fileName].append({classId: className})
            else:
                dict.update({fileName: {classId: className}})
            
            cur = fileName + '(id: ' + sourceAnchorId + '): ' + className
            print cur
    
    return dict