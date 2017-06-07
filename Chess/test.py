# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 18:38:56 2017

@author: Xinxin
"""
#test

import re
from defination import *
from BuildClassDict import *
from ClassMseParser import *

#build the ClassDict from infile
infile = "./src/src.mse"
ClassDict = BuildClassDict(infile)

dict = ClassMseParser("2033",ClassDict)

