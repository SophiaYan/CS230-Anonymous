# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 18:09:29 2017

@author: Xinxin
"""

# the file to define class definiation

# For class we keep:
#(FAMIX.Class (id: 12)
#		(name 'Math')
#		(modifiers 'public' 'final'))
class Class:
    'Class for "class" type'
    ID = ""
    namd = ""
    modifiers = []
    methods = []
    attributes = []
    loc = 1
    
    def __init__(self, id, name, modifiers, methods, attributes):
       self.ID = id
       self.name = name
       self.modifiers = modifiers
       self.methods = methods
       self.attributes = attributes

    
    def getID(self):
        return self.ID
        
    def getAttributes(self):
       return self.attributes
    
    def getName(self):
        return self.name
       
    def getMethods(self):
        return self.methods
    
    def getModifiers(self):
        return self.modifiers
        
    def getLOC(self):
        return self.loc
        
    def updateLOC(self,loc):
        self.loc = loc
       
    def updateName(self,name):
        self.name = name
        
    def updateAttributes(self, attr):
        self.attributes.append(attr)

    def updateMethods(self, met):
        self.methods.append(met)
       
    def updateModifiers(self,mod):
        self.modifiers.append(mod)
    
    
    
  

# For Method We keep:
#	(FAMIX.Method (id: 4)
#		(name 'updateMoves')
#		(modifiers 'public')
#		(parentType (ref: 1801))
#          (signature 'updateMoves(pieces.Piece[][], int, int)')	       
class Method:
    'Class for "method" type'
    ID = ""
    name = ""
    modifiers = []
    parentType = ""
    signature = ""
    loc = 1
    
    def __init__(self,id,name,modifiers,parenttype, signature):
        self.ID = id
        self.name = name
        self.modifiers = modifiers
        self.parentType = parenttype
        self.signature = signature

    def getID(self):
        return self.ID
        
    def getName(self):
        return self.name
    
    def getModifiers(self):
        return self.modifiers
    
    def getSignature(self):
        return self.signature
    
    def getParentType(self):
        return self.parentType
        
    def getLOC(self):
        return self.loc
        
    def updateLOC(self,loc):
        self.loc = loc
        
    def updateName(self, name):
        self.name = name
        
    def updateModifiers(self,mod):
       self.modifiers.append(mod)  
     
    def updateParentType(self,parT):
        self.parentType = parT
    
    def updateSignture(self,sign):
        self.signature = sign
        
# For Attribute We keep: 
#	(FAMIX.Attribute (id: 109)
#		(name 'undoCach')
#		(modifiers 'private')
#		(parentType (ref: 1546))

class Attribute:
    'Class for "attribute" type'
    ID = ""
    name = ""
    modifiers = []
    parentType = ""
    loc = 1
    
    def __init__(self,id,name,modifiers,parenttype):
        self.ID = id
        self.name = name
        self.modifiers = modifiers
        self.parentType = parenttype
        
    def getID(self):
        return self.ID
        
    def getName(self):
        return self.name
    
    def getModifiers(self):
        return self.modifiers
    
    def getParentType(self):
        return self.parentType
        
    def getLOC(self):
        return self.loc
        
    def updateLOC(self,loc):
        self.loc = loc
     
    def updateName(self,name):
        self.name = name
        
    def updateModifiers(self,mod):
        self.modifiers.append(mod)  
     
    def updateParentType(self,parT):
        self.parentType = parT