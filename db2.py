import  sqlite3

conn = sqlite3.connect("mydatabase.db")
mycursor = conn.cursor()

sql ="""
select * from books
"""

try:
    mycursor.execute(sql)
except Exception as err:
    print("Something went wrong rolling back")

else:
    print("Everything is fine")
finally:
    print("Closing the connection")
    conn.close()



