# -*- coding: utf-8 -*-
# @Author: Rohan Kumara
# @Date:   2020-11-03 23:47:55
# @Last Modified by:   Rohan Kumara
# @Last Modified time: 2020-11-04 23:58:52


import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break11
    print(data.decode(), end='')

mysock.close()
