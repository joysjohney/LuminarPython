from functools import *
class Employee:
    def __init__(self,id,name,desig,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.salary=salary

    def printEmp(self):
        print("ID =",self.id)
        print("Name =",self.name)
        print("Designation =",self.desig)
        print("Salary =",self.salary)

    def __str__(self):
        return self.name

emplst=[]
f=open("empdetails","r")

for data in f:
    values=data.rstrip("\n").split(",")

    id=values[0]
    name=values[1]
    desig=values[2]
    salary=values[3]

    obj=Employee(id,name,desig,salary)
    emplst.append(obj)

result1=list(map(lambda emp:emp.name.upper(),emplst))
result2=list(filter(lambda emp:int(emp.salary)>25000,emplst))
result3=list(map(lambda emp:int(emp.salary)+5000,emplst))

print("Employee name to uppercase =",result1)
print("Employee salary above 25000")
for ls in result2:
    print(ls)
print("Updated salary =",result3)

maxsalary=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,list(map(lambda emp:emp.salary,emplst)))
print("Maximum salary =",maxsalary)

maxsalemp=list(filter(lambda emp:emp.salary==maxsalary,emplst))
for emp in maxsalemp:
    print("Maximum salaried employee =",emp)
