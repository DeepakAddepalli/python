import  sqlite3

conn = sqlite3.connect("mydatabase.db")
mycursor = conn.cursor()

sql ="""
CREATE TABLE books(

bid integer primary KEY,

title TEXT,
author TEXT
)
"""
mycursor.execute(sql)
conn.close()