# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 18:18:03 2017

@author: Xinxin
"""

from defination import *


# input: class id and pre-build Class Dictionary with funciton BuildClassDict 
# out put a dictionary with {"name":class name,"children":list of method and attribute, "size":0}

def ClassMseParser(cid, ClassDict):
    if cid not in ClassDict:
        print "Class ID not found"
        #return -1
    classObj = ClassDict[cid]
    
    dict = {"name":classObj.getName(),"children":[],"size":classObj.getLOC()}
    for methodObj in classObj.getMethods():
        subDict = {"name":"Method: " + methodObj.getName(),"size":methodObj.getLOC()}#, "childtype":"Method"}
        dict["children"].append(subDict)
    
    for attrObj in classObj.getAttributes():
        subDict = {"name":"Attribute: "+ attrObj.getName(),"size":attrObj.getLOC()}#, "childtype":"Attribute"}
        dict["children"].append(subDict)
    return dict


