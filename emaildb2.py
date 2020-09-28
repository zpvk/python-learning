import sqlite3

con = sqlite3.connect('emaildb.sqlite')
cur = con.cursor()