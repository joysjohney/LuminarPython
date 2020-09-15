import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ct978Ad62",
    database="luminarpython",
    auth_plugin="mysql_native_password"

)

cursor=db.cursor()

try:
    cursor.execute("SELECT * FROM EMPLOYEE")
    myresult=cursor.fetchall()

    for x in myresult:
        print(x)

except Exception as e:
    db.rollback()
    print(e.args)
finally:
    db.close()