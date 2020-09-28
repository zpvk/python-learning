# -*- coding: utf-8 -*-
# @Author: Rohan Kumara
# @Date:   2020-09-28 23:18:52
# @Last Modified by:   Rohan Kumara
# @Last Modified time: 2020-09-29 01:20:54


import sqlite3

conn = sqlite3.connect('emaildb.sqlite.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

## input data to database
fname = input('Enter file name:')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    org = email.split()
    dom = org[len(org)-1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (dom,))
    row = cur.fetchone()
    if row is None :
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)',(dom,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (dom,))
conn.commit()
    
#https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 1000'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()