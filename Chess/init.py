#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 19:21:53 2017

@author: Jingyu
"""

# Preparations
# Build dictionaries from MSE file, find the mapping between file and class, between
# Class and Method /Attribute
# Input: working dir/src/src.mse
# Output: ClassDict, file2class Mapping

import re
from defination import *
from BuildClassDict import *
from BuildFile2ClassDict import *


infile = "./src/src.mse"

ClassDict = BuildClassDict(infile)
file2class = BuildFile2ClassDict(infile)