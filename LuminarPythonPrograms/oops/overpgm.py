class Employee:

    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal

    def printVal(self):
        print(self.id)
        print(self.name)
        print(self.sal)

    def __str__(self):
        return self.name


obj=Employee(1011,"Ajay",25000)
obj2=Employee(1012,"Vijay",30000)
obj3=Employee(1013,"Vinay",35000)


ls=[]
ls.append(obj)
ls.append(obj2)
ls.append(obj3)

for emp in ls:
    if(emp.sal>32000):
        print(emp)
