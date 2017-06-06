import numpy as np
import os
import glob
import csv
import fnmatch

allFiles = []
filename = os.getcwd() + '/src/src.mse'
toMatch = 'FAMIX.Class'
num = 1
print filename
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

		# find class file id
		sourceAnchorId = sourceAnchorLine[(index1 + 20):]
		sourceAnchorId = sourceAnchorId.split(')')[0]

		# find file name
		# TODO

		cur = 'id: ' + sourceAnchorId + ' -- ' + className
		print num
		num = num + 1
		print cur
		allFiles.append(str(cur))

with open('MseParseRes.csv','wb') as myfile:
	wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
	wr.writerow(allFiles)
