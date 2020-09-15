f=open("employees")
emp={}
for lines in f:
    id,name,desig,salary=lines.rstrip("\n").split(",")
    # 1001,ajay,qa,25000
    if(id not in emp):
        emp[id]={"id":id,"name":name,"desig":desig,"salary":salary}
        # 1001={id:1001,name:ajay,desig:qa,salary:2000}
print(emp)

def fetchData(**kwargs):
    # kwargs={id:1001,property:desig}

    id=str(kwargs["id"])
    # id=1001
    if (id not in emp):
        print("emplyee not exist")
    else:
        if "property" in kwargs:
            val=kwargs["property"]
            print(emp[id][val])

fetchData(id="1002",property="desig")


