# -*- coding: utf-8 -*-
# @Author: Rohan Kumara
# @Date:   2020-10-27 23:58:50
# @Last Modified by:   Rohan Kumara
# @Last Modified time: 2020-11-26 23:56:56


while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done with ':
        break
    print(line)
print('Done!')
