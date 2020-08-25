employee={
    "eid":1002,
    "ename":"person",
    "desig":"tester",
    "salary":15000
}

#print employee name

print(employee["ename"])

#check for company is there

print("company" in employee)

#add new record comapany name Luminar

employee["cname"]="Luminar"

#update employee salary = current salary + 5000

employee["salary"]+=5000

#print all key:value pairs

for key in employee:
    print(key,":",employee[key])


