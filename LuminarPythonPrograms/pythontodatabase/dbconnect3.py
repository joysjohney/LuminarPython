import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ct978Ad62",
    database="luminarpython",
    auth_plugin="mysql_native_password"

)

cursor=db.cursor()

sql = """INSERT INTO EMPLOYEE(
        FIRST_NAME, LAST_NAME,AGE,SEX,INCOME) VALUES
        ('Noyal','Thomas',23,'M',17000)"""

try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    db.rollback()
    print(e.args)
finally:
    db.close()