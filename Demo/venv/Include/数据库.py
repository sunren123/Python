from pymysql import *

conn=connect(host="localhost",port=3306,user="root",password="root",database="test",charset="utf8")


cursor=conn.cursor()

ss=cursor.execute("select * from person")
print(ss)
ss=cursor.fetchall()
print(ss)

cursor.close()
conn.close()