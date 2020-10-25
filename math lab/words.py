# -*- coding: utf-8 -*-
# @Author: Rohan Kumara
# @Date:   2020-10-25 22:19:03
# @Last Modified by:   Rohan Kumara
# @Last Modified time: 2020-10-25 22:20:50



name = input('Enter file:')
handle = open(name, 'r')
counts = dict()

for line in handle:
        words = line.split()