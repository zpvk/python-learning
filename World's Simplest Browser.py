# -*- coding: utf-8 -*-
# @Author: Rohan Kumara
# @Date:   2020-11-03 23:47:55
# @Last Modified by:   Rohan Kumara
# @Last Modified time: 2020-11-03 23:51:39


import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))