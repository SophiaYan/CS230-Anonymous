#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 19:21:53 2017

@author: Jingyu
"""

import re
from defination import *
from BuildClassDict import *
from BuildFile2ClassDict import *

#build the ClassDict from infile
infile = "./src/src.mse"

ClassDict = BuildClassDict(infile)
file2class = BuildFile2ClassDict(infile)