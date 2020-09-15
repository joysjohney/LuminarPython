#step-1  import mysql connector module

import mysql.connector

#step-2  establish connection

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ct978Ad62",
    auth_plugin="mysql_native_password",
    database="luminarpython"

)

#step-3  prepare a cursor object using cursor() method

cursor=db.cursor()

#step-4  execute SQL query using cursor() method

sql="SELECT VERSION()"
cursor.execute(sql)

#step-5  Fetch a single row using fetchone() method

data=cursor.fetchone()
print("Database version : ",data)

#step-6  Disconnect from server

db.close