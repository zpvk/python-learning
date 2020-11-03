# -*- coding: utf-8 -*-
# @Author: Rohan Kumara
# @Date:   2020-11-03 23:47:55
# @Last Modified by:   Rohan Kumara
# @Last Modified time: 2020-11-03 23:54:43


import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

