class Employee:
    def setEmployee(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.deig=desig
        self.salary=salary

    def printValues(self):
        print(self.eid)
        print(self.ename)
        print(self.desig)
        print(self.salary)

obj=Employee()
obj.Employee(1001,"Rahul","Tester",250000)
obj.printValues()
