import sqlite3

conn=sqlite3.connect("mydb.db")

db=conn.execute("create table student(Name text, rollno integer)")

conn.commit()
conn.close()