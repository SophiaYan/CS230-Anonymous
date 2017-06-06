import numpy as np
import os
import glob
import csv
import fnmatch

allFiles = []
num = 1
for root, dirnames, filenames in os.walk(os.getcwd() + '/src'):
	for fname in fnmatch.filter(filenames, '*.java'):
		filename = os.path.join(root, fname)
		# current file name
		cur = filename.rsplit('/', 2)[1] + '/' + fname + ':'

		with open(filename) as f:
			content = f.readlines()
		lines = [x.strip('\n') for x in content]
		for i,line in enumerate(lines):
			index = line.find(' class ')
			if (index != -1):
				index = index + 7
				line = line[index:]
				# find all class names in the file
				className = line.split(' ')[0]
				cur = cur + ' ' + className
				print num
				num = num + 1
				print cur
				allFiles.append(str(cur))

with open('ParseRes.csv','wb') as myfile:
	wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
	wr.writerow(allFiles)
