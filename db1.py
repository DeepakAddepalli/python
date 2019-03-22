import  sqlite3

conn = sqlite3.connect("mydatabase.db")
mycursor = conn.cursor()

sql ="""
Insert into books(
title ,
author 
) values(?,?)
"""
books=[
    (
"the monk who said his ferrari","Robbin Sharma"
    )
    ,(
        "my Experiments with truth","M.K.Gandhi"
    ),
    (
        "My experments with food","ramesh"
    )
]

mycursor.executemany(sql,books)
conn.commit()
conn.close()