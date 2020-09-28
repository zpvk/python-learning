# -*- coding: utf-8 -*-
# @Author: Rohan Kumara
# @Date:   2020-09-28 23:18:52
# @Last Modified by:   Rohan Kumara
# @Last Modified time: 2020-09-28 23:51:47


import sqlite3

con = sqlite3.connect('emaildb.sqlite')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

## input data to database
fname = input('Enter file name:')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startwith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (email,)')
    row = cur.fetchone()
    if row in None :
        cur.execute('')
    