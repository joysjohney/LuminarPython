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
    #print(obj)
    obj.printEmp()

    emplst.append(obj)

for emp in emplst:
    print(emp)