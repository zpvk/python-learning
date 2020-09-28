# -*- coding: utf-8 -*-
# @Author: Rohan
# @Date:   2020-09-28 23:11:53
# @Last Modified by:   Your name
# @Last Modified time: 2020-09-28 23:12:53


import sqlite3

con = sqlite3.connect('emaildb.sqlite')
cur = con.cursor()