# -*- coding: utf-8 -*-
# @Author: Rohan Kumara
# @Date:   2020-09-28 23:18:52
# @Last Modified by:   Rohan Kumara
# @Last Modified time: 2020-09-28 23:20:29


import sqlite3

con = sqlite3.connect('emaildb.sqlite')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS ')