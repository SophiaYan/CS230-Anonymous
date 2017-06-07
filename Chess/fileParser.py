import numpy as np
import os, sys
import glob
import csv
import fnmatch
from stat import *
import json
# allFiles = []
# num = 1
# for root, dirnames, filenames in os.walk(os.getcwd() + '/src'):
# 	for fname in fnmatch.filter(filenames, '*.java'):
# 		filename = os.path.join(root, fname)
# 		# current file name
# 		cur = filename.rsplit('/', 2)[1] + '/' + fname + ':'

# 		with open(filename) as f:
# 			content = f.readlines()
# 		lines = [x.strip('\n') for x in content]
# 		for i,line in enumerate(lines):
# 			index = line.find(' class ')
# 			if (index != -1):
# 				index = index + 7
# 				line = line[index:]
# 				# find all class names in the file
# 				className = line.split(' ')[0]
# 				cur = cur + ' ' + className
# 				print num
# 				num = num + 1
# 				print cur
# 				allFiles.append(str(cur))

# with open('ParseRes.csv','wb') as myfile:
# 	wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
# 	wr.writerow(allFiles)

#os.chdir(os.getcwd() + "/src/controller")
#for filename in glob.glob("*.java"):
#    print filename
    
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
        elif S_ISREG(mode):
            # It's a file, call the callback function (leaf node)
            if f.endswith(".java"):
                subdict = parse(top, f)
                dict["children"].append(subdict)
                callback(f)
        else:
            # Unknown file type, print a message
            print 'Skipping %s' % pathname

def parse(dir, filename):
    leaf = {"name": filename, "size" : 0}
    return leaf
    
def visitfile(file):
    print 'visiting', file

if __name__ == '__main__':
    dict = {"name": "root", "children" :[], "size":0}
    walktree(os.getcwd() + "/src", visitfile, dict)
    with open('src.json', 'w') as outfile:
        json.dump(dict, outfile, ensure_ascii=False, sort_keys = False)