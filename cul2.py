# -*- coding: utf-8 -*-
# @Author: Rohan Kumara
# @Date:   2020-10-26 23:43:23
# @Last Modified by:   Rohan Kumara
# @Last Modified time: 2020-10-26 23:45:36

import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
        info = img.read(100000)
        if len(info) < 1: break
        size = size + len(info)
        fhand.write(info)
        