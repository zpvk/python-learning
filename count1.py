# -*- coding: utf-8 -*-
# @Author: Rohan Kumara
# @Date:   2020-10-27 23:59:06
# @Last Modified by:   Rohan Kumara
# @Last Modified time: 2020-10-27 23:59:06


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)
