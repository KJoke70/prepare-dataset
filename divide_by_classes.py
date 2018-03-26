#!/usr/bin/env python2
"""
Script to divide the test set into it's different classes

__author__ = "Martin Lautenbacher"
__version__ = "1.0"
"""

import os
import shutil

test_256_path = 'result_set/256/test/'
result_path = 'test_sets/'
subset_0 = '000000/'
subset_1 = '000001/'
subset_2 = '000002/'
flist_name = 'filelist.txt'

assert os.path.exists(test_256_path + subset_0)
assert os.path.exists(test_256_path + subset_1)
assert os.path.exists(test_256_path + subset_2)
if os.path.exists(result_path):
    shutil.rmtree(result_path)

os.makedirs(result_path)

shutil.copytree(test_256_path + subset_0,result_path + subset_0)
shutil.copytree(test_256_path + subset_1,result_path + subset_1)
shutil.copytree(test_256_path + subset_2,result_path + subset_2)
shutil.copy(test_256_path + flist_name, result_path + flist_name)

os.chdir(result_path)

with open(flist_name) as f:
    filelist = f.readlines()

print 'items on filelist:', len(filelist)
filelist = [x.strip() for x in filelist]

files_0 = []
files_1 = []
files_2 = []
for item in filelist:
    ind = item.find(' ')
    a = item[0:ind]
    b = item[ind+1:]
    if subset_0 in a:
        files_0.append((a, b))
    elif subset_1 in a:
        files_1.append((a, b))
    elif subset_2 in a:
        files_2.append((a, b))
    else:
        print 'ERROR'

classes_0 = [y for x,y in files_0]
classes_0 = set(classes_0)
classes_1 = [y for x,y in files_1]
classes_1 = set(classes_1)
classes_2 = [y for x,y in files_2]
classes_2 = set(classes_2)

for c in classes_0:
    if not os.path.exists(subset_0 + c):
        os.makedirs(subset_0 + c)

for c in classes_1:
    if not os.path.exists(subset_1 + c):
        os.makedirs(subset_1 + c)

for c in classes_2:
    if not os.path.exists(subset_2 + c):
        os.makedirs(subset_2 + c)

flist_0 = open('filelist_0.txt', 'w')
flist_1 = open('filelist_1.txt', 'w')
flist_2 = open('filelist_2.txt', 'w')

i = 0
for f, c in files_0:
    shutil.move(f, subset_0 + c + '/')
    flist_0.write('%s %s\n' % (subset_0 + c + f[f.rfind('/'):], c))
    i += 1

for f, c in files_1:
    shutil.move(f, subset_1 + c + '/')
    flist_1.write('%s %s\n' % (subset_1 + c + f[f.rfind('/'):], c))
    i += 1

for f, c in files_2:
    shutil.move(f, subset_2 + c + '/')
    flist_2.write('%s %s\n' % (subset_2 + c + f[f.rfind('/'):], c))
    i += 1

print 'processed files:', i

flist_0.close()
flist_1.close()
flist_2.close()

filenames = ['filelist_0.txt', 'filelist_1.txt', 'filelist_2.txt']
with open('filelist.txt', 'w') as outfile:
        for fname in filenames:
                    with open(fname) as infile:
                                    outfile.write(infile.read())
