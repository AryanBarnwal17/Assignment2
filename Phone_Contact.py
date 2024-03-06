import sqlite3 as s3
mycon = s3.connect('test.db')
cur = mycon.cursor()
cur.execute("SELECT * FROM STUDENTS")
mycon.commit()
print(cur.fetchall())
mycon.commit()
mycon.close()